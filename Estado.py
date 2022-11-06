
import hashlib


class Estado:

    def __init__(self,nodo,lista_nodos, coste):
        self.nodo = nodo
        self.listNodos = sorted(lista_nodos)
        self.id = self.md5generador(self.nodo,self.listNodos)
        self.coste = coste
        
    def md5generador(self,id_nodo,lista):
        # creamos el estado (nodo actual +  nodos por visitar) y creamos su id en formato md5
        estado = f'{id_nodo} {lista}'
        md5 = hashlib.md5(estado.encode())
        return md5.hexdigest()

    def getNodo(self):
        return self.nodo

    def getListaNodos(self):
        return self.listNodos
    
    def getCoste(self):
        return self.coste
