from Tokens import tokens, Tokens
from Errores import Errores, Error
from arbol import tokensArbol, TokensArbol
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
        self.sin_errores = ""
        self.lista_arbol = []
    
    def agragarToken(self, tipoDelToken):
        self.lista_de_tokens.append(Tokens(tipoDelToken, self.auxlex, self.fila, self.columna,self.indice))
        self.sin_errores += self.auxlex
        self.auxlex= ""
        self.estado = 0
        self.sin_errores += self.auxlex

    def agragarErrores(self, tipoDelToken):
        self.listaErrores.append(Errores(tipoDelToken, self.auxlex, self.fila, self.columna, self.indiceError))
        self.auxlex= ""
        self.estado = 0

    def agregar_al_arbol(self, tipoDelToken):
        self.lista_arbol.append(TokensArbol(tipoDelToken))

    def analizador(self, entrada):
        cadena = entrada + "#"
        contador = 0
        while contador <= (len(cadena) -1):
            actual = cadena[contador]
            self.columna += 1
            if self.estado == 0:
                if actual.isalpha():
                    self.auxlex += actual
                    self.estado = 1
                elif actual == '_':
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
                    self.sin_errores += actual
                    self.estado = 0
                elif actual == "\t":
                    self.columna += 1
                    self.sin_errores += actual
                    self.estado = 0
                elif actual == " ":
                    self.estado = 0
                    self.sin_errores += actual
                elif actual == '/':
                    self.auxlex += actual
                    self.estado = 7
                elif actual == '*':
                    self.auxlex += actual
                    self.indice +=1
                    self.agragarToken(tokens.Signo_por)
                    self.agregar_al_arbol(tokensArbol.Signo_por)
                elif actual == ';':
                    self.auxlex += actual
                    self.indice +=1
                    self.agragarToken(tokens.PuntoYComa)
                    self.agregar_al_arbol(tokensArbol.PuntoYComa)
                elif actual == ':':
                    self.auxlex += actual
                    self.indice +=1
                    self.agragarToken(tokens.Dos_Puntos)
                    self.agregar_al_arbol(tokensArbol.Dos_Puntos)
                elif actual == "\\":
                    self.auxlex += actual
                    self.indice +=1
                    self.agragarToken(tokens.Diagonal_Inversa)
                    self.agregar_al_arbol(tokensArbol.Diagonal_Inversa)
                elif actual == '(':
                    self.auxlex += actual
                    self.indice +=1
                    self.agragarToken(tokens.Parentesis_Abierto)
                    self.agregar_al_arbol(tokensArbol.Parentesis_Abierto)
                elif actual == ')':
                    self.auxlex += actual
                    self.indice +=1
                    self.agragarToken(tokens.Parentesis_Cerrado)
                    self.agregar_al_arbol(tokensArbol.Parentesis_Cerrado)
                elif actual == '{':
                    self.auxlex += actual
                    self.indice +=1
                    self.agragarToken(tokens.Llave_Abierta)
                    self.agregar_al_arbol(tokensArbol.Llave_Abierta)
                elif actual == '}':
                    self.auxlex += actual
                    self.indice +=1
                    self.agragarToken(tokens.Llave_Cerrada)
                    self.agregar_al_arbol(tokensArbol.Llave_Cerrada)
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
                    self.agregar_al_arbol(tokensArbol.Punto)
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
                    self.agregar_al_arbol(tokensArbol.Corchete_Abierto)
                elif actual == ']':
                    self.auxlex += actual
                    self.indice +=1
                    self.agragarToken(tokens.Corchete_Cerrado)
                    self.agregar_al_arbol(tokensArbol.Corchete_Cerrado)
                elif actual == ',':
                    self.auxlex += actual
                    self.indice +=1
                    self.agragarToken(tokens.Coma)
                    self.agregar_al_arbol(tokensArbol.Coma)
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
                        self.agregar_al_arbol(tokensArbol.Identificador)
                        self.auxlex = ""
                    else:
                        self.columna -= 1
                        self.indice += 1
                        self.agragarToken(tokens.Identificador)
                        self.agregar_al_arbol(tokensArbol.Identificador)
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
                    self.agregar_al_arbol(tokensArbol.Digito)
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
                    self.agregar_al_arbol(tokensArbol.Numero_Decimal)
                    self.auxlex = ""
                    contador -= 1

            elif self.estado == 3:
                if actual != '"':
                    self.estado = 3
                    self.auxlex += actual
                    if actual == "\n":
                        self.columna = 0
                        self.fila += 1
                        self.estado = 3
                else:
                    self.auxlex += actual
                    self.estado = 6

            elif self.estado == 6:
                    self.columna -= 1
                    self.indice += 1
                    self.agragarToken(tokens.Cadena)
                    self.agregar_al_arbol(tokensArbol.Cadena)
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
                    self.agragarToken(tokens.Diagonal)
                    self.agregar_al_arbol(tokensArbol.Diagonal)
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
                    self.agregar_al_arbol(tokensArbol.Comentario_Unilinea)
                    self.sin_errores += self.auxlex
                    self.auxlex = ""
                    self.fila += 1
                    self.columna = 0
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
                elif actual != "*":
                    self.estado = 10
                    self.auxlex += actual
                    if actual == "\n":
                        self.columna = 0
                        self.fila += 1
                        self.estado = 10 
                else:
                    actual == "*" 
                    self.estado = 11
                    self.auxlex += actual

            elif self.estado == 12:
                    print("------->"+ self.auxlex)
                    self.agregar_al_arbol(tokensArbol.Comentario_Multilinea)
                    self.sin_errores += self.auxlex
                    self.auxlex = ""
                    self.columna -= 1
                    self.estado = 0
                    contador -= 1

            elif self.estado == 13:
                if actual == "+":
                    self.estado = 14
                    self.auxlex += actual
                else: 
                    self.columna -= 1
                    self.indice += 1
                    self.agragarToken(tokens.Signo_Mas)
                    self.agregar_al_arbol(tokensArbol.Signo_Mas)
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
                    self.agregar_al_arbol(tokensArbol.Signo_Menos)
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
                    self.agregar_al_arbol(tokensArbol.Mayor_que)
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
                    self.agregar_al_arbol(tokensArbol.Menor_que)
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
                    self.agregar_al_arbol(tokensArbol.Signo_Igual)
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
                    self.agregar_al_arbol(tokensArbol.And)
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
                    self.agregar_al_arbol(tokensArbol.Or)
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
                    self.agragarToken(tokens.Caracter)
                    self.agregar_al_arbol(tokensArbol.Caracter)
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

    def imprimirListaTokensArbol(self):
        for token in self.lista_arbol:
            print("------------------------------------------------------------------------------------")
            print('Token = {}'.format(token.getTipo()))
            print("------------------------------------------------------------------------------------")

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
        ruta = re.search(patron, self.sin_errores)
        ruta = ruta.group()

        ruta = re.sub(r'[a-zA-Z]:\\','',ruta)
        ruta = ruta.replace("user\\","")
        pathlib.Path(ruta).mkdir(parents=True, exist_ok=True)

        file = open(".\\" + ruta + nombre_archivo, "w")
        file.write(self.sin_errores)
        file.close()

        self.variables = re.findall(r'var [a-zA-Z_][a-zA-Z0-9_]*',self.sin_errores)
        for i in range(0,len(self.variables)):
            self.variables[i] = self.variables[i].replace("var ","")

    def generarArbol(self):
        file = open ("C:/Reportes_Compi/Grafo.dot", "w")
        file.write("digraph G{ \n")
        file.write("node[style="+"filled,"+"fillcolor="+"yellow,"+"shape="+"circle"+"] \n")
        file.write("node0[label="+"S0"+"] \n")
        contador = 1
        verificando_identificador = True
        verificando_digito = True
        verificando_decimal = True
        verificando_cadena = True
        verificando_Signo_Igual = True
        verificando_Diagonal = True
        verificando_por = True
        verificando_puntoycoma = True
        verificando_dos_puntos = True
        verificando_diagonal_inversa = True
        verificando_parentesis_abierto = True
        verificando_parentesis_cerrado = True
        verificando_llave_abierta = True
        verificando_llave_cerrada = True
        verificando_mayor_que = True
        verificando_menor_que = True
        verificando_punto = True
        verificando_signo_mas = True
        verificando_signo_menos = True
        verificando_corchete_abierto = True
        verificando_corchete_cerrado = True
        verificando_coma = True
        verificando_and = True
        verificando_or = True
        verificando_caracter = True
        verificando_comentario_unilinea = True
        verificando_comentario_multilinea = True
        for recorrido in self.lista_arbol:
            #while verificando:
                if recorrido.getTipo() == "Identificador":
                    while verificando_identificador:
                        file.write("    node{0}[shape=\"doublecircle\", label=\"S{0} Identificador\"];\n".format(contador))
                        file.write("    node0->node{}[label=\"{}\"];\n".format(contador,"letra | _"))
                        file.write("    node{0}->node{0}[label=\"{1}\"];\n".format(contador,"letra | _ | digito"))
                        verificando_identificador = False
                    #file.write("    node", contador , "[shape="+"doublecircule,"+"label= S", contador ," Identificador]; \n")
                    #file.write("    node1->node" , contador , "[label =","Letra| -" ,"]; \n")
                    #file.write("    node",contador,"->node",contador, "[label =","Letra| - | Digito" ,"]; \n")
                elif recorrido.getTipo() == "Numero Entero":
                    while verificando_digito:
                        file.write("    node{0}[shape=\"doublecircle\", label=\"S{0} - Numero Entero\"];\n".format(contador))
                        file.write("    node0->node{}[label=\"{}\"];\n".format(contador,"digito"))
                        file.write("    node{0}->node{0}[label=\"{1}\"];\n".format(contador,"digito"))
                        verificando_digito = False
                elif recorrido.getTipo() == "Numero Decimal":
                    while verificando_decimal:
                        file.write("    node{0}[label=\"{0}\"];\n".format(contador))
                        file.write("    node0->node{}[label=\"{}\"];\n".format(contador,"digito"))
                        file.write("    node{0}->node{0}[label=\"{1}\"];\n".format(contador,"digito"))
                        contador += 1
                        file.write("    node{0}[label=\"{0}\"];\n".format(contador))
                        file.write("    node{}->node{}[label=\"{}\"];\n".format(contador-1,contador,"punto"))
                        contador += 1
                        file.write("    node{0}[shape=\"doublecircle\", label=\"{0} - Numero Decimal\"];\n".format(contador))
                        file.write("    node{}->node{}[label=\"{}\"];\n".format(contador-1,contador,"digito"))
                        file.write("    node{0}->node{0}[label=\"{1}\"];\n".format(contador,"digito"))
                        verificando_decimal = False
                elif recorrido.getTipo() == "Cadena":
                    while verificando_cadena:
                        file.write("    node{0}[label=\"{0}\"];\n".format(contador))
                        file.write("    node0->node{}[label=\"{}\"];\n".format(contador,"\\\""))
                        file.write("    node{0}->node{0}[label=\"{1}\"];\n".format(contador,"Caracter"))
                        contador += 1
                        file.write("    node{0}[shape=\"doublecircle\", label=\"{0} - Cadena\"];\n".format(contador))
                        file.write("    node{}->node{}[label=\"{}\"];\n".format(contador-1,contador,"\\\""))
                        verificando_cadena = False
                elif recorrido.getTipo() == "Signo Igual":
                    while verificando_Signo_Igual:
                        file.write("    node{0}[shape=\"doublecircle\", label=\"S{0} - Signo Igual\"];\n".format(contador))
                        file.write("    node0->node{}[label=\"{}\"];\n".format(contador,"="))
                        verificando_Signo_Igual = False
                elif recorrido.getTipo() == "Diagonal":
                    while verificando_Diagonal:
                        file.write("    node{0}[shape=\"doublecircle\", label=\"S{0} - Diagonal\"];\n".format(contador))
                        file.write("    node0->node{}[label=\"{}\"];\n".format(contador,"/"))
                        verificando_Diagonal = False
                elif recorrido.getTipo() == "Signo Por":
                    while verificando_por:
                        file.write("    node{0}[shape=\"doublecircle\", label=\"S{0} - Signo Por\"];\n".format(contador))
                        file.write("    node0->node{}[label=\"{}\"];\n".format(contador,"*"))
                        verificando_por = False
                elif recorrido.getTipo() == "Punto y Coma":
                    while verificando_puntoycoma:
                        file.write("    node{0}[shape=\"doublecircle\", label=\"S{0} - Punto y Coma\"];\n".format(contador))
                        file.write("    node0->node{}[label=\"{}\"];\n".format(contador,";"))
                        verificando_puntoycoma = False
                elif recorrido.getTipo() == "Dos Puntos":
                    while verificando_dos_puntos:
                        file.write("    node{0}[shape=\"doublecircle\", label=\"S{0} - Dos Puntos\"];\n".format(contador))
                        file.write("    node0->node{}[label=\"{}\"];\n".format(contador,":"))
                        verificando_dos_puntos = False
                elif recorrido.getTipo() == "Diagonal Inversa":
                    while verificando_diagonal_inversa:
                        file.write("    node{0}[shape=\"doublecircle\", label=\"S{0} - Diagonal Inversa\"];\n".format(contador))
                        file.write("    node0->node{}[label=\"{}\"];\n".format(contador,"diagonal Inversa"))
                        verificando_diagonal_inversa = False
                elif recorrido.getTipo() == "Parentesis Abierto":
                    while verificando_parentesis_abierto:
                        file.write("    node{0}[shape=\"doublecircle\", label=\"S{0} - Parentesis Abierto\"];\n".format(contador))
                        file.write("    node0->node{}[label=\"{}\"];\n".format(contador,"("))
                        verificando_parentesis_abierto = False
                elif recorrido.getTipo() == "Parentesis Cerrado":
                    while verificando_parentesis_cerrado:
                        file.write("    node{0}[shape=\"doublecircle\", label=\"S{0} - Parentesis Cerrado\"];\n".format(contador))
                        file.write("    node0->node{}[label=\"{}\"];\n".format(contador,")"))
                        verificando_parentesis_cerrado = False
                elif recorrido.getTipo() == "Llave Abierta":
                    while verificando_llave_abierta:
                        file.write("    node{0}[shape=\"doublecircle\", label=\"S{0} - Llave Abierta\"];\n".format(contador))
                        file.write("    node0->node{}[label=\"{}\"];\n".format(contador,"{"))
                        verificando_llave_abierta = False
                elif recorrido.getTipo() == "Llave Cerrada":
                    while verificando_llave_cerrada:
                        file.write("    node{0}[shape=\"doublecircle\", label=\"S{0} - Llave Cerrada\"];\n".format(contador))
                        file.write("    node0->node{}[label=\"{}\"];\n".format(contador,"}"))
                        verificando_llave_cerrada = False
                elif recorrido.getTipo() == "Mayor Que":
                    while verificando_mayor_que:
                        file.write("    node{0}[shape=\"doublecircle\", label=\"S{0} - Mayor que\"];\n".format(contador))
                        file.write("    node0->node{}[label=\"{}\"];\n".format(contador,">"))
                        verificando_mayor_que = False
                elif recorrido.getTipo() == "Menor Que":
                    while verificando_menor_que:
                        file.write("    node{0}[shape=\"doublecircle\", label=\"S{0} - Menor que\"];\n".format(contador))
                        file.write("    node0->node{}[label=\"{}\"];\n".format(contador,"<"))
                        verificando_menor_que = False
                elif recorrido.getTipo() == "Punto":
                    while verificando_punto:
                        file.write("    node{0}[shape=\"doublecircle\", label=\"S{0} - Punto\"];\n".format(contador))
                        file.write("    node0->node{}[label=\"{}\"];\n".format(contador,"Punto"))
                        verificando_punto = False
                elif recorrido.getTipo() == "Signo Mas":
                    while verificando_signo_mas:
                        file.write("    node{0}[shape=\"doublecircle\", label=\"S{0} - Signo Mas\"];\n".format(contador))
                        file.write("    node0->node{}[label=\"{}\"];\n".format(contador,"+"))
                        verificando_signo_mas = False
                elif recorrido.getTipo() == "Signo Menos":
                    while verificando_signo_menos:
                        file.write("    node{0}[shape=\"doublecircle\", label=\"S{0} - Signo Menos\"];\n".format(contador))
                        file.write("    node0->node{}[label=\"{}\"];\n".format(contador,"-"))
                        verificando_signo_menos = False
                elif recorrido.getTipo() == "Corchete Abierto":
                    while verificando_corchete_abierto:
                        file.write("    node{0}[shape=\"doublecircle\", label=\"S{0} - Corchete Abierto\"];\n".format(contador))
                        file.write("    node0->node{}[label=\"{}\"];\n".format(contador,"["))
                        verificando_corchete_abierto = False
                elif recorrido.getTipo() == "Corchete Cerrado":
                    while verificando_corchete_cerrado:
                        file.write("    node{0}[shape=\"doublecircle\", label=\"S{0} - Corchete Cerrado\"];\n".format(contador))
                        file.write("    node0->node{}[label=\"{}\"];\n".format(contador,"]"))
                        verificando_corchete_cerrado = False
                elif recorrido.getTipo() == "Coma":
                    while verificando_coma:
                        file.write("    node{0}[shape=\"doublecircle\", label=\"S{0} - Coma\"];\n".format(contador))
                        file.write("    node0->node{}[label=\"{}\"];\n".format(contador,","))
                        verificando_coma = False
                elif recorrido.getTipo() == "And":
                    while verificando_and:
                        file.write("    node{0}[label=\"{0}\"];\n".format(contador))
                        file.write("    node0->node{}[label=\"{}\"];\n".format(contador,"&"))
                        contador += 1
                        file.write("    node{0}[shape=\"doublecircle\", label=\"{0} - And\"];\n".format(contador))
                        file.write("    node{}->node{}[label=\"{}\"];\n".format(contador-1,contador,"&"))
                        verificando_and = False
                elif recorrido.getTipo() == "Or":
                    while verificando_or:
                        file.write("    node{0}[label=\"{0}\"];\n".format(contador))
                        file.write("    node0->node{}[label=\"{}\"];\n".format(contador,"|"))
                        contador += 1
                        file.write("    node{0}[shape=\"doublecircle\", label=\"{0} - And\"];\n".format(contador))
                        file.write("    node{}->node{}[label=\"{}\"];\n".format(contador-1,contador,"|"))
                        verificando_or = False
                elif recorrido.getTipo() == "Caracter":
                    while verificando_caracter:
                        file.write("    node{0}[label=\"{0}\"];\n".format(contador))
                        file.write("    node0->node{}[label=\"{}\"];\n".format(contador,"\\\'"))
                        file.write("    node{0}->node{0}[label=\"{1}\"];\n".format(contador,"Caracter"))
                        contador += 1
                        file.write("    node{0}[shape=\"doublecircle\", label=\"{0} - Caracter\"];\n".format(contador))
                        file.write("    node{}->node{}[label=\"{}\"];\n".format(contador-1,contador,"\\\'"))
                        verificando_caracter = False
                elif recorrido.getTipo() == "Comentario Unilinea":
                    while verificando_comentario_unilinea:
                        file.write("    node{0}[label=\"{0}\"];\n".format(contador))
                        file.write("    node0->node{}[label=\"{}\"];\n".format(contador,"/"))
                        contador += 1
                        file.write("    node{0}[shape=\"doublecircle\", label=\"{0} - Comentario Unilinea\"];\n".format(contador))
                        file.write("    node{}->node{}[label=\"{}\"];\n".format(contador-1,contador,"/"))
                        file.write("    node{0}->node{0}[label=\"{1}\"];\n".format(contador,"Caracter"))
                        verificando_comentario_unilinea = False
                elif recorrido.getTipo() == "Comentario Multilinea":
                    while verificando_comentario_multilinea:
                        file.write("    node{0}[label=\"{0}\"];\n".format(contador))
                        file.write("    node0->node{}[label=\"{}\"];\n".format(contador,"/"))
                        contador += 1
                        file.write("    node{0}[label=\"{0}\"];\n".format(contador))
                        file.write("    node{}->node{}[label=\"{}\"];\n".format(contador-1,contador,"*"))
                        file.write("    node{0}->node{0}[label=\"{1}\"];\n".format(contador,"Caracter"))
                        contador += 1
                        file.write("    node{0}[label=\"{0}\"];\n".format(contador))
                        file.write("    node{}->node{}[label=\"{}\"];\n".format(contador-1,contador,"*"))
                        contador += 1
                        file.write("    node{0}[shape=\"doublecircle\", label=\"{0} - Comentario Multulinea\"];\n".format(contador))
                        file.write("    node{}->node{}[label=\"{}\"];\n".format(contador-1,contador,"/"))
                        verificando_comentario_multilinea = False
                #else:
                #else:
                    #file.write("    node{0}[shape=\"doublecircle\", label=\"{0}\"];\n".format(contador))
                    #file.write("    node0->node{}[label=\"{}\"];\n".format(contador,recorrido))
                    #file.write("    node"+contador+"[shape="+"doublecircle,"+ "label="+contador+"];\n")
                    #file.write("    node1->node"+contador+"[label="+contador+"];\n")
                contador += 1
        file.write("}")
        file.close()

        os.system("dot -Tpng C:/Reportes_Compi/Grafo.dot -o C:/Reportes_Compi/Grafo.png")
        os.system("start C:/Reportes_Compi/Grafo.png")






                    

    

