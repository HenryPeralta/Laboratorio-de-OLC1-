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
        self.sin_errores = ""
    
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