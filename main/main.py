import xml.sax

from key import key
from nodos import nodos
from Grafo import Grafo
from edge import edge

datosKeys= dict()  #Contiene todos los datos de las etiquetas <keys
grafo = Grafo()


class CiudadesHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.datosxml = dict()  #tiene los datos de cualquier etiqueta ya sea nodo o aristas, estos datos estan guardados en forma de diccionario con la key y su contenido
  
    def startElement(self, name, attrs): #Esto lee el inicio de todas las etiquetas
        self.current = name #Esto indica en que  trozo del xml esta (node, edge)
        if name == 'node':
            self.id = attrs.get('id')
           
        if name == 'data':
            self.key = attrs.get('key')

        if name == 'key':
            self.idkey = attrs.get('id')
            self.fora = attrs.get('for')
            self.keyname = attrs.get('attr.name')
            objkey = key(self.idkey,self.fora,self.keyname)  #Creo un objeto key con todos los valores que me da esa etiqueta
            datosKeys.update({self.idkey:objkey}) #Para identificar los ids rapidos creo un diccionario y a cada id le asigno su objeto

        if name == 'edge':
            self.source = attrs.get('source')
            self.target = attrs.get('target')
            self.idArista = attrs.get('id')
    
    def characters(self, content):  #Lee el contenido que hay entre la etiqueta start y end
            self.contenidoEtiqueta = content #Lo uso en endElement

    def endElement(self, name): # </
        if name == 'data':
            #Hago el diccionario de datos del nodo
            self.datosxml.update({self.key:self.contenidoEtiqueta})
            
        if name == 'node':
            nodo = nodos(self.id,self.datosxml)#cada vez que ve la etiqueta node crea un nodo nuevo, conque da igual el nombre d ela variable que tenga
            grafo.nodos.append(nodo)
            self.datosxml = {} #Vacio el diccionario para el siguiente nodo

        if name == 'edge':
            self.datosxml.update({self.key:self.contenidoEtiqueta})
            arista = edge(self.idArista,self.source,self.target,self.datosxml)
            grafo.aristas.append(arista)
            self.datosxml = {}


parser = xml.sax.make_parser()
handler = CiudadesHandler()
parser.setContentHandler(handler)
parser.parse('AB.graphXML')





 
  
