from enum import Enum

class tokens(Enum):
        Identificador = 1
        Cadena = 2
        Digito = 3
        Signo_Igual = 4
        Numero_Decimal = 5
        Palabra_Reservada = 6
        Comentario_Unilinea = 7
        Signo_por = 8
        PuntoYComa = 9
        Parentesis_Abierto = 10
        Parentesis_Cerrado = 11
        Llave_Abierta = 12
        Llave_Cerrada = 13
        Mayor_que = 14
        Menor_que = 15
        Punto = 16
        Signo_Mas = 17
        Signo_Menos = 18
        Corchete_Abierto = 19
        Corchete_Cerrado = 20
        Coma = 21
        Signo_Division = 22
        Igual = 23
        And = 24
        Or = 25
        Comentario_Multilinea = 26
        Mas_Mas = 27
        Menos_Menos = 28
        Mayor_Igual_Que = 29
        Menor_Igual_Que = 30
        No = 31
        No_Es_Igual = 32
        Igualdad_Estricta = 34
        Desigualdad_Estricta = 35
        Dos_Puntos = 36
        Diagonal_Inversa = 37
        Numeral = 38



class Tokens:

    def __init__(self, tipoDelToken, auxlex, fila, columna, indice):
        self.tipoDelToken = tipoDelToken
        self.auxlex = auxlex
        self.fila = fila
        self.columna = columna
        self.indice = indice

    def getIndice(self):
        return self.indice
    
    def getFila(self):
        return self.fila

    def getColumna(self):
        return self.columna

    def getAuxlex(self):
        return self.auxlex

    def getTipo(self):
        if self.tipoDelToken is tokens.Identificador:
            return "Identificador"
        elif self.tipoDelToken is tokens.Cadena:
            return "Cadena"
        elif self.tipoDelToken is tokens.Digito:
            return "Numero Entero"
        elif self.tipoDelToken is tokens.Signo_Igual:
            return "Signo Igual"
        elif self.tipoDelToken is tokens.Numero_Decimal:
            return "Numero Decimal"
        elif self.tipoDelToken is tokens.Palabra_Reservada:
            return "Palabra Reservada"
        elif self.tipoDelToken is tokens.Comentario_Unilinea:
            return "Comentario Unilinea"
        elif self.tipoDelToken is tokens.Signo_por:
            return "Signo Por"
        elif self.tipoDelToken is tokens.PuntoYComa:
            return "Punto y Coma"
        elif self.tipoDelToken is tokens.Parentesis_Abierto:
            return "Parentesis Abierto"
        elif self.tipoDelToken is tokens.Parentesis_Cerrado:
            return "Parentesis Cerrado"
        elif self.tipoDelToken is tokens.Llave_Abierta:
            return "Llave Abierta"
        elif self.tipoDelToken is tokens.Llave_Cerrada:
            return "Llave Cerrada"
        elif self.tipoDelToken is tokens.Mayor_que:
            return "Mayor Que"
        elif self.tipoDelToken is tokens.Menor_que:
            return "Menor Que"
        elif self.tipoDelToken is tokens.Punto:
            return "Punto"
        elif self.tipoDelToken is tokens.Signo_Mas:
            return "Signo Mas"
        elif self.tipoDelToken is tokens.Signo_Menos:
            return "Signo Menos"
        elif self.tipoDelToken is tokens.Corchete_Abierto:
            return "Corchete Abierto"
        elif self.tipoDelToken is tokens.Corchete_Cerrado:
            return "Corchete Cerrado"
        elif self.tipoDelToken is tokens.Coma:
            return "Coma"
        elif self.tipoDelToken is tokens.Signo_Division:
            return "Signo Divison"
        elif self.tipoDelToken is tokens.Igual:
            return "Igual"
        elif self.tipoDelToken is tokens.And:
            return "And"
        elif self.tipoDelToken is tokens.Or:
            return "Or"
        elif self.tipoDelToken is tokens.Comentario_Multilinea:
            return "Comentario Multilinea"
        elif self.tipoDelToken is tokens.Mas_Mas:
            return "Mas Mas"  
        elif self.tipoDelToken is tokens.Menos_Menos:
            return "Menos Menos"   
        elif self.tipoDelToken is tokens.Mayor_Igual_Que:
            return "Mayor Igual Que"       
        elif self.tipoDelToken is tokens.Menor_Igual_Que:
            return "Menor Igual Que"  
        elif self.tipoDelToken is tokens.No:
            return "No"  
        elif self.tipoDelToken is tokens.No_Es_Igual:
            return "No Es Igual"
        elif self.tipoDelToken is tokens.Igualdad_Estricta:
            return "Igualda Estricta" 
        elif self.tipoDelToken is tokens.Desigualdad_Estricta:
            return "Desigualdad Estricta"
        elif self.tipoDelToken is tokens.Dos_Puntos:
            return "Dos Puntos"
        elif self.tipoDelToken is tokens.Diagonal_Inversa:
            return "Diagonal Inversa"
        elif self.tipoDelToken is tokens.Numeral:
            return "Numeral"
        else:
            return "desconocido"


