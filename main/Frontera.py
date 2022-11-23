import Estado

class Frontera:
    nodosFrontera = list()
    ultimoNodoExpandido = None
    idGeneracion = 0
        
    def addNodoFrontera(self, nodo):
        if self.ultimoNodoExpandido is None:
            nodo.padre = None
            nodo.profundidad = 0
            nodo.costo = 0
            nodo.valor =0    #ESTOO SEGUN EL ALGORITMO QUE UTILIZEMOS DEBE CAMBIAR
            self.ultimoNodoExpandido = nodo
        else:
            nodo.padre = self.ultimoNodoExpandido
            self.idGeneracion = self.idGeneracion +1
            nodo.idGeneracion = self.idGeneracion
            nodo.profundidad = (nodo.padre).profundidad + 1

        self.nodosFrontera.append(nodo)
    
    def sacarNodoFrontera(self,nodo):
        i = 0
        for x in self.nodosFrontera:
             i = i + 1
             if x.id == nodo.id:
                self.nodosFrontera.remove(i)

    def expandirNodos(self,grafo):

        valorMenor = None
        i = 0 #Contador que recorre los indices de la frontera
        posNodoMenor = 0 #Indica que posicion del vector corresponde al nodo con menor valorFrontera en la frontera
        for x in self.nodosFrontera:
            if valorMenor is None:
             valorMenor = x.valor
             posNodoMenor = i
            else:
             if valorMenor < x.valor:
                valorMenor = x.valor
                posNodoMenor = i
            i = i + 1

        aristaAd = grafo.adyacentesAristas(self.nodosFrontera[posNodoMenor].id)
        # nodosAdya = espacioEstados.sucesores(self.nodosFrontera(i))  #Esto creo que pilla algo raro, no pilla los nodos adyacentes
        for arista in aristaAd:
                costoArista = arista.diccionario["d16"]  #costo
                nodoNuevoFront = grafo.getObjetoNodo(arista.target)
                nodoNuevoFront.costo = self.nodosFrontera[posNodoMenor].costo + float(costoArista)
                self.addNodoFrontera(nodoNuevoFront)
        
        #saco el nodo de la frontera y busco sus adyacentes y los meto
        self.ultimoNodoExpandido = self.nodosFrontera[posNodoMenor]

        self.nodosFrontera.pop(posNodoMenor)  #Saco de la frontera ya el nodo expandido
        


    