import Estado

class Nodo:
    id: int
    idGeneracion: int
    padre: int
    estado: Estado
    valor:int
    profundidad:int
    costo:int
    heuristica:float
    accion:str
    diccionario: dict()  # Contiene todos los datos del nodo

    # constructor
    def __init__(self, id, diccionario):
        self.id = id
        self.diccionario = diccionario
        
    def getIDNodo(self):
        return self.id
    
    def getAtributosNodo(self):
        return self.diccionario

    def toString(self):
        print('[{}][{},{},{},{},{},{},{}]'.format(self.id,self.costo,self.estado,self.padre,self.accion,self.profundidad,self.heuristica,self.valor))
