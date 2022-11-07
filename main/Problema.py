from EspacioDeEstados import EspacioDeEstados
from Estado import Estado

class Problema:

    def __init__(self):
        #objeto espacio de estados
        self.__espacioEstados=EspacioDeEstados("Capitales y Talavera/CR.graphXML")

        #Definicion del EstadoInicial
        nodoInicial = "3123"
        listaNodosInicial = ['3161', '3114', '2479', '3365', '3363']
        
        # Comprobamos que dichos nodos existen
        existenNodos = True
        if not self.__espacioEstados.nodoPerteneceGrafo(nodoInicial, listaNodosInicial):
            existenNodos = False
                    
        if (existenNodos):
            heuristica = 0
            self.__estadoInicial=Estado(nodoInicial,listaNodosInicial,heuristica)
        
            solucion = self.__espacioEstados.sucesores(self.__estadoInicial)
            for s in solucion:
                print(s)

    def getEstadoInicial(self):
        return self.__estadoInicial

    def getEspacioEstados(self):
        return self.__espacioEstados
    
    def esObjetivo(self,estado):
        return estado.getListaNodos() == []
    
if (__name__ == "__main__"):
    
    p = Problema()
