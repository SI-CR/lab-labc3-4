#!/usr/bin/python3

from Grafo import Grafo
from Estado import Estado

class EspacioDeEstados:

    grafo: Grafo

    def __init__(self, ficheroGrafo):
        self.grafo = Grafo(ficheroGrafo)

    # método que nos indica si un nodo pertenece al grafo o no
    def nodoPerteneceGrafo(self, nodoInicial, listaNodos):
        if not self.grafo.existeNodo(nodoInicial):
            return False
        for n in listaNodos:
            if not self.grafo.existeNodo(n):
                return False
        return True


    # en este metodo se encarga de devolver una lista de sucesores para  
    # el estado que hemos pasado como parametro.
    def sucesores(self, estado):

        listaSucesores = []
        listaAdyacentes = self.grafo.adyacentesAristas(estado.getNodo())
        nodosSinVisitar = estado.getListaNodos()
        
        # en caso de que el nodo tenga aristas adyacentes
        if len(listaAdyacentes) > 0:
           
           # obtenemos el nombre de la calle y la distancia (coste) de cada arista
            for arista in listaAdyacentes:
                atributos = arista.getAtributosArista()
                nombreCalle = atributos.get('d22')
                distancia = atributos.get('d16')

                listaNuevosNodos = []
                
                # obtenemos los nodos que conectan con cada arista adyacente del nodo en el que nos encontramos
                for i in nodosSinVisitar:
                    siguienteNodo = arista.getTargetArista()
                    if  i != siguienteNodo:
                        listaNuevosNodos.append(i)
                        
                # creamos un nuevos estado con el primer adyacente
                # y la lista de nodos adyacentes (eliminando el primero, que es el que hemos cogido)
                nuevoEstado = Estado(siguienteNodo,sorted(listaNuevosNodos), distancia)
                #coste = distancia (distancia entre el nodo inicial y el nodo, o lo que es lo mismo, la longitud de la calle o arista)
                # creamos el formato de la solución con la acción de movernos de un nodo a otro adyacente, indicando el nombre
                # de la calle (arista), su coste, y el nuevo estado resultante tras esa acción 
                formato= '{} --> {}: {} ({}, {}) coste: {}'.format(estado.getNodo(), siguienteNodo, nombreCalle, siguienteNodo, nuevoEstado.getListaNodos(), round(float(distancia),2))
                #round: redondea el número al entero más cercano.
                listaSucesores.append([formato]) # lo introducimos en la nueva lista de sucesores

            return listaSucesores
        
        else: 
            return None