
from Estado import Estado

class Nodo:
    #__id: int
    #__datosXML: dict()  # Contiene todos los datos del nodo
    class_counter = 0
    
    
    def metodoBusqueda(self,tipoBusqueda):
        if tipoBusqueda == "anchura":
            valor=self.__profundidad
        elif tipoBusqueda == "costo":
            valor=self.__coste
        else:
            valor = (-1)/(self.__profundidad + 1)

        return valor
    
    def __init__(self, id, datosXML):
        self.__id = id
        self.__datosXML = datosXML
    

    # constructor
    def actualizarDatos(self, padre, estado, coste, tipoBusqueda, accion, profundidad): #id
        self.__id = Nodo.class_counter
        self.__padre = padre
        self.__estado = estado
        self.__accion = accion
        self.__profundidad = profundidad
        #self.__heuristica = 0 # de momento, inicializada a 0 ya que no la usaremos en nuestros algoritmos de búsqueda
        
        if self.__padre == None:
            self.__coste = 0
            self.__profundidad = 0
        else:
            self.__coste = padre.getCoste() + coste
            self.__profundidad = padre.getProfundidad() + 1
        
        v = self.metodoBusqueda(tipoBusqueda)
        self.__valor = v
        Nodo.class_counter += 1
        #self.__datosXML = datosXML
        
        
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
    
    
    def getAtributosNodo(self):
        return self.__datosXML