from enum import Enum

class tokensArbol(Enum):
        Identificador = 1
        Cadena = 2
        Digito = 3
        Signo_Igual = 4
        Numero_Decimal = 5
        Comentario_Unilinea = 6
        Signo_por = 7
        PuntoYComa = 8
        Parentesis_Abierto = 9
        Parentesis_Cerrado = 10
        Llave_Abierta = 11
        Llave_Cerrada = 12
        Mayor_que = 13
        Menor_que = 14
        Punto = 15
        Signo_Mas = 16
        Signo_Menos = 17
        Corchete_Abierto = 18
        Corchete_Cerrado = 19
        Coma = 20
        Diagonal = 21
        Igual = 22
        And = 23
        Or = 24
        Comentario_Multilinea = 25
        Mas_Mas = 26
        Menos_Menos = 27
        Mayor_Igual_Que = 28
        Menor_Igual_Que = 29
        No = 30
        No_Es_Igual = 31
        Igualdad_Estricta = 32
        Desigualdad_Estricta = 33
        Dos_Puntos = 34
        Diagonal_Inversa = 35
        Numeral = 36
        Caracter = 37

class TokensArbol:

    def __init__(self, tipoDelToken):
        self.tipoDelToken = tipoDelToken

    def getTipo(self):
        if self.tipoDelToken is tokensArbol.Identificador:
            return "Identificador"
        elif self.tipoDelToken is tokensArbol.Cadena:
            return "Cadena"
        elif self.tipoDelToken is tokensArbol.Digito:
            return "Numero Entero"
        elif self.tipoDelToken is tokensArbol.Signo_Igual:
            return "Signo Igual"
        elif self.tipoDelToken is tokensArbol.Numero_Decimal:
            return "Numero Decimal"
        elif self.tipoDelToken is tokensArbol.Comentario_Unilinea:
            return "Comentario Unilinea"
        elif self.tipoDelToken is tokensArbol.Signo_por:
            return "Signo Por"
        elif self.tipoDelToken is tokensArbol.PuntoYComa:
            return "Punto y Coma"
        elif self.tipoDelToken is tokensArbol.Parentesis_Abierto:
            return "Parentesis Abierto"
        elif self.tipoDelToken is tokensArbol.Parentesis_Cerrado:
            return "Parentesis Cerrado"
        elif self.tipoDelToken is tokensArbol.Llave_Abierta:
            return "Llave Abierta"
        elif self.tipoDelToken is tokensArbol.Llave_Cerrada:
            return "Llave Cerrada"
        elif self.tipoDelToken is tokensArbol.Mayor_que:
            return "Mayor Que"
        elif self.tipoDelToken is tokensArbol.Menor_que:
            return "Menor Que"
        elif self.tipoDelToken is tokensArbol.Punto:
            return "Punto"
        elif self.tipoDelToken is tokensArbol.Signo_Mas:
            return "Signo Mas"
        elif self.tipoDelToken is tokensArbol.Signo_Menos:
            return "Signo Menos"
        elif self.tipoDelToken is tokensArbol.Corchete_Abierto:
            return "Corchete Abierto"
        elif self.tipoDelToken is tokensArbol.Corchete_Cerrado:
            return "Corchete Cerrado"
        elif self.tipoDelToken is tokensArbol.Coma:
            return "Coma"
        elif self.tipoDelToken is tokensArbol.Diagonal:
            return "Diagonal"
        elif self.tipoDelToken is tokensArbol.Igual:
            return "Igual"
        elif self.tipoDelToken is tokensArbol.And:
            return "And"
        elif self.tipoDelToken is tokensArbol.Or:
            return "Or"
        elif self.tipoDelToken is tokensArbol.Comentario_Multilinea:
            return "Comentario Multilinea"
        elif self.tipoDelToken is tokensArbol.Mas_Mas:
            return "Mas Mas"  
        elif self.tipoDelToken is tokensArbol.Menos_Menos:
            return "Menos Menos"   
        elif self.tipoDelToken is tokensArbol.Mayor_Igual_Que:
            return "Mayor Igual Que"       
        elif self.tipoDelToken is tokensArbol.Menor_Igual_Que:
            return "Menor Igual Que"  
        elif self.tipoDelToken is tokensArbol.No:
            return "No"  
        elif self.tipoDelToken is tokensArbol.No_Es_Igual:
            return "No Es Igual"
        elif self.tipoDelToken is tokensArbol.Igualdad_Estricta:
            return "Igualda Estricta" 
        elif self.tipoDelToken is tokensArbol.Desigualdad_Estricta:
            return "Desigualdad Estricta"
        elif self.tipoDelToken is tokensArbol.Dos_Puntos:
            return "Dos Puntos"
        elif self.tipoDelToken is tokensArbol.Diagonal_Inversa:
            return "Diagonal Inversa"
        elif self.tipoDelToken is tokensArbol.Numeral:
            return "Numeral"
        elif self.tipoDelToken is tokensArbol.Caracter:
            return "Caracter"
        else:
            return "Desconocido"