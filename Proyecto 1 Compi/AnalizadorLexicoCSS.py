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
        self.palabrasreservadas = ["var", "for", "while", "if", "else", "do", "continue", "break", "return", "function", "constructor", "class", "Math.pow", "true", "false"]

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

                else:
                    if actual == '#':
                        print("-------Fin del Analisis Lexico-------")
                    else:
                        self.auxlex += actual
                        self.estado = -99

                        #hola

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
                    self.estado = 8
                    self.auxlex += actual
                else: 
                    self.columna -= 1
                    self.indice += 1
                    self.agragarToken(tokens.Signo_Division)
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