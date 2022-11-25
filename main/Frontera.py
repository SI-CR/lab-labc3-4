from NodoArbol import NodoArbol

class Frontera:

    def __init__(self):
        self.__listaFrontera = []

    def anadirNodo(self,nodoArbol):
        self.__listaFrontera.append(nodoArbol)
        self.__listaFrontera=sorted(self.__listaFrontera,key=lambda Nodo: Nodo.getValor())

    def anadirListaNodos(self, Ln):
        for nodo in Ln:
            self.anadirNodo(nodo)

    def sacar(self):
        return self.__listaFrontera.pop(0)

    def estaVacia(self):
        return self.__listaFrontera == []