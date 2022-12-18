
from EspacioDeEstados import EspacioDeEstados
from Estado import Estado

class Problema:

    d1 = 0
    arcoMinimo = 0

    def __init__(self, nodoInicial, listaNodosInicial,tipoHeuristica):
        #listaNodosInicial = []
        #for n in listaNodos:
        #    listaNodosInicial.append(int(n))
        listaNodosInicial = sorted(listaNodosInicial, key=lambda reverse:True)
        self.__espacioEstados=EspacioDeEstados("main/nuevo.graphxml")
        
        existenNodos = True
        if not self.__espacioEstados.nodoPerteneceGrafo(nodoInicial, listaNodosInicial):
            existenNodos = False
                    
        if (existenNodos):
            heuristica = 0
            if tipoHeuristica == "euclidea":
                self.d1 = self.__espacioEstados.calcularHeuristica(nodoInicial, listaNodosInicial)
                heuristica =self.d1
            elif tipoHeuristica == "arco":
                self.arcoMinimo = self.__espacioEstados.arcoMinimo()
                heuristica = self.__espacioEstados.heuristicaArco(listaNodosInicial,self.arcoMinimo)

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
    