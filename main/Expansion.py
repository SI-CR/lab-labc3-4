from EspacioDeEstados import EspacioDeEstados
from Nodo import Nodo
from Estado import Estado

def AlgoritmoBusqueda (self,problema,estrategia,profundidad_maxima):
    nodo=Nodo()
    listaSucesores = EspacioDeEstados.sucesores(nodo.getEstado())
    if estrategia == "Anchura":
        nodo.valor = nodo.getProfundidad()
    elif  estrategia == "Profundidad":
        nodo.valor=1/(nodo.profundidad+1)
    elif  estrategia == "Costo Uniforme":
        nodo.valor=nodo.getCosto()

    nodo.id = nodo.getProfundidad()+1 # ponemos que sea mas 1 ya que la profundidad empezara en 0 
    nodo.padre = nodo.getPadre()
    nodo.profundidad 
