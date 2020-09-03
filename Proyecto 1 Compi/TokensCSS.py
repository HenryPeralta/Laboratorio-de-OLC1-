from enum import Enum

class tokensCss(Enum):
    Identificador = 1
    Comentario_Unilinea = 2
    Comentario_Multilinea = 3
    Cadena = 4

class TokensCss:

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
        if self.tipoDelToken is tokensCss.Identificador:
            return "Identificador"
        elif self.tipoDelToken is tokensCss.Comentario_Unilinea:
            return "Comentario Unilinea"
        elif self.tipoDelToken is tokensCss.Comentario_Multilinea:
            return "Comentario Multilinea"
        elif self.tipoDelToken is tokensCss.Cadena:
            return "Cadena"
        else:
            return "desconocido"        