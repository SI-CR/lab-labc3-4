
from EspacioDeEstados import EspacioDeEstados
from Estado import Estado

class Problema:

    d1 = 0

    def __init__(self, nodoInicial, listaNodosInicial,tipoHeuristica):
        #listaNodosInicial = []
        #for n in listaNodos:
        #    listaNodosInicial.append(int(n))
        listaNodosInicial = sorted(listaNodosInicial, key=lambda reverse:True)
        self.__espacioEstados=EspacioDeEstados("main/nuevo.graphxml.xml")
        
        existenNodos = True
        if not self.__espacioEstados.nodoPerteneceGrafo(nodoInicial, listaNodosInicial):
            existenNodos = False
                    
        if (existenNodos):
            if tipoHeuristica == "euclidea":
                self.d1 = self.__espacioEstados.calcularHeuristica(nodoInicial, listaNodosInicial)
                heuristica =self.d1
            else:
                heuristica = self.__espacioEstados.heuristicaArco(listaNodosInicial,self.__espacioEstados.arcoMinimo())  #esto es para d1

            self.__estadoInicial=Estado(nodoInicial,listaNodosInicial,heuristica)
            #self.__estadoInicial.getListaNodos()
            

    def getEstadoInicial(self):
        return self.__estadoInicial

    def getEspacioEstados(self):
        return self.__espacioEstados
    
    def esObjetivo(self,estado):
        return estado.getListaNodos() == []
    
    def getGrafo(self):
        return self.__espacioEstados.getGrafo()
    