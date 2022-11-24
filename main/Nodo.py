from Estado import Estado

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
    
    def getIdGeneracion(self):
        return self.idGeneracion

    def getPadre(self):
        return self.padre

    def getEstado(self):
        return self.estado

    def getProfundidad(self):
        return self.profundidad

    def getCosto(self):
        return self.costo

    def getHeuristica(self):
        return self.heuristica

    def getAccion(self):
        return self.accion

    def getAtributosNodo(self):
        return self.diccionario

    def toString(self):
        print('[{}][{},{},{},{},{},{},{}]'.format(self.id,self.costo,self.estado.seis_digitos(),self.padre,self.accion,self.profundidad,self.heuristica,self.valor))
