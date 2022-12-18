
from cgitb import handler
#from turtle import circle
import xml.sax

from leerFichero import CiudadesHandler


class Grafo():

    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    Handler = CiudadesHandler()
    parser.setContentHandler(Handler)

    def __init__(self, ficheroGrafo):
        
        Grafo.parser.parse(ficheroGrafo)
        
        self.nodosGrafo = Grafo.Handler.getNodos()
        self.aristasGrafo = Grafo.Handler.getAristas()
        self.idsNodos = Grafo.Handler.getIdsNodos()
        self.idsAristas = Grafo.Handler.getIdsAristas()
        
    def existeNodo(self, source):  # Indica si un nodo existe en el grafo
        for n in self.idsNodos:
            if int(source) == int(n):
                return True
        else:
            print("NODO INEXISTENTE")    
            return False
        
    def existeArista(self, sourceOrigen, sourceDestino,sourceID):  # Indica si una arista existe en el grafo
        for a in self.idsAristas:
            info = a.split(',')
            if int(sourceOrigen) == int(info[0]) and int(sourceDestino) == int(info[1]) and int(sourceID) == int(info[2]):
                return True
        else:
            print("ARISTA INEXISTENTE")    
            return False
        
    def existeAristaSinID(self, sourceOrigen, sourceDestino):  # Mismo método de existeArista pero sin necesidad de indicar el ID
        for a in self.idsAristas:
            info = a.split(',')
            if int(sourceOrigen) == int(info[0]) and int(sourceDestino) == int(info[1]):
                return True
        else:
            print("ARISTA INEXISTENTE")    
            return False

    def getObjetoNodo(self,source):  # Busca el id del nodo y te devuelve el objeto
        if self.existeNodo(source):
            for n in self.nodosGrafo:
                if int(source) == int(n.getIDNodo()):
                    return n
        else:
            return None
        
    def getObjetoArista(self, sourceOrigen, sourceDestino, sourceID):  # Busca el id de la arista y te devuelve el objeto
        if self.existeArista(sourceOrigen, sourceDestino, sourceID):
            for n in self.aristasGrafo:
                if (int(sourceID) == int(n.getIDArista()) and (int(sourceOrigen) == int(n.getSourceArista())) and (int(sourceDestino) == int(n.getTargetArista()))):
                    return n
        else:
            return None
        
    def getObjetoAristaSinID(self, sourceOrigen, sourceDestino):  # Mismo método de getObjetoArista pero sin necesidad de indicar el ID
        if self.existeAristaSinID(sourceOrigen, sourceDestino):
            for n in self.aristasGrafo:
                if ((int(sourceOrigen) == int(n.getSourceArista())) and (int(sourceDestino) == int(n.getTargetArista()))):
                    return n
        else:
            return None
        
    # Devuelve los atributos de un nodo indicando su id y los datos de las keys
    def getInfoNodo(self, source, datosKeys):
        nodo = self.getObjetoNodo(source)
        if nodo != None:
            print(" NODO", source, ":")
            for x in nodo.getAtributosNodo():
                print("    " , datosKeys[x].keyname, ":", nodo.getAtributosNodo()[x])
                
    # Devuelve los atributos de una arista indicando su id y los datos de las keys
    def getInfoArista(self, sourceOrigen, sourceDestino, sourceID, datosKeys):
        arista = self.getObjetoArista(sourceOrigen, sourceDestino, sourceID)
        if arista != None:
            print(" ARISTA", sourceOrigen, sourceDestino, sourceID, ":")
            for x in arista.getAtributosArista():
                print("    " , datosKeys[x].keyname, ":", arista.getAtributosArista()[x])
                
    # Mismo método de getInfoArista pero sin necesidad de indicar el ID
    def getInfoAristaSinID(self, sourceOrigen, sourceDestino, datosKeys):
        arista = self.getObjetoAristaSinID(sourceOrigen, sourceDestino)
        if arista != None:
            print(" ARISTA", sourceOrigen, sourceDestino, arista.getIDArista(),":")
            for x in arista.getAtributosArista():
                print("    " , datosKeys[x].keyname, ":", arista.getAtributosArista()[x])
                
    def adyacentesAristas(self, source):  # Devuelve una lista de aristas adyacentes a un nodo
        adyacentes = []
        if self.existeNodo(source):
            for arista in self.aristasGrafo:
                if int(arista.source) == int(source):
                    a = self.getObjetoAristaSinID(arista.source, arista.target)
                    adyacentes.append(a)
            return adyacentes
        else: 
            return "error"
    
    def adyacentesNodo(self, source):  # Devuelve una lista de nodos adyacentes a otro
        adyacentes = []
        for a in self.aristasGrafo:
            if int(a.source) == int(source):
                adyacentes.append(a.target)
        return adyacentes
    
    def getArtistasGrafo(self):
        return self.aristasGrafo
#if (__name__ == "__main__"):
    
#    g = Grafo("Capitales y Talavera/CR.graphXML")
#    g.__init__