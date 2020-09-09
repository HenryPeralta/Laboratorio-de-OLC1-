from enum import Enum

class tokensCss(Enum):
    Identificador = 1
    Comentario_Unilinea = 2
    Comentario_Multilinea = 3
    Signo_Division = 4
    Cadena = 5
    Propiedad = 6
    Signo_Por = 7
    Numeral = 8
    Punto = 9
    Digito = 10
    Numero_Decimal = 11
    Dos_Puntos = 12
    Llave_Abierta = 13
    Llave_Cerrada = 14
    PuntoYComa = 15
    Guion = 16
    Unidades_De_Medida = 17
    Porcentaje = 18
    Hexadecimal = 19
    Parentesis_Abierto = 20
    Parentesis_Cerrado = 21
    Coma = 22 

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
        elif self.tipoDelToken is tokensCss.Signo_Division:
            return "Signo Division"
        elif self.tipoDelToken is tokensCss.Propiedad:
            return "Propiedad"
        elif self.tipoDelToken is tokensCss.Signo_Por:
            return "Signo Por"
        elif self.tipoDelToken is tokensCss.Numeral:
            return "Numeral"  
        elif self.tipoDelToken is tokensCss.Punto:
            return "Punto"   
        elif self.tipoDelToken is tokensCss.Digito:
            return "Digito"
        elif self.tipoDelToken is tokensCss.Numero_Decimal:
            return "Numero Decimal"  
        elif self.tipoDelToken is tokensCss.Dos_Puntos:
            return "Dos Puntos" 
        elif self.tipoDelToken is tokensCss.Llave_Abierta:
            return "Llave Abierta"
        elif self.tipoDelToken is tokensCss.Llave_Cerrada:
            return "Llave Cerrada" 
        elif self.tipoDelToken is tokensCss.PuntoYComa:
            return "Punto y Coma" 
        elif self.tipoDelToken is tokensCss.Guion:
            return "Guion" 
        elif self.tipoDelToken is tokensCss.Unidades_De_Medida:
            return "Unidad De Medida"     
        elif self.tipoDelToken is tokensCss.Porcentaje:
            return "Porcentaje"  
        elif self.tipoDelToken is tokensCss.Hexadecimal:
            return "Hexadecimal" 
        elif self.tipoDelToken is tokensCss.Parentesis_Abierto:
            return "Parentesis Abierto"
        elif self.tipoDelToken is tokensCss.Parentesis_Cerrado:
            return "Parentesis Cerrado"
        elif self.tipoDelToken is tokensCss.Coma:
            return "Coma"                  
        else:
            return "desconocido"        