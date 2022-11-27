from NodoArbol import NodoArbol
from Frontera import Frontera
from Problema import Problema


def busquedaSolucion(problema, estrategia, profundidadMaxima):

    solucion = None

    while (solucion == None):
        solucion, ultimoNodoVisitado = algoritmoBusqueda(
            problema, estrategia, profundidadMaxima)

    return solucion, ultimoNodoVisitado


def algoritmoBusqueda(problema, estrategia, profundidaMaxima):

    datosPoda = {}

    frontera = Frontera()
    estadoInicial = problema.getEstadoInicial()
    nodoInicial = NodoArbol(
        None, estadoInicial, 0, estrategia, '0.0 0 0.0')
    frontera.anadirNodo(nodoInicial)
    solucion = None

    while ((solucion == None) and (not (frontera.estaVacia()))):
        nodoActual = frontera.sacar()
        estadoNodoActual = nodoActual.getEstado()
        if problema.esObjetivo(estadoNodoActual):
            solucion = True
        else:
            sucesoresEstado = problema.getEspacioEstados().sucesores(estadoNodoActual)
            if sucesoresEstado != None:
                listaNodos = expandirNodos(
                    sucesoresEstado, nodoActual, profundidaMaxima, estrategia)
                nodosPoda, datosPoda = algoritmoPoda(
                    datosPoda, listaNodos, estrategia)
                frontera.anadirListaNodos(nodosPoda)

    if (solucion == None):
        return None, None
    else:
        return formatoSolucion(nodoActual), nodoActual


def expandirNodos(listaSucesores, padre, profundidadMaxima, estrategia):

    listaNodos = []

    if (padre.getProfundidad() < int(profundidadMaxima)):
        for datosSucesor in listaSucesores:
            coste = datosSucesor[2]
            accion = datosSucesor[0]
            estado = datosSucesor[1]
            nodo = NodoArbol(padre, estado, coste, estrategia, accion)
            listaNodos.append(nodo)

    return listaNodos


def algoritmoPoda(dictPoda, listaNodos, estrategia):

    ListaNodosPoda = []

    for nodo in listaNodos:
        idEstadoNodo = nodo.getEstado().getID()
        valorNodo = nodo.getValor()

        if (idEstadoNodo in dictPoda):
            if (estrategia in ["profundidad"]):
                if valorNodo > int(dictPoda.get(idEstadoNodo)):
                    dictPoda.update({idEstadoNodo: valorNodo})
                    ListaNodosPoda.append(nodo)
            else:
                if valorNodo < int(dictPoda.get(idEstadoNodo)):

                    dictPoda.update({idEstadoNodo: valorNodo})
                    ListaNodosPoda.append(nodo)
        else:
            dictPoda.update({idEstadoNodo: valorNodo})
            ListaNodosPoda.append(nodo)

    return ListaNodosPoda, dictPoda


def formatoSolucion(nodo):

    solucion = []

    while nodo.getPadre() is not None:
        solucion.append(nodo)
        nodo = nodo.getPadre()
    solucion.append(nodo)
    return solucion


if __name__ == "__main__":

    listaNodosSolucion = []

    profundidad = 0
    profundidadMaxima = 68
    Estrategia = "costo"
    nodoInicial = "54"
    listaNodosInicial = ['186', '699', '1277']
    problema = Problema(nodoInicial, listaNodosInicial)

    solucion, ultimoNodoVisitado, = busquedaSolucion(
        problema, Estrategia, profundidadMaxima)

    if (solucion is not None):
        print("SOLUCION ENCONTRADA")
        print("- Problema:",  problema.getEstadoInicial().getNodo(),
              problema.getEstadoInicial().getListaNodos())
        print("- Estrategia usada:", Estrategia)
        print("- Ultimo nodo visitado:", ultimoNodoVisitado.getIDNodo())
        for nodo in reversed(solucion):
            listaNodosSolucion.append(nodo.getIDNodo())
        print(listaNodosSolucion)
        print("- PROFUNDIDAD:", ultimoNodoVisitado.getProfundidad())
        print("- COSTE:", round(ultimoNodoVisitado.getCoste(), 2))
        print("FIN DEL PROGRAMA")
    else:
        print("NO HAY SOLUCIÓN")
