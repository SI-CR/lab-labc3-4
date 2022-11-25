from Estado import Estado

class NodoArbol:
    
    class_counter = 0
    
    def estrategiaBusqueda(self,estrategia):
        if estrategia == 'anchura':
            f=self.__profundidad
        elif estrategia == "costo":
            f=self.__coste
        else:
            f=int((-1)/(self.__profundidad+1))

        return f


    def __init__(self,padre,estado,costo,estrategia,accion):
        self.__id = NodoArbol.class_counter
        self.__padre= padre

        self.__estado= estado
        self.__accion=accion
        self.__h=0

        if self.__padre == None:
            self.__coste=0
            self.__profundidad=0
        else:
            self.__coste= padre.getCoste() + float(costo)
            self.__profundidad=padre.getProfundidad() + 1

        NodoArbol.class_counter += 1
        self.__valor=self.estrategiaBusqueda(estrategia)
    
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