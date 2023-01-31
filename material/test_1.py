import random

class Grafo:
    def __init__(self, dirigido=False):
        self.dirigido = dirigido
        self.vertices = {}
    
    def agregar_vertice(self, v):
        if v not in self.vertices:
            self.vertices[v] = {}
    
    def vertice_aleratorio(self):
        return random.choice(list(self.vertices.keys()))

    def adyacentes(self, v):
        return list(self.vertices[v])
    
    def agregar_arista(self, v, w, peso=1):
        self.vertices[v][w] = peso
        if not self.dirigido:
            self.vertices[w][v] = peso
    
    def es_arista(self, v, w):
        return w in self.vertices[v]
    
    def peso(self, v, w):
        if self.es_arista(v, w):
            return self.vertices[v][w]
    
    #def __iter__(self):
    #    return iter(self.vertices)

    #def __str__(self):
    #    return str(self.vertices)

    #def __repr__(self):
    #    return str(self.vertices)

    #def __len__(self):
    #    return len(self.vertices)