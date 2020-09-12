from Tokens import tokens, Tokens
from Errores import Errores, Error
import os
import re
import pathlib

class AnalizadorLexico:

    def __init__(self):
        self.lista_de_tokens = []
        self.listaErrores = []
        self.estado = 0
        self.auxlex = ""
        self.columna = 0
        self.fila = 1
        self.indice = 0
        self.indiceError = 0
        self.palabrasreservadas = ["var", "for", "while", "if", "else", "do", "continue", "break", "return", "function", "constructor", "class", "Math.pow", "true", "false"]
        self.guardarcomentario = ""
    
    def agragarToken(self, tipoDelToken):
        self.lista_de_tokens.append(Tokens(tipoDelToken, self.auxlex, self.fila, self.columna,self.indice))
        self.guardarcomentario += self.auxlex
        self.auxlex= ""
        self.estado = 0
        self.guardarcomentario += self.auxlex

    def agragarErrores(self, tipoDelToken):
        self.listaErrores.append(Errores(tipoDelToken, self.auxlex, self.fila, self.columna, self.indiceError))
        self.auxlex= ""
        self.estado = 0

    def analizador(self, entrada):
        cadena = entrada + "#"
        contador = 0
        while contador < len(cadena):
            actual = cadena[contador]
            self.columna += 1
            if self.estado == 0:
                if actual.isalpha():
                    self.auxlex += actual
                    self.estado = 1
                elif actual.isdigit():
                    self.auxlex += actual
                    self.estado = 2
                elif actual == '"':
                    self.auxlex += actual
                    self.estado = 3
                elif actual == '=':
                    self.auxlex += actual
                    self.estado = 21
                elif actual == "\n":
                    self.columna = 0
                    self.fila += 1
                    self.guardarcomentario += actual
                    self.estado = 0
                elif actual == "\t":
                    self.columna += 1
                    self.estado = 0
                    self.guardarcomentario += actual
                elif actual == " ":
                    self.estado = 0
                    self.guardarcomentario += actual
                elif actual == '/':
                    self.auxlex += actual
                    self.estado = 7
                elif actual == '*':
                    self.auxlex += actual
                    self.indice +=1
                    self.agragarToken(tokens.Signo_por)
                elif actual == ';':
                    self.auxlex += actual
                    self.indice +=1
                    self.agragarToken(tokens.PuntoYComa)
                elif actual == ':':
                    self.auxlex += actual
                    self.indice +=1
                    self.agragarToken(tokens.Dos_Puntos)
                elif actual == "\\":
                    self.auxlex += actual
                    self.indice +=1
                    self.agragarToken(tokens.Diagonal_Inversa)
                elif actual == '(':
                    self.auxlex += actual
                    self.indice +=1
                    self.agragarToken(tokens.Parentesis_Abierto)
                elif actual == ')':
                    self.auxlex += actual
                    self.indice +=1
                    self.agragarToken(tokens.Parentesis_Cerrado)
                elif actual == '{':
                    self.auxlex += actual
                    self.indice +=1
                    self.agragarToken(tokens.Llave_Abierta)
                elif actual == '}':
                    self.auxlex += actual
                    self.indice +=1
                    self.agragarToken(tokens.Llave_Cerrada)
                elif actual == '>':
                    self.auxlex += actual
                    self.estado = 17
                elif actual == '<':
                    self.auxlex += actual
                    self.estado = 19
                elif actual == '.':
                    self.auxlex += actual
                    self.indice +=1
                    self.agragarToken(tokens.Punto)
                elif actual == '+':
                    self.auxlex += actual
                    self.estado = 13
                elif actual == '-':
                    self.auxlex += actual
                    self.estado = 15
                elif actual == '[':
                    self.auxlex += actual
                    self.indice +=1
                    self.agragarToken(tokens.Corchete_Abierto)
                elif actual == ']':
                    self.auxlex += actual
                    self.indice +=1
                    self.agragarToken(tokens.Corchete_Cerrado)
                elif actual == ',':
                    self.auxlex += actual
                    self.indice +=1
                    self.agragarToken(tokens.Coma)
                elif actual == '&':
                    self.auxlex += actual
                    self.estado = 23
                elif actual == '|':
                    self.auxlex += actual
                    self.estado = 25
                elif actual == '!':
                    self.auxlex += actual
                    self.estado = 27
                elif actual == "'":
                    self.auxlex += actual
                    self.estado = 31
                    
                else:
                    if actual == '#' and contador == (len(cadena) - 1):
                        print("-------Fin del Analisis Lexico-------")
                    else:
                        self.auxlex += actual
                        self.estado = -99

            elif self.estado == 1:
                if actual.isalpha() or actual.isdigit() or actual == "_":
                    self.estado = 1
                    self.auxlex += actual
                else:
                    if self.auxlex in self.palabrasreservadas:
                        self.columna -= 1
                        self.indice += 1
                        self.agragarToken(tokens.Palabra_Reservada)
                        self.auxlex = ""
                    else:
                        self.columna -= 1
                        self.indice += 1
                        self.agragarToken(tokens.Identificador)
                        self.auxlex = ""
                    contador -= 1

            elif self.estado == 2:
                if actual.isdigit():
                    self.estado = 2
                    self.auxlex += actual
                elif actual == ".":
                    self.auxlex += actual
                    self.estado = 4
                else: 
                    self.columna -= 1
                    self.indice += 1
                    self.agragarToken(tokens.Digito)
                    self.auxlex = ""
                    contador -= 1

            elif self.estado == 4:
                if actual.isdigit():
                    self.estado = 5
                    self.auxlex += actual
                elif actual == "\n":
                    self.columna = 0
                    self.fila += 1
                    self.estado = -99
                else:
                    self.auxlex += actual
                    self.estado = -99

            elif self.estado == 5:
                if actual.isdigit():
                    self.estado = 5
                    self.auxlex += actual
                else:
                    self.columna -= 1
                    self.indice += 1
                    self.agragarToken(tokens.Numero_Decimal)
                    self.auxlex = ""
                    contador -= 1

            elif self.estado == 3:
                if actual != '"':
                    self.estado = 3
                    self.auxlex += actual
                else:
                    self.auxlex += actual
                    self.estado = 6

            elif self.estado == 6:
                    self.columna -= 1
                    self.indice += 1
                    self.agragarToken(tokens.Cadena)
                    self.auxlex = ""
                    contador -= 1

            elif self.estado == 7:
                if actual == "/":
                    self.estado = 8
                    self.auxlex += actual
                elif actual == "*":
                    self.auxlex += actual
                    self.estado = 10
                else: 
                    self.columna -= 1
                    self.indice += 1
                    self.agragarToken(tokens.Signo_Division)
                    self.auxlex = ""
                    contador -= 1

            elif self.estado == 8:
                if actual != "\n":
                    self.estado = 8
                    self.auxlex += actual
                else: 
                    self.auxlex += actual
                    self.estado = 9

            elif self.estado == 9:
                    print("------->"+ self.auxlex)
                    self.guardarcomentario += self.auxlex
                    self.auxlex = ""
                    self.estado = 0
                    contador -= 1

            elif self.estado == 10:
                if actual != "*":
                    self.estado = 10
                    self.auxlex += actual
                    if actual == "\n":
                        self.columna = 0
                        self.fila += 1
                        self.estado = 10
                else: 
                    self.auxlex += actual
                    self.estado = 11

            elif self.estado == 11:
                if actual == "/":
                    self.estado = 12
                    self.auxlex += actual
                else:
                    actual == "*" 
                    self.estado = 10
                    self.auxlex += actual

            elif self.estado == 12:
                    self.columna -= 1
                    self.indice += 1
                    self.agragarToken(tokens.Comentario_Multilinea)
                    self.auxlex = ""
                    contador -= 1

            elif self.estado == 13:
                if actual == "+":
                    self.estado = 14
                    self.auxlex += actual
                else: 
                    self.columna -= 1
                    self.indice += 1
                    self.agragarToken(tokens.Signo_Mas)
                    self.auxlex = ""
                    contador -= 1

            elif self.estado == 14:
                    self.columna -= 1
                    self.indice += 1
                    self.agragarToken(tokens.Mas_Mas)
                    self.auxlex = ""
                    contador -= 1

            elif self.estado == 15:
                if actual == "-":
                    self.estado = 16
                    self.auxlex += actual
                else: 
                    self.columna -= 1
                    self.indice += 1
                    self.agragarToken(tokens.Signo_Menos)
                    self.auxlex = ""
                    contador -= 1

            elif self.estado == 16:
                    self.columna -= 1
                    self.indice += 1
                    self.agragarToken(tokens.Menos_Menos)
                    self.auxlex = ""
                    contador -= 1

            elif self.estado == 17:
                if actual == "=":
                    self.estado = 18
                    self.auxlex += actual
                else: 
                    self.columna -= 1
                    self.indice += 1
                    self.agragarToken(tokens.Mayor_que)
                    self.auxlex = ""
                    contador -= 1

            elif self.estado == 18:
                    self.columna -= 1
                    self.indice += 1
                    self.agragarToken(tokens.Mayor_Igual_Que)
                    self.auxlex = ""
                    contador -= 1

            elif self.estado == 19:
                if actual == "=":
                    self.estado = 20
                    self.auxlex += actual
                else: 
                    self.columna -= 1
                    self.indice += 1
                    self.agragarToken(tokens.Menor_que)
                    self.auxlex = ""
                    contador -= 1

            elif self.estado == 20:
                    self.columna -= 1
                    self.indice += 1
                    self.agragarToken(tokens.Menor_Igual_Que)
                    self.auxlex = ""
                    contador -= 1

            elif self.estado == 21:
                if actual == "=":
                    self.estado = 22
                    self.auxlex += actual
                else: 
                    self.columna -= 1
                    self.indice += 1
                    self.agragarToken(tokens.Signo_Igual)
                    self.auxlex = ""
                    contador -= 1

            elif self.estado == 22:
                if actual == "=":
                    self.estado = 29
                    self.auxlex += actual
                else:
                    self.columna -= 1
                    self.indice += 1
                    self.agragarToken(tokens.Igual)
                    self.auxlex = ""
                    contador -= 1

            elif self.estado == 23:
                if actual == "&":
                    self.estado = 24
                    self.auxlex += actual
                elif actual == "\n":
                    self.columna = 0
                    self.fila += 1
                    self.estado = -99
                else: 
                    self.auxlex += actual
                    self.estado = -99

            elif self.estado == 24:
                    self.columna -= 1
                    self.indice += 1
                    self.agragarToken(tokens.And)
                    self.auxlex = ""
                    contador -= 1

            elif self.estado == 25:
                if actual == "|":
                    self.estado = 26
                    self.auxlex += actual
                elif actual == "\n":
                    self.columna = 0
                    self.fila += 1
                    self.estado = -99
                else: 
                    self.auxlex += actual
                    self.estado = -99

            elif self.estado == 26:
                    self.columna -= 1
                    self.indice += 1
                    self.agragarToken(tokens.Or)
                    self.auxlex = ""
                    contador -= 1

            elif self.estado == 27:
                if actual == "=":
                    self.estado = 28
                    self.auxlex += actual
                else: 
                    self.columna -= 1
                    self.indice += 1
                    self.agragarToken(tokens.No)
                    self.auxlex = ""
                    contador -= 1

            elif self.estado == 28:
                if actual == "=":
                    self.estado = 30
                    self.auxlex += actual
                else: 
                    self.columna -= 1
                    self.indice += 1
                    self.agragarToken(tokens.No_Es_Igual)
                    self.auxlex = ""
                    contador -= 1

            elif self.estado == 29:
                    self.columna -= 1
                    self.indice += 1
                    self.agragarToken(tokens.Igualdad_Estricta)
                    self.auxlex = ""
                    contador -= 1

            elif self.estado == 30:
                    self.columna -= 1
                    self.indice += 1
                    self.agragarToken(tokens.Desigualdad_Estricta)
                    self.auxlex = ""
                    contador -= 1

            elif self.estado == 31:
                if actual != "'":
                    self.estado = 31
                    self.auxlex += actual
                else:
                    self.auxlex += actual
                    self.estado = 32

            elif self.estado == 32:
                    self.columna -= 1
                    self.indice += 1
                    self.agragarToken(tokens.Cadena)
                    self.auxlex = ""
                    contador -= 1
                    
            elif self.estado == -99:
                self.columna -=1
                self.indiceError += 1
                self.agragarErrores(Error.desconocido)
                self.auxlex = ""
                contador -= 1


            contador += 1

    def analizarArchivo(self, ruta):  
        if os.path.isfile(ruta):
            archivo = open(ruta, "r")
            self.analizador(archivo.read())
            archivo.close()

    def imprimirListaTokens(self):
        for token in self.lista_de_tokens:
            print("------------------------------------------------------------------------------------")
            print('Indice = {}    Token = {}    Lexema = {}    Fila = {}    Columna = {}'.format(token.getIndice(), token.getTipo(), token.getAuxlex(), token.getFila(), token.getColumna()))
            print("------------------------------------------------------------------------------------")

    def imprimirListaErrores(self):
        for error in self.listaErrores:
            print("************************************************************************************")
            print('TOKEN => {}     LEXEMA => {}     FILA => {}     COLUMNA => {}     INDICE => {}'.format(error.getTipo(), error.getAuxlex(), error.getFila(), error.getColumna(), error.getIndice()))
            print("************************************************************************************")

    def imprimirLista(self):
        for token in self.lista_de_tokens:
            print(token.getAuxlex())

    def generarHtml(self):
        file = open ("C:/Reportes_Compi/Lista_Tokens.html", "w")
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

        if len(self.lista_de_tokens) != 0:
            contador = 1
            for token in self.lista_de_tokens:
                file.write("<tr>")
                file.write("    <td>{}</td>".format(contador))
                file.write("    <td>{}</td>".format(token.getTipo()))
                file.write("    <td>{}</td>".format(token.getAuxlex()))
                file.write("    <td>{}</td>".format(token.getFila()))
                file.write("    <td>{}</td>".format(token.getColumna()))
                file.write("</tr>")
                contador += 1

        file.close()

        os.system("start C:/Reportes_Compi/Lista_Tokens.html")

    def generarErrores(self):
        file = open ("C:/Reportes_Compi/Errores_Lexicos.html", "w")
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

        if len(self.listaErrores) != 0:
            contador = 1
            for errores in self.listaErrores:
                file.write("<tr>")
                file.write("    <td>{}</td>".format(contador))
                file.write("    <td>{}</td>".format(errores.getTipo()))
                file.write("    <td>{}</td>".format(errores.getAuxlex()))
                file.write("    <td>{}</td>".format(errores.getFila()))
                file.write("    <td>{}</td>".format(errores.getColumna()))
                file.write("</tr>")
                contador += 1

        file.close()

        os.system("start C:/Reportes_Compi/Errores_Lexicos.html")

    def crearArchivoLimpio(self, nombre_archivo):
        patron = r'([a-zA-Z]:\\)(\w+\\)+'
        ruta = re.search(patron, self.guardarcomentario)
        ruta = ruta.group()

        ruta = re.sub(r'[a-zA-Z]:\\','',ruta)
        ruta = ruta.replace("user\\","")
        pathlib.Path(ruta).mkdir(parents=True, exist_ok=True)

        file = open(".\\" + ruta + nombre_archivo, "w")
        file.write(self.guardarcomentario)
        file.close()

        self.variables = re.findall(r'var [a-zA-Z_][a-zA-Z0-9_]*',self.guardarcomentario)
        for i in range(0,len(self.variables)):
            self.variables[i] = self.variables[i].replace("var ","")





                    

    

