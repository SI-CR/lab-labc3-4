
from EspacioDeEstados import EspacioDeEstados
from Estado import Estado


class Problema:

    d1 = 0

    def __init__(self, nodoInicial, listaNodosInicial, tipoHeuristica):
        listaNodosInicial = sorted(listaNodosInicial, key=lambda reverse: True)
        self.__espacioEstados = EspacioDeEstados("nuevo.graphxml")

        existenNodos = True
        if not self.__espacioEstados.nodoPerteneceGrafo(nodoInicial, listaNodosInicial):
            existenNodos = False

        if (existenNodos):
            heuristica = 0
            if tipoHeuristica == "euclidea":
                self.d1 = self.__espacioEstados.calcularHeuristica(
                    nodoInicial, listaNodosInicial)
                heuristica = self.d1
            elif tipoHeuristica == "arco":
                heuristica = self.__espacioEstados.heuristicaArco(
                    listaNodosInicial, self.__espacioEstados.arcoMinimo())  # esto es para d1

            self.__estadoInicial = Estado(
                nodoInicial, listaNodosInicial, heuristica)

    def getEstadoInicial(self):
        return self.__estadoInicial

    def getEspacioEstados(self):
        return self.__espacioEstados

    def esObjetivo(self, estado):
        return estado.getListaNodos() == []

    def getGrafo(self):
        return self.__espacioEstados.getGrafo()
    
