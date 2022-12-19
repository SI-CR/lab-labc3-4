#!/usr/bin/python3

from Grafo import Grafo
from Estado import Estado
import math
import itertools

class EspacioDeEstados:

    minima_distancia = 0.0
    def __init__(self, ficheroGrafo):
        self.__grafo = Grafo(ficheroGrafo)

    # método que nos indica si un nodo pertenece al grafo o no
    def nodoPerteneceGrafo(self, nodoInicial, listaNodos):
        if not self.__grafo.existeNodo(nodoInicial):
            return False
        for n in listaNodos:
            if not self.__grafo.existeNodo(n):
                return False
        return True
    
    def getGrafo(self):
        return self.__grafo

    def arcoMinimo(self):
        arcoMin = float('inf')
        aristas = self.__grafo.getArtistasGrafo()
        for ar in aristas:
            longArista = ar.getAtributosArista().get("d17")
            arcoMin = min(arcoMin,float(longArista))
        return arcoMin
    
    def heuristicaArco(self,listaNodosVisitados,arcoMinimo):
        return float(arcoMinimo) * len(listaNodosVisitados)
    
        
    def calcularDistancia(self, n1, n2):
        
        nodo1 = self.__grafo.getObjetoNodo(n1)
        nodo2 = self.__grafo.getObjetoNodo(n2)
        atributosN1 = nodo1.getAtributosNodo()
        atributosN2 = nodo2.getAtributosNodo()
        xN1 = atributosN1.get("d6")
        yN1 = atributosN1.get("d5")
        xN2 = atributosN2.get("d6")
        yN2 = atributosN2.get("d5")
        
        a = (float(xN1)-float(xN2))**2
        b = (float(yN1)-float(yN2))**2

        result = math.sqrt((a+b))
       
        return result
    
    def calcularHeuristica(self, nodoInicial, listaNodos):
        if len(listaNodos) == 0:
            return 0
        else:
            listaDist = list()
            if len(listaNodos)>1:
                listaNodos.append(nodoInicial)
                combinaciones = itertools.combinations(listaNodos,2)
                for combi in combinaciones:
                    dist = self.calcularDistancia(combi[0],combi[1])
                    listaDist.append(dist)
                self.minima_distancia = sorted(listaDist).pop(0)
            listaDist.clear()
            listaDist.append(self.minima_distancia)
            for nv in listaNodos:
                dist = self.calcularDistancia(nodoInicial,nv)
                listaDist.append(dist)
            minimo = sorted(listaDist).pop(0) * len(listaNodos)
            return round(minimo,2)



    # en este metodo se encarga de devolver una lista de sucesores para  
    # el estado que hemos pasado como parametro.
    def sucesores(self, estado,d1,tipoHeuristica,arcominimo):

        listaSucesores = []
        listaAdyacentes = self.__grafo.adyacentesAristas(estado.getNodo())
        listaAdyacentes = sorted(listaAdyacentes, key=lambda Edge: (int(Edge.getTargetArista())))
        heuristica = 0
        nodosSinVisitar = estado.getListaNodos()
        
        # en caso de que el nodo tenga aristas adyacentes
        if len(listaAdyacentes) > 0:
           
           # obtenemos el nombre de la calle y la distancia (coste) de cada arista
            for arista in listaAdyacentes:
                atributos = arista.getAtributosArista()
                nombreCalle = atributos.get('d23')
                coste = atributos.get('d17')
                if nombreCalle == None: nombreCalle = "<Sin Nombre>"

                listaNuevosNodos = []
                
                # obtenemos los nodos que conectan con cada arista adyacente del nodo en el que nos encontramos
                for i in nodosSinVisitar:
                    siguienteNodo = arista.getTargetArista()
                    if  i != siguienteNodo:
                        listaNuevosNodos.append(i)
                if tipoHeuristica == "euclidea":
                    minCombiDistan = list()
                    combs = itertools.combinations(estado.getListaNodos(), 1)
                    for combi in combs:
                        dist = self.calcularDistancia(combi[0],estado.getNodo())
                        minCombiDistan.append(dist)
                    d2 = min(minCombiDistan,default=0)
                    heuristica = min(d1,d2) * len(estado.getListaNodos())
                elif tipoHeuristica == "arco":
                    heuristica = self.heuristicaArco(listaNuevosNodos,arcominimo)
                
                # creamos un nuevos estado con el primer adyacente
                # y la lista de nodos adyacentes (eliminando el primero, que es el que hemos cogido)
                nuevoEstado = Estado(siguienteNodo,listaNuevosNodos, heuristica)
                # creamos el formato de la solución con la acción de movernos de un nodo a otro adyacente, indicando el nombre
                # de la calle (arista), su coste, y el nuevo estado resultante tras esa acción 
                #formato= '{} --> {}: {} ({}, {}) coste: {}, ID (md5):'.format(estado.getNodo(), siguienteNodo, nombreCalle, siguienteNodo, nuevoEstado.getListaNodos(), round(float(distancia),2))
                # formato = '{} --> {} ({}) coste: {}'.format(estado.getNodo(),siguienteNodo,nombreCalle,float(coste))
                formato = '{} --> {}'.format(estado.getNodo(),siguienteNodo)
                #round: redondea el número al entero más cercano.
                listaSucesores.append([formato, nuevoEstado, coste])
            return listaSucesores
        
        else: 
            return None