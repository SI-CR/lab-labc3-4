import xml.sax

class CiudadesHandler(xml.sax.ContentHandler):

    def startElement(self, name, attrs): #Esto lee el inicio de todas las etiquetas
        self.current = name #Esto indica en que  trozo del xml esta (node, edge)
        if name == 'node':
            self.id = attrs.get('id')
            print(" Id nodo: " + self.id + " ")
        if name == 'data':
            self.key = attrs.get('key')
            print("       key del dato: " + self.key + " ")
    
    def characters(self, content):  #Lee el contenido que hay entre la etiqueta start y end
            self.contenidoEtiqueta = content

    def endElement(self, name): # </
        if name == "node":
         print("         " + self.contenidoEtiqueta)
        self.current=""

   

        

parser = xml.sax.make_parser()
handler = CiudadesHandler()
parser.setContentHandler(handler)
parser.parse('ejemplo.graphXML')