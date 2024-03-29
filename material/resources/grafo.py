import random


class Grafo:
    def __init__(self, dirigido=False):
        """DOC: Representa un grafo no dirigido con aristas
        de peso 1 por default, implementado con diccinario
        de diccionarios"""
        self.dirigido = dirigido
        self.vertices = {}

    def agregar_vertice(self, v):
        """DOC: Agrega un vertice al diccionario de vertices"""
        if v not in self.vertices:
            self.vertices[v] = {}

    def vertice_aleatorio(self):
        """DOC: Devuelve un vertice aleratorio"""
        return random.choice(list(self.vertices))

    def adyacentes(self, v):
        """DOC: Devuelve una lista de adyacencia a un vertice
        PRE: Recibe un vertice valido
        POST: devuelve una lista de adyacencia"""
        return list(self.vertices[v])

    def obtener_vertices(self):
        """DOC: Devuelve una lista de vertices"""
        return self.vertices.keys()

    def agregar_arista(self, v, w, peso=1):
        """DOC: Agrega una arista no dirigida de peso 1 por default"""
        self.vertices[v][w] = peso
        if not self.dirigido:
            self.vertices[w][v] = peso

    def es_arista(self, v, w):
        '''DOC: Devuelve un tipo de dato bool si "w" es adyacente a "v"'''
        return w in self.vertices[v]

    def peso(self, v, w):
        """DOC: Devuelve el peso de la arista de "v" a "w"
        PRE: Recibe dos vertices validos
        POST: Devuelve el peso de la arista"""
        if self.es_arista(v, w):
            return self.vertices[v][w]

    def __iter__(self):
        """DOC: Devuelve un iterador de los vertices"""
        return iter(self.vertices)

    def __str__(self):
        """DOC: Devuelve una representacion en string del grafo"""
        return str(self.vertices)

    def __repr__(self):
        return str(self.vertices)

    def __len__(self):
        """DOC: Devuelve la cantidad de vertices del grafo"""
        return len(self.vertices)


visual_cortex = [
    (1, 4),
    (1, 14),
    (1, 15),
    (1, 16),
    (1, 17),
    (1, 18),
    (2, 7),
    (2, 82),
    (2, 152),
    (2, 153),
    (2, 154),
    (2, 155),
    (2, 156),
    (2, 157),
    (2, 158),
    (2, 159),
    (2, 160),
    (2, 161),
    (2, 162),
    (2, 163),
    (2, 164),
    (2, 165),
    (2, 166),
    (2, 167),
    (2, 168),
    (2, 169),
    (2, 170),
    (2, 171),
    (2, 172),
    (2, 173),
    (2, 174),
    (2, 175),
    (2, 176),
    (2, 177),
    (2, 184),
    (2, 185),
    (3, 102),
    (3, 176),
    (3, 177),
    (3, 178),
    (3, 179),
    (3, 180),
    (3, 181),
    (3, 182),
    (3, 183),
    (5, 1),
    (5, 36),
    (5, 37),
    (5, 38),
    (5, 39),
    (5, 40),
    (5, 41),
    (5, 42),
    (5, 43),
    (5, 44),
    (5, 45),
    (5, 46),
    (5, 47),
    (5, 48),
    (5, 49),
    (5, 50),
    (5, 51),
    (5, 52),
    (5, 53),
    (5, 54),
    (5, 55),
    (5, 56),
    (5, 57),
    (5, 58),
    (5, 59),
    (5, 60),
    (5, 82),
    (5, 102),
    (6, 59),
    (6, 60),
    (6, 61),
    (6, 62),
    (6, 63),
    (6, 64),
    (6, 65),
    (6, 66),
    (6, 67),
    (6, 68),
    (6, 69),
    (6, 70),
    (6, 71),
    (6, 72),
    (6, 73),
    (6, 74),
    (6, 75),
    (6, 76),
    (6, 77),
    (6, 78),
    (6, 79),
    (6, 80),
    (6, 81),
    (7, 3),
    (7, 149),
    (7, 184),
    (7, 185),
    (7, 186),
    (7, 187),
    (7, 188),
    (7, 189),
    (7, 190),
    (7, 191),
    (7, 192),
    (7, 193),
    (7, 194),
    (8, 149),
    (8, 150),
    (8, 151),
    (9, 35),
    (9, 82),
    (9, 83),
    (9, 84),
    (9, 85),
    (9, 86),
    (9, 87),
    (9, 88),
    (9, 89),
    (9, 90),
    (9, 91),
    (9, 92),
    (9, 93),
    (9, 94),
    (9, 95),
    (9, 96),
    (9, 97),
    (9, 98),
    (9, 99),
    (9, 100),
    (9, 101),
    (9, 102),
    (9, 103),
    (9, 104),
    (9, 105),
    (9, 147),
    (9, 148),
    (9, 149),
    (9, 152),
    (10, 36),
    (10, 103),
    (10, 104),
    (10, 105),
    (10, 106),
    (10, 107),
    (10, 108),
    (10, 109),
    (10, 110),
    (10, 111),
    (10, 112),
    (10, 113),
    (10, 114),
    (10, 115),
    (10, 116),
    (10, 117),
    (10, 118),
    (10, 119),
    (10, 120),
    (10, 121),
    (10, 122),
    (10, 123),
    (10, 124),
    (10, 125),
    (10, 126),
    (10, 127),
    (10, 128),
    (10, 129),
    (10, 130),
    (10, 131),
    (10, 149),
    (11, 35),
    (11, 129),
    (11, 130),
    (11, 131),
    (11, 132),
    (11, 133),
    (11, 134),
    (11, 135),
    (11, 136),
    (11, 137),
    (11, 138),
    (11, 139),
    (11, 140),
    (11, 141),
    (11, 142),
    (11, 143),
    (11, 144),
    (11, 145),
    (11, 146),
    (11, 147),
    (11, 148),
    (12, 1),
    (12, 4),
    (12, 18),
    (12, 19),
    (12, 20),
    (12, 21),
    (12, 22),
    (12, 23),
    (12, 24),
    (12, 25),
    (12, 26),
    (12, 27),
    (12, 28),
    (12, 29),
    (12, 30),
    (12, 31),
    (12, 32),
    (12, 33),
    (12, 34),
    (12, 35),
    (12, 82),
]
