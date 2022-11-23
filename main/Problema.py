
from EspacioDeEstados import EspacioDeEstados
from Estado import Estado
from Frontera import Frontera

class Problema:

    def __init__(self):
        espacioEstados=EspacioDeEstados("lab-labc3-4/main/CR.graphXML")

        #Definicion del EstadoInicial
        nodoInicial = "3123"
        listaNodosInicial = ['3161', '3114', '2479', '3365', '3363']
        
        existenNodos = True
        if not espacioEstados.nodoPerteneceGrafo(nodoInicial, listaNodosInicial):
            existenNodos = False
                    
        if (existenNodos):
            heuristica = 0
            self.__estadoInicial=Estado(nodoInicial,listaNodosInicial,heuristica)
        
            solucion = espacioEstados.sucesores(self.__estadoInicial)
            for s in solucion:
                print(s)
        
        #TAREA 3
        frontera = Frontera()
        nodoInicialFrontera = "3123"
        frontera.addNodoFrontera(espacioEstados.grafo.getObjetoNodo(nodoInicialFrontera)) #Nodo inicio
        #frontera.expandirNodos(espacioEstados.grafo)

    def getEstadoInicial(self):
        return self.__estadoInicial

    def getEspacioEstados(self):
        return self.__espacioEstados
    
    def esObjetivo(self,estado):
        return estado.getListaNodos() == []
    
if (__name__ == "__main__"):
    
    p = Problema()