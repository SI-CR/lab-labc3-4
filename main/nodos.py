class nodos:
    id:int
    diccionario:dict() #Contiene todos los datos del nodo
    
    #constructor
    def __init__(self,id,diccionario):
        self.id = id
        self.diccionario = diccionario
