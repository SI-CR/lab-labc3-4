from NodoArbol import NodoArbol
from Frontera import Frontera
from Problema import Problema


def busquedaSolucion(problema, estrategia, profundidadMaxima,d1,tipoHeuristica):

    solucion = None

    while (solucion == None):
        solucion, ultimoNodoVisitado = algoritmoBusqueda(problema, estrategia, profundidadMaxima,d1,tipoHeuristica)

    return solucion, ultimoNodoVisitado


def algoritmoBusqueda(problema, estrategia, profundidaMaxima,d1,tipoHeuristica):

    datosPoda = []
    frontera = Frontera()
    estadoInicial = problema.getEstadoInicial()
    nodoInicial = NodoArbol(None, estadoInicial, 0, estrategia, '0.0 0 0.0')
    frontera.anadirNodo(nodoInicial)
    solucion = None

    while ((solucion == None) and (not (frontera.estaVacia()))):
        nodoActual = frontera.sacar()
        estadoNodoActual = nodoActual.getEstado()
        if problema.esObjetivo(estadoNodoActual):  #Aqui compara si la linea de estados esta vacia
            solucion = True
        else:
            # comprobar profundidad e id estado visitado
            if nodoActual.getProfundidad() <= profundidadMaxima and nodoActual.getEstado().getID() not in datosPoda:
                sucesoresEstado = problema.getEspacioEstados().sucesores(estadoNodoActual,d1,tipoHeuristica)
                datosPoda.append(nodoActual.getEstado().getID())
                if sucesoresEstado != None:
                    listaNodos = expandirNodos(sucesoresEstado, nodoActual, profundidaMaxima, estrategia)
                    frontera.anadirListaNodos(listaNodos)
    if (solucion == None):
        return None, None
    else:
        return formatoSolucion(nodoActual), nodoActual


def expandirNodos(listaSucesores, padre, profundidadMaxima, estrategia):

    listaNodos = []
    for datosSucesor in listaSucesores:
        coste = datosSucesor[2]
        accion = datosSucesor[0]
        estado = datosSucesor[1]
        nodo = estado.getNodo()
        nodo = NodoArbol(padre, estado, coste, estrategia, accion)
        listaNodos.append(nodo)
    return listaNodos


def formatoSolucion(nodo):

    solucion = []

    while nodo.getPadre() is not None:
        solucion.append(nodo)
        nodo = nodo.getPadre()
    solucion.append(nodo)
    return solucion


if __name__ == "__main__":

    listaNodosSolucion = []

    profundidadMaxima = 600
    Estrategia = "a*"
    nodoInicial = "71"
    listaNodosInicial = ['2','112', '287', '561', '660']
    tipoHeuristica = "arco"
    
    problema = Problema(nodoInicial, listaNodosInicial,tipoHeuristica)
    d1 = problema.d1

    solucion, ultimoNodoVisitado, = busquedaSolucion(
        problema, Estrategia, profundidadMaxima,d1,tipoHeuristica)

    if (solucion is not None):
        print("SOLUCION ENCONTRADA")
        print("- Problema:",  problema.getEstadoInicial().getNodo(),
              problema.getEstadoInicial().getListaNodos())
        print("- Estrategia usada:", Estrategia)
        print("- Estado:", ultimoNodoVisitado.getEstado().getNodo(), ultimoNodoVisitado.getEstado().getListaNodos())
        print("- Ultimo nodo visitado:", ultimoNodoVisitado.getIDNodo(), ultimoNodoVisitado.get6Digitos())
        #3e8b20
        print("- CAMINO SEGUIDO:")
        for nodo in reversed(solucion):
            if nodo.getPadre() == None:
                print("[",nodo.getIDNodo(),"][",round(nodo.getCoste(),2),"[(", nodo.getEstado().getNodo(),",",nodo.getEstado().getListaNodos(),")|", nodo.get6Digitos(), "]",
                    None, nodo.getAccion(), nodo.getProfundidad(), round(nodo.getHeuristica(),2), round(nodo.getValor(),2),"]")
            else:
                print("[",nodo.getIDNodo(),"][",round(nodo.getCoste(),2),"[(", nodo.getEstado().getNodo(),",",nodo.getEstado().getListaNodos(),")|", nodo.get6Digitos(), "]",
                    nodo.getPadre().getIDNodo(), nodo.getAccion(), nodo.getProfundidad(), round(nodo.getHeuristica(),2), round(nodo.getValor(),2),"]")
        print("- PROFUNDIDAD:", ultimoNodoVisitado.getProfundidad())
        print("- COSTE TOTAL:",ultimoNodoVisitado.getValor())
        print("FIN DEL PROGRAMA")
    else:
        print("NO HAY SOLUCIÓN")
