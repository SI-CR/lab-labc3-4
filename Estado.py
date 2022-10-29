
import hashlib


class Estado:
    
    def md5generador(self,id_nodo,lista):
        n=0
        m = hashlib.md5()
        m.update(id_nodo.encode())
        for i in lista:
            m.update(list[n].encode())
            n=n+1
        return m.hexdigest()

    def __init__(self,nodo,lista_nodos,coste):
        self.nodo = nodo
        self.lista_nodos = sorted(lista_nodos)
        self.id = self.md5generador(self.nodo,self.lista_nodos)

    def get_nodo(self):
        return self.nodo

    def get_lista_nodos(self):
        return self.lista_nodos

