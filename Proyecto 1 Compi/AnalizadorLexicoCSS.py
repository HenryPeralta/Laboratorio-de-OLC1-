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
        self.sin_errores = ""
        self.salida_consola = ""

    def agragarTokenCss(self, tipoDelToken):
        self.lista_de_tokens_Css.append(TokensCss(tipoDelToken, self.auxlex, self.fila, self.columna,self.indice))
        self.sin_errores += self.auxlex
        self.auxlex= ""
        self.estado = 0
        self.sin_errores += self.auxlex

    def agragarErroresCss(self, tipoDelToken):
        self.listaErrores_Css.append(ErroresCss(tipoDelToken, self.auxlex, self.fila, self.columna, self.indiceError))
        self.auxlex= ""
        self.estado = 0

    def analizadorCss(self, entrada):
        cadena = entrada + "#"
        contador = 0
        while contador <= (len(cadena) -1):
            actual = cadena[contador]
            self.columna += 1

            if self.estado == 0:
                if actual.isalpha():
                    self.auxlex += actual
                    self.estado = 1
                    self.salida_consola += "Estado S0 -> S1 con una Letra " + actual + "\n"
                    print("Estado S0 -> S1 con una Letra " + actual)
                elif actual.isdigit(): #es un digito
                    self.auxlex += actual
                    self.estado = 2
                    self.salida_consola += "Estado S0 -> S2 con un Digito " + actual + "\n"
                elif actual == '"':
                    self.auxlex += actual
                    self.estado = 3
                    self.salida_consola += "Estado S0 -> S3 con una Comilla Doble " + actual + "\n"
                elif actual == '/':
                    self.auxlex += actual
                    self.estado = 5
                    self.salida_consola += "Estado S0 -> S5 con una Diagonal " + actual + "\n"
                elif actual == "\n":
                    self.columna = 0
                    self.fila += 1
                    self.sin_errores += actual
                    self.estado = 0
                elif actual == "\t":
                    self.columna += 1
                    self.sin_errores += actual
                    self.estado = 0
                elif actual == " ":
                    self.estado = 0
                    self.sin_errores += actual
                elif actual == '-':
                    self.auxlex += actual
                    self.estado = 11
                    self.salida_consola += "Estado S0 -> S11 con una Diagonal " + actual + "\n"
                elif actual == '*':
                    self.auxlex += actual
                    self.indice +=1
                    self.agragarTokenCss(tokensCss.Signo_Por)
                    self.salida_consola += "Estado S0 -> S0 con un Asterisco " + actual + "\n"
                    self.salida_consola += "--> Finalizo en el Estado 0 y es un Asterisco" + "\n" + "\n"
                elif actual == '#':
                    self.auxlex += actual
                    self.estado = 12
                    self.salida_consola += "Estado S0 -> S12 con un Numeral " + actual + "\n"
                elif actual == '.':
                    self.auxlex += actual
                    self.indice +=1
                    self.agragarTokenCss(tokensCss.Punto)
                    self.salida_consola += "Estado S0 -> S0 con un Punto " + actual + "\n"
                    self.salida_consola += "--> Finalizo en el Estado 0 y es un Punto" + "\n" + "\n"
                elif actual == ':':
                    self.auxlex += actual
                    self.indice +=1
                    self.agragarTokenCss(tokensCss.Dos_Puntos)
                    self.salida_consola += "Estado S0 -> S0 con Dos Puntos " + actual + "\n"
                    self.salida_consola += "--> Finalizo en el Estado 0 y son Dos Puntos" + "\n" + "\n"
                elif actual == '{':
                    self.auxlex += actual
                    self.indice +=1
                    self.agragarTokenCss(tokensCss.Llave_Abierta)
                    self.salida_consola += "Estado S0 -> S0 con una Llave Abierta " + actual + "\n"
                    self.salida_consola += "--> Finalizo en el Estado 0 y es una Llave Abierta" + "\n" + "\n"
                elif actual == '}':
                    self.auxlex += actual
                    self.indice +=1
                    self.agragarTokenCss(tokensCss.Llave_Cerrada)
                    self.salida_consola += "Estado S0 -> S0 con una Llave Cerrada " + actual + "\n"
                    self.salida_consola += "--> Finalizo en el Estado 0 y es una Llave Cerrada" + "\n" + "\n"
                elif actual == ';':
                    self.auxlex += actual
                    self.indice +=1
                    self.agragarTokenCss(tokensCss.PuntoYComa)
                    self.salida_consola += "Estado S0 -> S0 con un Punto y Coma " + actual + "\n"
                    self.salida_consola += "--> Finalizo en el Estado 0 y es un Punto y Coma" + "\n" + "\n"
                elif actual == '%':
                    self.auxlex += actual
                    self.indice +=1
                    self.agragarTokenCss(tokensCss.Porcentaje)
                    self.salida_consola += "Estado S0 -> S0 con un Porcentaje " + actual + "\n"
                    self.salida_consola += "--> Finalizo en el Estado 0 y es un Porcentaje" + "\n" + "\n"
                elif actual == '(':
                    self.auxlex += actual
                    self.indice +=1
                    self.agragarTokenCss(tokensCss.Parentesis_Abierto)
                    self.salida_consola += "Estado S0 -> S0 con un Parentesis Abierto " + actual + "\n"
                    self.salida_consola += "--> Finalizo en el Estado 0 y es un Parentesis Abierto" + "\n" + "\n"
                elif actual == ')':
                    self.auxlex += actual
                    self.indice +=1
                    self.agragarTokenCss(tokensCss.Parentesis_Cerrado)
                    self.salida_consola += "Estado S0 -> S0 con un Parentesis Cerrado " + actual + "\n"
                    self.salida_consola += "--> Finalizo en el Estado 0 y es un Parentesis Cerrado" + "\n" + "\n"
                elif actual == ',':
                    self.auxlex += actual
                    self.indice +=1
                    self.agragarTokenCss(tokensCss.Coma)
                    self.salida_consola += "Estado S0 -> S0 con una Coma " + actual + "\n"
                    self.salida_consola += "--> Finalizo en el Estado 0 y es una Coma" + "\n" + "\n"
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
                    self.salida_consola += "Estado S1 -> S1 con una Letra " + actual + "\n"
                    print("Estado S1 -> S1 con una Letra " + actual)
                else:
                    if self.auxlex in self.propiedades:
                        self.columna -= 1
                        self.indice += 1
                        self.agragarTokenCss(tokensCss.Propiedad)
                        self.auxlex = ""
                        self.salida_consola += "--> Finalizo en el Estado 1 y es una Propiedad" + "\n" + "\n"                        
                        print("--> Finalizo en el Estado 1 y es una Propiedad")
                        print("\n")
                    elif self.auxlex in self.unidades_de_medida:
                        self.columna -= 1
                        self.indice += 1
                        self.agragarTokenCss(tokensCss.Unidades_De_Medida)
                        self.auxlex = ""
                        self.salida_consola += "--> Finalizo en el Estado 1 y es una Unidad De Medida" + "\n" + "\n"
                        print("--> Finalizo en el Estado 1 y es una Unidad De Medida")
                        print("\n")
                    else:
                        self.columna -= 1
                        self.indice += 1
                        self.agragarTokenCss(tokensCss.Identificador)
                        self.auxlex = ""
                        self.salida_consola += "--> Finalizo en el Estado 1 y es un Identificador" + "\n" + "\n"
                        print("--> Finalizo en el Estado 1 y es un Identificador")
                        print("\n")
                    contador -= 1

            elif self.estado == 2:
                if actual.isdigit():
                    self.estado = 2
                    self.auxlex += actual
                    self.salida_consola += "Estado S2 -> S2 con un Digito " + actual + "\n"
                elif actual == ".":
                    self.auxlex += actual
                    self.estado = 9
                    self.salida_consola += "Estado S2 -> S9 con un Punto " + actual + "\n"
                else: 
                    self.columna -= 1
                    self.indice += 1
                    self.agragarTokenCss(tokensCss.Digito)
                    self.auxlex = ""
                    self.salida_consola += "--> Finalizo en el Estado 2 y es un Digito" + "\n" + "\n"
                    contador -= 1

            elif self.estado == 3:
                if actual != '"':
                    self.estado = 3
                    self.auxlex += actual
                    if actual == "\n":
                        self.columna = 0
                        self.fila += 1
                        self.estado = 3
                    self.salida_consola += "Estado S3 -> S3 con un Caracter " + actual + "\n"
                else:
                    self.auxlex += actual
                    self.estado = 4
                    self.salida_consola += "Estado S3 -> S4 con una Comilla Doble " + actual + "\n"

            elif self.estado == 4:
                    self.columna -= 1
                    self.indice += 1
                    self.agragarTokenCss(tokensCss.Cadena)
                    self.auxlex = ""
                    self.salida_consola += "--> Finalizo en el Estado 4 y es un Comentario" + "\n" + "\n"
                    contador -= 1

            elif self.estado == 5:
                if actual == "*":
                    self.estado = 6
                    self.auxlex += actual
                    self.salida_consola += "Estado S5 -> S6 con una Diagonal " + actual + "\n"
                else: 
                    self.columna -= 1
                    self.indice += 1
                    self.agragarTokenCss(tokensCss.Signo_Division)
                    self.auxlex = ""
                    self.salida_consola += "--> Finalizo en el Estado 5 y es una Diagonal" + "\n" + "\n"
                    contador -= 1

            elif self.estado == 6:
                if actual != "*":
                    self.estado = 6
                    self.auxlex += actual
                    if actual == "\n":
                        self.columna = 0
                        self.fila += 1
                        self.estado = 6
                    self.salida_consola += "Estado S6 -> S6 con un Caracter " + actual + "\n"
                else: 
                    self.auxlex += actual
                    self.estado = 7
                    self.salida_consola += "Estado S6 -> S7 con un Asterisco " + actual + "\n"

            elif self.estado == 7:
                if actual == "/":
                    self.estado = 8
                    self.auxlex += actual
                    self.salida_consola += "Estado S7 -> S8 con una Diagonal " + actual + "\n"
                elif actual != "*":
                    self.estado = 6
                    self.auxlex += actual
                    if actual == "\n":
                        self.columna = 0
                        self.fila += 1
                        self.estado = 6
                    self.salida_consola += "Estado S7 -> S6 con un caracter " + actual + "\n" 
                else:
                    actual == "*" 
                    self.estado = 7
                    self.auxlex += actual
                    self.salida_consola += "Estado S7 -> S7 con un Asterisco " + actual + "\n"

            elif self.estado == 8:
                    print("------->"+ self.auxlex)
                    self.sin_errores += self.auxlex
                    self.auxlex = ""
                    self.columna -= 1
                    self.indice += 1
                    self.estado = 0
                    self.salida_consola += "--> Finalizo en el Estado 8 y es un Comentario" + "\n" + "\n"
                    contador -= 1
                    
            elif self.estado == 9:
                if actual.isdigit():
                    self.estado = 10
                    self.auxlex += actual
                    self.salida_consola += "Estado S9 -> S10 con un Digito " + actual + "\n"
                elif actual == "\n":
                    self.columna = 0
                    self.fila += 1
                    self.estado = -99
                    self.salida_consola += "Se Esperaba un Digito" + "\n" + "\n"
                else:
                    self.auxlex += actual
                    self.estado = -99
                    self.salida_consola += "Se Esperaba un Digito" + "\n" + "\n"

            elif self.estado == 10:
                if actual.isdigit():
                    self.estado = 10
                    self.auxlex += actual
                    self.salida_consola += "Estado S10 -> S10 con un Digito " + actual + "\n"
                else:
                    self.columna -= 1
                    self.indice += 1
                    self.agragarTokenCss(tokensCss.Numero_Decimal)
                    self.auxlex = ""
                    self.salida_consola += "--> Finalizo en el Estado 10 y es un Decimal" + "\n" + "\n"
                    contador -= 1

            elif self.estado == 11:
                if actual.isalpha() or actual == "-":
                    self.estado = 1
                    self.auxlex += actual
                    self.salida_consola += "Estado S11 -> S11 con un Digito " + actual + "\n"
                elif actual.isdigit():
                    self.estado = 2
                    self.auxlex += actual
                    self.salida_consola += "Estado S11 -> S2 con un Digito " + actual + "\n"
                else: 
                    self.columna -= 1
                    self.indice += 1
                    self.agragarTokenCss(tokensCss.Guion)
                    self.auxlex = ""
                    self.salida_consola += "--> Finalizo en el Estado 11 y es un Guion" + "\n" + "\n"
                    contador -= 1

            elif self.estado == 12:
                if actual.isalpha() or actual.isdigit():
                    self.estado = 13
                    self.auxlex += actual
                    self.salida_consola += "Estado S12 -> S13 con un Digito o Letra " + actual + "\n"
                else: 
                    self.columna -= 1
                    self.indice += 1
                    self.agragarTokenCss(tokensCss.Numeral)
                    self.auxlex = ""
                    self.salida_consola += "--> Finalizo en el Estado 12 y es un Numeral" + "\n" + "\n"
                    contador -= 1

            elif self.estado == 13:
                if actual.isalpha() or actual.isdigit():
                    self.estado = 13
                    self.auxlex += actual
                    self.salida_consola += "Estado S13 -> S13 con un Digito o Letra " + actual + "\n"
                else: 
                    self.columna -= 1
                    self.indice += 1
                    self.agragarTokenCss(tokensCss.Hexadecimal)
                    self.auxlex = ""
                    self.salida_consola += "--> Finalizo en el Estado 13 y es un Hexadecimal" + "\n" + "\n"
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

    def generarHtml_Css(self):
        file = open ("C:/Reportes_Compi/Lista_Tokens_Css.html", "w")
        file.write("<!DOCTYPE html>\n<html>\n")
        file.write("<head>\n")
        file.write("<meta charset = " + "'utf-8'" + " />\n")
        file.write("<title> Reporte de Tokens</title>\n")
        file.write("<meta name = " + "'viewport'" + " content = " + "'initial-scale=1.0; maximum-scale=1.0; width=device-width;'" + ">\n")
        file.write("<Style type = " + "'text/css'" + ">\n")
        file.write("@import url(https://fonts.googleapis.com/css?family=Roboto:400,500,700,300,100);;\n")
        file.write("body{\n")
        file.write("    background: rgba(204, 204, 204, 1);\n")
        file.write("    background: -moz-linear-gradient(top, rgba(204, 204, 204, 1) 0%, rgba(255, 255, 255, 1) 100%);\n")
        file.write("    background: -webkit-gradient(left top, left bottom, color-stop(0%, rgba(204, 204, 204, 1)), color - stop(100%, rgba(255, 255, 255, 1)));\n")
        file.write("    background: -webkit-linear-gradient(top, rgba(204, 204, 204, 1) 0%, rgba(255, 255, 255, 1) 100%);\n")
        file.write("    background: -o-linear-gradient(top, rgba(204, 204, 204, 1) 0%, rgba(255, 255, 255, 1) 100%);\n")
        file.write("    background: -ms-linear-gradient(top, rgba(204, 204, 204, 1) 0%, rgba(255, 255, 255, 1) 100%);\n")
        file.write("    background: linear-gradient(to bottom, rgba(204, 204, 204, 1) 0%, rgba(255, 255, 255, 1) 100%);\n")
        file.write("    filter: progid: DXImageTransform.Microsoft.gradient(startColorstr = '#cccccc', endColorstr = '#ffffff', GradientType = 0);\n")
        file.write("    font-family: " + "'Roboto'" + ", helvetica, arial, sans-serif;\n")
        file.write("    font-size: 16px;\n")
        file.write("    font-weight: 400;\n")
        file.write("    text-rendering: optimizeLegibility;\n")
        file.write("}\n")

        file.write("div.table-title{\n")
        file.write("    display: block;\n")
        file.write("    margin: auto;\n")
        file.write("    max-width: 600px;\n")
        file.write ("   padding: 5px;\n")
        file.write("    width: 100 %;\n")
        file.write("}\n")

        file.write(".table-title h3{\n")
        file.write("    color: #fff;\n")
        file.write("    font-size: 30px;\n")
        file.write("    font-weight: 400;\n")
        file.write("    font-style:normal;\n")
        file.write("    font-family: " + "'Roboto'" + ", helvetica, arial, sans-serif;\n")
        file.write("    text-shadow: 1px 1px black;\n")
        file.write("    text-transform:uppercase;\n")
        file.write("}\n")

        file.write(".table-fill{\n")
        file.write("    background: white;\n")
        file.write("    border-radius:3px;\n")
        file.write("    border-color: black;\n")
        file.write("    border-collapse: collapse;\n")
        file.write("    height: 320px;\n")
        file.write("    margin: auto;\n")
        file.write("    max-width: 600px;\n")
        file.write("    padding: 5px;\n")
        file.write("    width: 100 %;\n")
        file.write("    box-shadow: 30px 30px 30px 30px rgba(1, 0.1, 0.1, 0.1);\n")
        file.write("    animation: float 5s infinite;\n")
        file.write("}\n")

        file.write("th{\n")
        file.write("    color:#D5DDE5;\n")
        file.write("    background:#1b1e24;\n")
        file.write("    border-bottom:4px solid #9ea7af;\n")
        file.write("    border-right: 1px solid #343a45;\n")
        file.write("    font-size:23px;\n")
        file.write("    font-weight: 100;\n")
        file.write("    padding: 24px;\n")
        file.write("    text-align:left;\n")
        file.write("    text-shadow: 0 1px 1px rgba(0, 0, 0, 0.1);\n")
        file.write("    vertical-align:middle;\n")
        file.write("}\n")

        file.write("th:last-child {\n")
        file.write("    border-top - right-radius:3px;\n")
        file.write("    border-right:none;\n")
        file.write("}\n")

        file.write("tr{\n")
        file.write("    border-top: 1px solid #C1C3D1;\n")
        file.write("    border-bottom -: 1px solid #C1C3D1;\n")
        file.write("    color:#666B85;\n")
        file.write("    font-size:16px;\n")
        file.write("    font-weight:normal;\n")
        file.write("    text-shadow: 0 1px 1px rgba(256, 256, 256, 0.1);\n")
        file.write("}\n")

        file.write("tr: hover td{\n")
        file.write("    background:#4E5066;\n")
        file.write("    color:#FFFFFF;\n")
        file.write("    border-top: 1px solid #22262e;\n")
        file.write("}\n")

        file.write("tr: first-child{\n")
        file.write("    border-top:none;\n")
        file.write("}\n")

        file.write("tr: last-child{\n")
        file.write("    border-bottom:none;\n")
        file.write("}\n")

        file.write("tr: nth-child(odd) td{\n")
        file.write("    background:#EBEBEB;\n")
        file.write("}\n")

        file.write("tr: nth-child(odd):hover td{\n")
        file.write("    background:#4E5066;\n")
        file.write("}\n")

        file.write("tr: last-child td: first-child{\n")
        file.write("    border-bottom-left-radius:3px;\n")
        file.write("}\n")

        file.write("tr: last-child td: last-child{\n")
        file.write("    border-bottom-right-radius:3px;\n")
        file.write("}\n")

        file.write("td{\n")
        file.write("    background:#FFFFFF;\n")
        file.write("    padding: 20px;\n")
        file.write("    text-align:left;\n")
        file.write("    vertical-align:middle;\n")
        file.write("    font-weight:300;\n")
        file.write("    font-size:18px;\n")
        file.write("    text-shadow: -1px -1px 1px rgba(0, 0, 0, 0.1);\n")
        file.write("    border-right: 1px solid #C1C3D1;\n")
        file.write("}\n")

        file.write("td: last-child{\n")
        file.write("    border-right: 0px;\n")
        file.write("}\n")

        file.write("th.text-left {\n")
        file.write("    text-align: left;\n")
        file.write("}\n")

        file.write("th.text-center {\n")
        file.write("    text-align: center;\n")
        file.write("}\n")

        file.write("th.text-right {\n")
        file.write("    text-align: right;\n")
        file.write("}\n")

        file.write("td.text-left {\n")
        file.write("    text-align: left;\n")
        file.write("}\n")

        file.write("td.text-center {\n")
        file.write("    text-align: center;\n")
        file.write("}\n")

        file.write("td.text-right {\n")
        file.write("    text-align: right;\n")
        file.write("}\n")
        file.write(".encabezado h3{\n")
        file.write("    font-family: arial;\n")
        file.write("    color: #fff;\n")
        file.write("    position: relative;\n")
        file.write("    left: 5 %;\n")
        file.write("    top: 5 %;\n")

        file.write("    text-shadow: 0 1px 1px black;\n")
        file.write("}\n")

        file.write("</Style>\n")
        file.write("</head>\n")

        file.write("<body>\n")

        file.write("<div class=" + "'encabezado'" + ">\n")
        file.write("<h3>Universidad de San Carlos de Guatemala</h3>\n")
        file.write("<h3>Facultad de Ingenieria</h3>\n")
        file.write("<h3>Organizacion De Lenguajes y Compiladores 1</h3>\n")

        file.write("</div>\n")
        file.write("<div class=" + "'table-title'" + ">\n")
        file.write("<h3>Tabla de Simbolos</h3>\n")
        file.write("</div>\n")
        file.write("<table class=" + "'table-fill'" + ">\n")
        file.write("<thead>\n")
        file.write("<tr>\n")
        file.write("<th class=" + "'text-left'" + ">No.</th>\n")
        file.write("<th class=" + "'text-left'" + ">Token</th>\n")
        file.write("<th class=" + "'text-left'" + ">Lexema</th>\n")
        file.write("<th class=" + "'text-left'" + ">Fila</th>\n")
        file.write("<th class=" + "'text-left'" + ">Columna</th>\n")

        file.write("</tr>\n")

        file.write("</thead>\n")

        file.write("<tbody class=" + "'table-hover'" + ">")

        if len(self.lista_de_tokens_Css) != 0:
            contador = 1
            for token in self.lista_de_tokens_Css:
                file.write("<tr>")
                file.write("    <td>{}</td>".format(contador))
                file.write("    <td>{}</td>".format(token.getTipo()))
                file.write("    <td>{}</td>".format(token.getAuxlex()))
                file.write("    <td>{}</td>".format(token.getFila()))
                file.write("    <td>{}</td>".format(token.getColumna()))
                file.write("</tr>")
                contador += 1

        file.close()

        os.system("start C:/Reportes_Compi/Lista_Tokens_Css.html")

    def generarErrores_Css(self):
        file = open ("C:/Reportes_Compi/Errores_Lexicos_Css.html", "w")
        file.write("<!DOCTYPE html>\n<html>\n")
        file.write("<head>\n")
        file.write("<meta charset = " + "'utf-8'" + " />\n")
        file.write("<title> Reporte de Tokens</title>\n")
        file.write("<meta name = " + "'viewport'" + " content = " + "'initial-scale=1.0; maximum-scale=1.0; width=device-width;'" + ">\n")
        file.write("<Style type = " + "'text/css'" + ">\n")
        file.write("@import url(https://fonts.googleapis.com/css?family=Roboto:400,500,700,300,100);;\n")
        file.write("body{\n")
        file.write("    background: rgba(204, 204, 204, 1);\n")
        file.write("    background: -moz-linear-gradient(top, rgba(204, 204, 204, 1) 0%, rgba(255, 255, 255, 1) 100%);\n")
        file.write("    background: -webkit-gradient(left top, left bottom, color-stop(0%, rgba(204, 204, 204, 1)), color - stop(100%, rgba(255, 255, 255, 1)));\n")
        file.write("    background: -webkit-linear-gradient(top, rgba(204, 204, 204, 1) 0%, rgba(255, 255, 255, 1) 100%);\n")
        file.write("    background: -o-linear-gradient(top, rgba(204, 204, 204, 1) 0%, rgba(255, 255, 255, 1) 100%);\n")
        file.write("    background: -ms-linear-gradient(top, rgba(204, 204, 204, 1) 0%, rgba(255, 255, 255, 1) 100%);\n")
        file.write("    background: linear-gradient(to bottom, rgba(204, 204, 204, 1) 0%, rgba(255, 255, 255, 1) 100%);\n")
        file.write("    filter: progid: DXImageTransform.Microsoft.gradient(startColorstr = '#cccccc', endColorstr = '#ffffff', GradientType = 0);\n")
        file.write("    font-family: " + "'Roboto'" + ", helvetica, arial, sans-serif;\n")
        file.write("    font-size: 16px;\n")
        file.write("    font-weight: 400;\n")
        file.write("    text-rendering: optimizeLegibility;\n")
        file.write("}\n")

        file.write("div.table-title{\n")
        file.write("    display: block;\n")
        file.write("    margin: auto;\n")
        file.write("    max-width: 600px;\n")
        file.write ("   padding: 5px;\n")
        file.write("    width: 100 %;\n")
        file.write("}\n")

        file.write(".table-title h3{\n")
        file.write("    color: #fff;\n")
        file.write("    font-size: 30px;\n")
        file.write("    font-weight: 400;\n")
        file.write("    font-style:normal;\n")
        file.write("    font-family: " + "'Roboto'" + ", helvetica, arial, sans-serif;\n")
        file.write("    text-shadow: 1px 1px black;\n")
        file.write("    text-transform:uppercase;\n")
        file.write("}\n")

        file.write(".table-fill{\n")
        file.write("    background: white;\n")
        file.write("    border-radius:3px;\n")
        file.write("    border-color: black;\n")
        file.write("    border-collapse: collapse;\n")
        file.write("    height: 320px;\n")
        file.write("    margin: auto;\n")
        file.write("    max-width: 600px;\n")
        file.write("    padding: 5px;\n")
        file.write("    width: 100 %;\n")
        file.write("    box-shadow: 30px 30px 30px 30px rgba(1, 0.1, 0.1, 0.1);\n")
        file.write("    animation: float 5s infinite;\n")
        file.write("}\n")

        file.write("th{\n")
        file.write("    color:#D5DDE5;\n")
        file.write("    background:#1b1e24;\n")
        file.write("    border-bottom:4px solid #9ea7af;\n")
        file.write("    border-right: 1px solid #343a45;\n")
        file.write("    font-size:23px;\n")
        file.write("    font-weight: 100;\n")
        file.write("    padding: 24px;\n")
        file.write("    text-align:left;\n")
        file.write("    text-shadow: 0 1px 1px rgba(0, 0, 0, 0.1);\n")
        file.write("    vertical-align:middle;\n")
        file.write("}\n")

        file.write("th:last-child {\n")
        file.write("    border-top - right-radius:3px;\n")
        file.write("    border-right:none;\n")
        file.write("}\n")

        file.write("tr{\n")
        file.write("    border-top: 1px solid #C1C3D1;\n")
        file.write("    border-bottom -: 1px solid #C1C3D1;\n")
        file.write("    color:#666B85;\n")
        file.write("    font-size:16px;\n")
        file.write("    font-weight:normal;\n")
        file.write("    text-shadow: 0 1px 1px rgba(256, 256, 256, 0.1);\n")
        file.write("}\n")

        file.write("tr: hover td{\n")
        file.write("    background:#4E5066;\n")
        file.write("    color:#FFFFFF;\n")
        file.write("    border-top: 1px solid #22262e;\n")
        file.write("}\n")

        file.write("tr: first-child{\n")
        file.write("    border-top:none;\n")
        file.write("}\n")

        file.write("tr: last-child{\n")
        file.write("    border-bottom:none;\n")
        file.write("}\n")

        file.write("tr: nth-child(odd) td{\n")
        file.write("    background:#EBEBEB;\n")
        file.write("}\n")

        file.write("tr: nth-child(odd):hover td{\n")
        file.write("    background:#4E5066;\n")
        file.write("}\n")

        file.write("tr: last-child td: first-child{\n")
        file.write("    border-bottom-left-radius:3px;\n")
        file.write("}\n")

        file.write("tr: last-child td: last-child{\n")
        file.write("    border-bottom-right-radius:3px;\n")
        file.write("}\n")

        file.write("td{\n")
        file.write("    background:#FFFFFF;\n")
        file.write("    padding: 20px;\n")
        file.write("    text-align:left;\n")
        file.write("    vertical-align:middle;\n")
        file.write("    font-weight:300;\n")
        file.write("    font-size:18px;\n")
        file.write("    text-shadow: -1px -1px 1px rgba(0, 0, 0, 0.1);\n")
        file.write("    border-right: 1px solid #C1C3D1;\n")
        file.write("}\n")

        file.write("td: last-child{\n")
        file.write("    border-right: 0px;\n")
        file.write("}\n")

        file.write("th.text-left {\n")
        file.write("    text-align: left;\n")
        file.write("}\n")

        file.write("th.text-center {\n")
        file.write("    text-align: center;\n")
        file.write("}\n")

        file.write("th.text-right {\n")
        file.write("    text-align: right;\n")
        file.write("}\n")

        file.write("td.text-left {\n")
        file.write("    text-align: left;\n")
        file.write("}\n")

        file.write("td.text-center {\n")
        file.write("    text-align: center;\n")
        file.write("}\n")

        file.write("td.text-right {\n")
        file.write("    text-align: right;\n")
        file.write("}\n")
        file.write(".encabezado h3{\n")
        file.write("    font-family: arial;\n")
        file.write("    color: #fff;\n")
        file.write("    position: relative;\n")
        file.write("    left: 5 %;\n")
        file.write("    top: 5 %;\n")

        file.write("    text-shadow: 0 1px 1px black;\n")
        file.write("}\n")

        file.write("</Style>\n")
        file.write("</head>\n")

        file.write("<body>\n")

        file.write("<div class=" + "'encabezado'" + ">\n")
        file.write("<h3>Universidad de San Carlos de Guatemala</h3>\n")
        file.write("<h3>Facultad de Ingenieria</h3>\n")
        file.write("<h3>Organizacion De Lenguajes y Compiladores 1</h3>\n")

        file.write("</div>\n")
        file.write("<div class=" + "'table-title'" + ">\n")
        file.write("<h3>Tabla de Errores</h3>\n")
        file.write("</div>\n")
        file.write("<table class=" + "'table-fill'" + ">\n")
        file.write("<thead>\n")
        file.write("<tr>\n")
        file.write("<th class=" + "'text-left'" + ">No.</th>\n")
        file.write("<th class=" + "'text-left'" + ">Token</th>\n")
        file.write("<th class=" + "'text-left'" + ">Error</th>\n")
        file.write("<th class=" + "'text-left'" + ">Fila</th>\n")
        file.write("<th class=" + "'text-left'" + ">Columna</th>\n")

        file.write("</tr>\n")

        file.write("</thead>\n")

        file.write("<tbody class=" + "'table-hover'" + ">")

        if len(self.listaErrores_Css) != 0:
            contador = 1
            for errores in self.listaErrores_Css:
                file.write("<tr>")
                file.write("    <td>{}</td>".format(contador))
                file.write("    <td>{}</td>".format(errores.getTipo()))
                file.write("    <td>{}</td>".format(errores.getAuxlex()))
                file.write("    <td>{}</td>".format(errores.getFila()))
                file.write("    <td>{}</td>".format(errores.getColumna()))
                file.write("</tr>")
                contador += 1

        file.close()

        os.system("start C:/Reportes_Compi/Errores_Lexicos_Css.html")