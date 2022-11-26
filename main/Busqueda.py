from NodoArbol import NodoArbol
from Frontera import Frontera
from EspacioDeEstados import EspacioDeEstados
from Problema import Problema
from Grafo import Grafo
import stack

#nodosCreados = 0


def __init__(self):
    pass


def generarNodoArbol(padre, estado, coste, estrategia, accion):
    nodo = NodoArbol(padre, estado, coste, estrategia, accion)
    return nodo


def expandirNodos(listaSucesores, padre, profundidadMaxima, estrategia):
    listaNodos = []
    global nodosCreados
    # print("padre", padre.getProfundidad())
    if (padre.getProfundidad() < int(profundidadMaxima)):
        for datosSucesor in listaSucesores:
            #print("Sucesor", datosSucesor[0], datosSucesor[1].getNodo(
            #), datosSucesor[1].getListaNodos(), datosSucesor[2])
            coste = datosSucesor[2]
            accion = datosSucesor[0]
            estado = datosSucesor[1]
            nodo = generarNodoArbol(padre, estado, coste, estrategia, accion)
            #print(nodo.getAccion(), "COSTE ACUMULADO:", nodo.getCoste(),
            #      nodo.getEstado().getListaNodos())
            listaNodos.append(nodo)

            #nodosCreados += 1
    return listaNodos


def algoritmoPoda(dictPoda, listaNodos, estrategia):

    ListaNodosPoda=[]

    for nodo in listaNodos:
        estadoNodo=nodo.getEstado()
        idEstadoNodo=estadoNodo.getID()
        valorNodo=nodo.getValor()

        if (idEstadoNodo in dictPoda):
            if (estrategia in ["profundidad"]):
                # print("profundidad")
                if valorNodo > int(dictPoda.get(idEstadoNodo)):
                    #print("p")
                    dictPoda.update({idEstadoNodo: valorNodo})
                    ListaNodosPoda.append(nodo)
            else:
                # print("anchura")
                if valorNodo < int(dictPoda.get(idEstadoNodo)):

                    dictPoda.update({idEstadoNodo: valorNodo})
                    ListaNodosPoda.append(nodo)
        else:
            dictPoda.update({idEstadoNodo: valorNodo})
            ListaNodosPoda.append(nodo)

    return ListaNodosPoda, dictPoda


def formatoSolucion(nodo):
    pila=stack.Stack()

    nodoPila=nodo

    while (not nodoPila.getPadre() == None):
        pila.push(nodoPila)
        nodoPila=nodoPila.getPadre()

    pila.push(nodoPila)

    pilaSolucion=[]

    while not pila.isEmpty():
        pilaSolucion.append(pila.pop())

    return pilaSolucion


def algoritmoBusqueda(problema, estrategia, profundidaMaxima):

    dictPoda={}

    frontera=Frontera()
    estadoInicial=problema.getEstadoInicial()
    nodoInicial=generarNodoArbol(None, estadoInicial, 0, estrategia, '0.0 0 0.0')
    frontera.anadirNodo(nodoInicial)
    solucion=None

    while ((solucion == None) and (not (frontera.estaVacia()))):
        nodoActual=frontera.sacar()
        estadoNodoActual=nodoActual.getEstado()
        #print("nodo actual", nodoActual.getAccion(), estadoNodoActual.getListaNodos())
        if problema.esObjetivo(estadoNodoActual):
            solucion=True
        else:
            sucesoresEstado=problema.getEspacioEstados().sucesores(estadoNodoActual)
            if sucesoresEstado != None:
                #print("s", sucesoresEstado)
                listaNodos=expandirNodos(
                    sucesoresEstado, nodoActual, profundidaMaxima, estrategia)
                nodosPoda, dictPoda = algoritmoPoda(
                    dictPoda, listaNodos, estrategia)
                frontera.anadirListaNodos(nodosPoda)

    if (solucion == None):
        return None, None
    else:
        return formatoSolucion(nodoActual), nodoActual


def busquedaSolucion(problema, estrategia, profundidadMaxima):

    #prof_Actual = 0
    solucion = None

    while ((solucion == None)):
        #global nodosCreados
        #nodosCreados = 0
        solucion, ultimoNodoVisitado = algoritmoBusqueda(problema, estrategia, profundidadMaxima)
        #prof_Actual = prof_Actual + 1

    return solucion, ultimoNodoVisitado


if __name__ == "__main__":

    listaNodosSolucion = []

    profundidad = 0
    profundidadMaxima = 68
    Estrategia = "anchura"
    # nodoInicial = "123"
    # listaNodosInicial = ['12', '10', '122']
    nodoInicial = "54"
    listaNodosInicial = ['186', '699', '1277']
    problema = Problema(nodoInicial, listaNodosInicial)

    solucion, ultimoNodoVisitado, = busquedaSolucion(
        problema, Estrategia, profundidadMaxima)

    if (solucion is not None):
        # Se escribe la solucion en un archivo .txt
        print("Ultimo nodo visitado:", ultimoNodoVisitado.getIDNodo())
        print("Estrategia usada:", Estrategia)
        print("Problema:",  problema.getEstadoInicial().getNodo(), problema.getEstadoInicial().getListaNodos())
        for nodo in solucion:
            listaNodosSolucion.append(nodo.getIDNodo())
        print(listaNodosSolucion)
        print("Profundidad", ultimoNodoVisitado.getProfundidad())
        print("Coste", round(ultimoNodoVisitado.getCoste(),2))
        print("FIN DEL PROGRAMA")
    else:
        print("NO HAY SOLUCIÓN")
