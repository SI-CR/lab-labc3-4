
# from cgitb import handler
import xml.sax

from key import Key
from Nodo import Nodo
from Edge import Edge


class CiudadesHandler(xml.sax.ContentHandler):

    def __init__(self):
        self.datosxml = dict()  # tiene los datos de cualquier etiqueta ya sea nodo o aristas, estos datos estan guardados en forma de diccionario con la key y su contenido
        self.todosNodos = list()
        self.idsNodos = list()
        self.todasAristas = list()
        self.idsAristas = list()
        self.datosKeys = dict()

    # Esto lee el inicio de todas las etiquetas
    def startElement(self, tag, atributos):
        # Esto indica en que  trozo del xml esta (node, edge)
        self.current = tag
        if tag == 'node':
            self.id = atributos.get('id')
            self.idsNodos.append(self.id)

        if tag == 'data':
            self.key = atributos.get('key')

        if tag == 'key':
            self.idKey = atributos.get('id')
            self.forKey = atributos.get('for')
            self.keyName = atributos.get('attr.name')
            # Creo un objeto key con todos los valores que me da esa etiqueta
            objkey = Key(self.idKey, self.forKey, self.keyName)
            # Para identificar los ids rapidos creo un diccionario y a cada id le asigno su objeto
            self.datosKeys.update({self.idKey: objkey})

        if tag == 'edge':
            self.origen = atributos.get('source')
            self.destino = atributos.get('target')
            self.idArista = atributos.get('id')
            self.idsAristas.append(self.origen + "," +
                                   self.destino + "," + self.idArista)

    def characters(self, content):  # Lee el contenido que hay entre la etiqueta start y end
        self.contenidoEtiqueta = content  # Lo uso en endElement

    def endElement(self, name):  # </
        if name == 'data':
            # Hago el diccionario de datos del nodo
            self.datosxml.update({self.key: self.contenidoEtiqueta})

        if name == 'node':
            # cada vez que ve la etiqueta node crea un nodo nuevo, conque da igual el nombre de la variable que tenga
            nodo = Nodo(self.id, self.datosxml)
            self.todosNodos.append(nodo)
            self.datosxml = {}  # Vacio el diccionario para el siguiente nodo

        if name == 'edge':
            # self.datosxml.update({self.key: self.contenidoEtiqueta})
            arista = Edge(self.idArista, self.origen,
                          self.destino, self.datosxml)
            self.todasAristas.append(arista)
            self.datosxml = {}

    def getNodos(self):
        return self.todosNodos

    def getIdsNodos(self):
        return self.idsNodos

    def getAristas(self):
        return self.todasAristas

    def getIdsAristas(self):
        return self.idsAristas

    def getDatosKeys(self):
        return self.datosKeys

    def printNodos(self):
        print(self.todosNodos)
