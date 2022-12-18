
import hashlib


class Estado:

    def __init__(self, nodo, lista_nodos, heuristica):
        self.nodo = nodo
        self.listaNodos = sorted(lista_nodos, key=lambda reverse: True)
        self.id = self.md5generador(self.nodo, self.listaNodos)
        self.heuristica = heuristica

    def md5generador(self, id_nodo, lista):
        estado = '(' + id_nodo + ','+'['
        for n in lista:
            if lista.index(n) == len(lista)-1:
                estado += n + '])'
            else:
                estado += n + ','
        if len(lista) == 0:
            estado += '])'
        md5 = hashlib.md5(str(estado).encode())
        return md5.hexdigest()

    def getID(self):
        return self.id

    def getNodo(self):
        return self.nodo

    def getListaNodos(self):
        return self.listaNodos
    
    def getHeuristica(self):
        return self.heuristica

    def get6digitosMD5(self):
        return self.id[26:]