from enum import Enum

class ErrorSintactico(Enum):
        desconocido =1

class ErroresSintactico:

    def __init__(self, tipoDelToken, auxlex, fila, columna, indiceError):
        self.tipoDelToken = tipoDelToken
        self.auxlex = auxlex
        self.fila = fila
        self.columna = columna
        self.indiceError = indiceError

    def getIndice(self):
        return self.indiceError
    
    def getFila(self):
        return self.fila

    def getColumna(self):
        return self.columna

    def getAuxlex(self):
        return self.auxlex

    def getTipo(self):
        if self.tipoDelToken is ErrorSintactico.desconocido:
            return "Desconocido"
        else:
            return "desconocido"