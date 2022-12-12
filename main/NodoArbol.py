
#from Estado import Estado


class NodoArbol:

    class_counter = 0

    def estrategiaBusqueda(self, estrategia):
        if estrategia == "anchura":
            valor = self.__profundidad
        elif estrategia == "costo":
            valor = self.__coste
        elif estrategia == "profundidad":
            valor = (-1)/(self.__profundidad + 1)
        elif estrategia == "a*":
            valor = self.__heuristica + self.__coste
        elif estrategia == "voraz":
            valor = self.__heuristica
        else:
            print("Estrategia no valida")
            valor = -1

        return valor

    def __init__(self, padre, estado, costo, estrategia, accion):
        self.__id = NodoArbol.class_counter
        NodoArbol.class_counter += 1
        self.__padre = padre

        self.__estado = estado
        self.__accion = accion
        if estrategia == "a*":
            self.__heuristica = estado.getHeuristica()
        else:
            if estrategia == "voraz":
                self.__heuristica = estado.getHeuristica()
            else:
                self.__heuristica = 0

        if self.__padre == None:
            self.__coste = 0
            self.__profundidad = 0
        else:
            self.__coste = padre.getCoste() + float(costo)
            self.__profundidad = padre.getProfundidad() + 1

        self.__valor = self.estrategiaBusqueda(estrategia)

    def getIDNodo(self):
        return self.__id

    def getCoste(self):
        return self.__coste

    def getProfundidad(self):
        return self.__profundidad

    def getValor(self):
        return self.__valor

    def getEstado(self):
        return self.__estado

    def getPadre(self):
        return self.__padre

    def getAccion(self):
        return self.__accion

    def get6Digitos(self):
        return self.getEstado().get6digitosMD5()
    
    def getHeuristica(self):
        return self.__heuristica
