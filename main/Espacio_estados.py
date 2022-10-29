#!/usr/bin/python3

import Grafo
from Estado import *

class EspacioDeEstados:

    def __init__(self, fichero_graphml):
        self.__grafo = Grafo(fichero_graphml)

    # este metodo nos dice si un nodo pertenece al grafo o no
    def esta(self, estado):
        if not self.__grafo.pertenece_nodo(estado.get_nodo()):
            return False
        for i in estado.get_lista_nodos():
            if not self.__grafo.pertenece_nodo(i):
                return False
        return True


    # en este metodo se encarga de devolver una lista de sucesores para  
    # el estado que hemos pasado como parametro.
    def sucesores(self, estado):

        lista_sucesores = []

        lista_de_adyacentes = self.__grafo.adyacentesNodo(estado.get_nodo())

        lista_nodos_por_recorrer = estado.get_lista_nodos()

        for ady in lista_de_adyacentes:
            nombre_calle = ady[2] # cogemos el ady [2] porque el 1 es el propio nodo

            lista_nodos_nueva = []

            for i in lista_nodos_por_recorrer:
                if  i != ady[1]:
                    lista_nodos_nueva.append(i)

            estado_nuevo = Estado(ady[1],estado.get_lista_nodos().remove(ady[1])) #cogemos el nuevo estado cogiendo el primer adyacente
            # y la lista de nodos adyacentes eliminando el primero, que es el que hemos cogido
            coste = ady[3] # distancia entre el nodo inicial y el nodo 
            acc_m= '({} -> {} ({}) coste: {})'.format(estado.get_nodo(),ady[1],nombre_calle,round(float(ady[3]),2))
            #round:redondea el número al entero más cercano.
            lista_sucesores.append([acc_m,estado_nuevo,coste]) # introducimos en la nueva lista de sucesores el nuevo sucesor

        return lista_sucesores
