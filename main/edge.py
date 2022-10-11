class edge():
    id:int
    source:int
    target:int   
    diccionario:dict()
    def __init__(self,id,source,target,diccionario):
        self.id = id
        self.source = source
        self.target = target
        self.diccionario = diccionario