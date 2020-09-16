from enum import Enum

class tokensSintactico(Enum):
    Numero_Entero = 1
    Variable = 2
    Signo_Mas = 3
    Signo_Menos = 4
    Signo_Por = 5
    Signo_Division = 6
    Parentesis_Abierto = 7
    Parentesis_Cerrado = 8
    Numero_Decimal = 9

class TokensSintactico:

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
        if self.tipoDelToken is tokensSintactico.Numero_Entero:
            return "Numero Entero"  
        elif self.tipoDelToken is tokensSintactico.Variable:
            return "Variable"
        elif self.tipoDelToken is tokensSintactico.Signo_Mas:
            return "Signo Mas"
        elif self.tipoDelToken is tokensSintactico.Signo_Menos:
            return "Signo Menos"
        elif self.tipoDelToken is tokensSintactico.Signo_Por:
            return "Signo Por"
        elif self.tipoDelToken is tokensSintactico.Signo_Division:
            return "Signo Division"
        elif self.tipoDelToken is tokensSintactico.Parentesis_Abierto:
            return "Parentesis Abierto"
        elif self.tipoDelToken is tokensSintactico.Parentesis_Cerrado:
            return "Parentesis Cerrado" 
        elif self.tipoDelToken is tokensSintactico.Numero_Decimal:
            return "Numero Decimal"                             
        else:
            return "desconocido" 