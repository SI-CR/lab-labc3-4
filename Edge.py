class Edge():
    id: int
    source: int
    target: int
    diccionario: dict()

    def __init__(self, id, source, target, diccionario):
        self.id = id
        self.source = source
        self.target = target
        self.diccionario = diccionario
        
    def getIDArista(self):
        return self.id
    
    def getSourceArista(self):
        return self.source
    
    def getTargetArista(self):
        return self.target
    
    def getAtributosArista(self):
        return self.diccionario
    
    def getTodosAtributosArista(self):
        return self.id, self.source, self.target, self.diccionario