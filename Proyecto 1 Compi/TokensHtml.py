from enum import Enum

class tokensHtml(Enum):
    Identificador = 1
    Digito = 2
    Cadena = 3
    Palabras_Reservada = 4
    Titulos = 5
    Etiquetas = 6
    Numero_Decimal = 7
    Parrafo = 8
    Hipervinculo = 9
    Propiedades = 10
    Unidades_de_Medida = 11
    Lista = 12
    Mayor_Que = 13
    Menor_Que = 14
    Diagonal = 15
    Punto = 16
    Igual = 17
    Parentesis_Abierto = 18
    Parentesis_Cerrado = 19


class TokensHtml:

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
        if self.tipoDelToken is tokensHtml.Identificador:
            return "Identificador" 
        elif self.tipoDelToken is tokensHtml.Digito:
            return "Digito"
        elif self.tipoDelToken is tokensHtml.Cadena:
            return "Cadena"
        elif self.tipoDelToken is tokensHtml.Palabras_Reservada:
            return "Palabra Reservada"  
        elif self.tipoDelToken is tokensHtml.Titulos:
            return "Titulos"  
        elif self.tipoDelToken is tokensHtml.Etiquetas:
            return "Etiqutas"
        elif self.tipoDelToken is tokensHtml.Numero_Decimal:
            return "Numero Decimal"  
        elif self.tipoDelToken is tokensHtml.Parrafo:
            return "Parrafo" 
        elif self.tipoDelToken is tokensHtml.Hipervinculo:
            return "Hipervinculo"
        elif self.tipoDelToken is tokensHtml.Propiedades:
            return "Propiedad"
        elif self.tipoDelToken is tokensHtml.Unidades_de_Medida:
            return "Unidades de Medida"   
        elif self.tipoDelToken is tokensHtml.Lista:
            return "Lista" 
        elif self.tipoDelToken is tokensHtml.Mayor_Que:
            return "Mayor Que"
        elif self.tipoDelToken is tokensHtml.Menor_Que:
            return "Menor Que"   
        elif self.tipoDelToken is tokensHtml.Diagonal:
            return "Diagonal"     
        elif self.tipoDelToken is tokensHtml.Punto:
            return "Punto"  
        elif self.tipoDelToken is tokensHtml.Igual:
            return "Igual"
        elif self.tipoDelToken is tokensHtml.Parentesis_Abierto:
            return "Parentesis Abierto"
        elif self.tipoDelToken is tokensHtml.Parentesis_Cerrado:
            return "Parentesis Cerrado"                
        else:
            return "desconocido"   