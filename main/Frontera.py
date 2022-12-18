
from NodoArbol import NodoArbol
from queue import PriorityQueue
#import heapq

# class Frontera:

#     def __init__(self):
#         self.__listaFrontera = []

#     def anadirNodo(self,nodoArbol):
#         #self.__listaFrontera.append(nodoArbol)
#         # if nodoArbol.getIDNodo() == 895:
#         #     print("coste", nodoArbol.getValor())
#         heapq.heappush(self.__listaFrontera,(float(nodoArbol.getValor()), int(nodoArbol.getIDNodo()),  nodoArbol))
#         #self.__listaFrontera=sorted(self.__listaFrontera,key=lambda NodoArbol: NodoArbol.getValor())

#     def anadirListaNodos(self, Ln):
#         for nodo in Ln:
#             self.anadirNodo(nodo)

#     def sacar(self):
#         return self.__listaFrontera.pop(0)

#     def estaVacia(self):
#         return self.__listaFrontera == []

class Frontera:
    #listaFrontera = PriorityQueue()

    def __init__(self):
        self.listaFrontera = PriorityQueue()

    def anadirNodo(self,nodo):
        #print("Añadido", nodo.getValor(),nodo.getIDNodo(),nodo)
        self.listaFrontera.put((nodo.getValor(),nodo.getIDNodo(),nodo))
        # self.listaFrontera.put(nodo.getValor(),nodo.getIDNodo(),nodo)
        
    def anadirListaNodos(self, Ln):
        for nodo in Ln:
            self.anadirNodo(nodo)
    
    def sacar(self):
       return self.listaFrontera.get(0)[2]
        
    def estaVacia(self):
        return self.listaFrontera == []