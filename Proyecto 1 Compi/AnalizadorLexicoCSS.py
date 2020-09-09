from TokensCSS import tokensCss, TokensCss
from ErroresCSS import ErroresCss, ErrorCss
import os

class AnalizadorLexicoCss:

    def __init__(self):
        self.lista_de_tokens_Css = []
        self.listaErrores_Css = []
        self.estado = 0
        self.auxlex = ""
        self.columna = 0
        self.fila = 1
        self.indice = 0
        self.indiceError = 0
        self.propiedades = ["color", "background-color", "background-image", "border", "Opacity", "background", "text-align", "font-family", "font-style", "font-weight", "font-size", "font", "padding-left", "padding right", "padding-bottom", "padding-top", "padding", "display", "line-height", "width", "height", "margin-top", "margin-right", "margin-bottom", "margin-left", "margin", "border-style", "display", "position", "bottom", "top", "right", "left", "float", "clear", "max-width", "min-width", "max-heigth", "min-height", "url", "border-top", "content"]
        self.unidades_de_medida = ["px", "em", "vh", "vw", "in", "cm", "mm", "pt", "pc",]

    def agragarTokenCss(self, tipoDelToken):
        self.lista_de_tokens_Css.append(TokensCss(tipoDelToken, self.auxlex, self.fila, self.columna,self.indice))
        self.auxlex= ""
        self.estado = 0

    def agragarErroresCss(self, tipoDelToken):
        self.listaErrores_Css.append(ErroresCss(tipoDelToken, self.auxlex, self.fila, self.columna, self.indiceError))
        self.auxlex= ""
        self.estado = 0

    def analizadorCss(self, entrada):
        cadena = entrada + "#"
        contador = 0
        while contador < len(cadena):
            actual = cadena[contador]
            self.columna += 1

            if self.estado == 0:
                if actual.isalpha(): #es una letra
                    self.auxlex += actual
                    self.estado = 1
                elif actual.isdigit(): #es un digito
                    self.auxlex += actual
                    self.estado = 2
                elif actual == '"':
                    self.auxlex += actual
                    self.estado = 3
                elif actual == '/':
                    self.auxlex += actual
                    self.estado = 5
                elif actual == "\n":
                    self.columna = 0
                    self.fila += 1
                    self.estado = 0
                elif actual == "\t":
                    self.columna += 1
                    self.estado = 0
                elif actual == " ":
                    self.estado = 0
                elif actual == '-':
                    self.auxlex += actual
                    self.estado = 11
                elif actual == '*':
                    self.auxlex += actual
                    self.indice +=1
                    self.agragarTokenCss(tokensCss.Signo_Por)
                elif actual == '#':
                    self.auxlex += actual
                    self.estado = 12
                elif actual == '.':
                    self.auxlex += actual
                    self.indice +=1
                    self.agragarTokenCss(tokensCss.Punto)
                elif actual == ':':
                    self.auxlex += actual
                    self.indice +=1
                    self.agragarTokenCss(tokensCss.Dos_Puntos)
                elif actual == '{':
                    self.auxlex += actual
                    self.indice +=1
                    self.agragarTokenCss(tokensCss.Llave_Abierta)
                elif actual == '}':
                    self.auxlex += actual
                    self.indice +=1
                    self.agragarTokenCss(tokensCss.Llave_Cerrada)
                elif actual == ';':
                    self.auxlex += actual
                    self.indice +=1
                    self.agragarTokenCss(tokensCss.PuntoYComa)
                elif actual == '%':
                    self.auxlex += actual
                    self.indice +=1
                    self.agragarTokenCss(tokensCss.Porcentaje)
                elif actual == '(':
                    self.auxlex += actual
                    self.indice +=1
                    self.agragarTokenCss(tokensCss.Parentesis_Abierto)
                elif actual == ')':
                    self.auxlex += actual
                    self.indice +=1
                    self.agragarTokenCss(tokensCss.Parentesis_Cerrado)
                elif actual == ',':
                    self.auxlex += actual
                    self.indice +=1
                    self.agragarTokenCss(tokensCss.Coma)
                else:
                    if actual == '#' and contador == (len(cadena) - 1):
                        print("-------Fin del Analisis Lexico-------")
                    else:
                        self.auxlex += actual
                        self.estado = -99

            elif self.estado == 1:
                if actual.isalpha() or actual.isdigit() or actual == "-":
                    self.estado = 1
                    self.auxlex += actual
                else:
                    if self.auxlex in self.propiedades:
                        self.columna -= 1
                        self.indice += 1
                        self.agragarTokenCss(tokensCss.Propiedad)
                        self.auxlex = ""
                    elif self.auxlex in self.unidades_de_medida:
                        self.columna -= 1
                        self.indice += 1
                        self.agragarTokenCss(tokensCss.Unidades_De_Medida)
                        self.auxlex = ""
                    else:
                        self.columna -= 1
                        self.indice += 1
                        self.agragarTokenCss(tokensCss.Identificador)
                        self.auxlex = ""
                    contador -= 1

            elif self.estado == 2:
                if actual.isdigit():
                    self.estado = 2
                    self.auxlex += actual
                elif actual == ".":
                    self.auxlex += actual
                    self.estado = 9
                else: 
                    self.columna -= 1
                    self.indice += 1
                    self.agragarTokenCss(tokensCss.Digito)
                    self.auxlex = ""
                    contador -= 1

            elif self.estado == 3:
                if actual != '"':
                    self.estado = 3
                    self.auxlex += actual
                else:
                    self.auxlex += actual
                    self.estado = 4

            elif self.estado == 4:
                    self.columna -= 1
                    self.indice += 1
                    self.agragarTokenCss(tokensCss.Cadena)
                    self.auxlex = ""
                    contador -= 1

            elif self.estado == 5:
                if actual == "*":
                    self.estado = 6
                    self.auxlex += actual
                else: 
                    self.columna -= 1
                    self.indice += 1
                    self.agragarTokenCss(tokensCss.Signo_Division)
                    self.auxlex = ""
                    contador -= 1

            elif self.estado == 6:
                if actual != "*":
                    self.estado = 6
                    self.auxlex += actual
                    if actual == "\n":
                        self.columna = 0
                        self.fila += 1
                        self.estado = 6
                else: 
                    self.auxlex += actual
                    self.estado = 7

            elif self.estado == 7:
                if actual == "/":
                    self.estado = 8
                    self.auxlex += actual
                else: 
                    self.auxlex += actual
                    self.estado = -99

            elif self.estado == 8:
                    self.columna -= 1
                    self.indice += 1
                    self.agragarTokenCss(tokensCss.Comentario_Multilinea)
                    self.auxlex = ""
                    contador -= 1

            elif self.estado == 9:
                if actual.isdigit():
                    self.estado = 10
                    self.auxlex += actual
                elif actual == "\n":
                    self.columna = 0
                    self.fila += 1
                    self.estado = -99
                else:
                    self.auxlex += actual
                    self.estado = -99

            elif self.estado == 10:
                if actual.isdigit():
                    self.estado = 10
                    self.auxlex += actual
                else:
                    self.columna -= 1
                    self.indice += 1
                    self.agragarTokenCss(tokensCss.Numero_Decimal)
                    self.auxlex = ""
                    contador -= 1

            elif self.estado == 11:
                if actual.isalpha() or actual == "-":
                    self.estado = 1
                    self.auxlex += actual
                elif actual.isdigit():
                    self.estado = 2
                    self.auxlex += actual
                else: 
                    self.columna -= 1
                    self.indice += 1
                    self.agragarTokenCss(tokensCss.Guion)
                    self.auxlex = ""
                    contador -= 1

            elif self.estado == 12:
                if actual.isalpha() or actual.isdigit():
                    self.estado = 13
                    self.auxlex += actual
                else: 
                    self.columna -= 1
                    self.indice += 1
                    self.agragarTokenCss(tokensCss.Numeral)
                    self.auxlex = ""
                    contador -= 1

            elif self.estado == 13:
                if actual.isalpha() or actual.isdigit():
                    self.estado = 13
                    self.auxlex += actual
                else: 
                    self.columna -= 1
                    self.indice += 1
                    self.agragarTokenCss(tokensCss.Hexadecimal)
                    self.auxlex = ""
                    contador -= 1
            
            elif self.estado == -99:
                self.columna -=1
                self.indiceError += 1
                self.agragarErroresCss(ErrorCss.desconocido)
                self.auxlex = ""
                contador -= 1

            contador += 1

    def analizarArchivoCss(self, ruta):  
        if os.path.isfile(ruta):
            archivo = open(ruta, "r")
            self.analizadorCss(archivo.read())
            archivo.close()

    def imprimirListaTokensCss(self):
        for token in self.lista_de_tokens_Css:
            print("------------------------------------------------------------------------------------")
            print('Indice = {}    Token = {}    Lexema = {}    Fila = {}    Columna = {}'.format(token.getIndice(), token.getTipo(), token.getAuxlex(), token.getFila(), token.getColumna()))
            print("------------------------------------------------------------------------------------")

    def imprimirListaErroresCss(self):
        for error in self.listaErrores_Css:
            print("************************************************************************************")
            print('TOKEN => {}     LEXEMA => {}     FILA => {}     COLUMNA => {}     INDICE => {}'.format(error.getTipo(), error.getAuxlex(), error.getFila(), error.getColumna(), error.getIndice()))