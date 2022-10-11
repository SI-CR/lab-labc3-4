class Grafo():
    nodos:list()
    aristas:list()

    def __init__(self):
        self.nodos = list()
        self.aristas = list()

    def adyacentes(self,source):  #Devuelve una lista de adyacentes
        adyacentes = []
        for x in self.aristas:
             if int(x.source) == int(source):
                adyacentes.append(x.target)
        return adyacentes
    
    def getObjetoNodo(self,source):  #Busca el id del nodo y te devuelve el objeto
        for x in self.nodos:
            if int(source) == int(x.id):
                return x
        return None

    def pintarInfo(self,source,datosKeys):
        nodo = self.getObjetoNodo(source)
        print("Nodo id: ", source)
        for x in nodo.diccionario:
            #nodo.diccionario[x]
            print("    " + datosKeys[x].keyname + ": " + nodo.diccionario[x])
