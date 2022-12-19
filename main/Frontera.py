
from NodoArbol import NodoArbol
from queue import PriorityQueue


class Frontera:

    def __init__(self):
        self.listaFrontera = PriorityQueue()

    def anadirNodo(self, nodo):
        self.listaFrontera.put((nodo.getValor(), nodo.getIDNodo(), nodo))

    def anadirListaNodos(self, Ln):
        for nodo in Ln:
            self.anadirNodo(nodo)

    def sacar(self):
        return self.listaFrontera.get(0)[2]

    def estaVacia(self):
        return self.listaFrontera == []
