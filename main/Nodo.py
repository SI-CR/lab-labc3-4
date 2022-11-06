
#import Estado

class Nodo:
    id: int
    diccionario: dict()  # Contiene todos los datos del nodo

    # constructor
    def __init__(self, id, diccionario):
        self.id = id
        self.diccionario = diccionario
        
    def getIDNodo(self):
        return self.id
    
    def getAtributosNodo(self):
        return self.diccionario
