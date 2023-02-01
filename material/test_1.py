import heapq
from resources import union_find as union
from resources import grafo as graf


def kruskal(grafo):
    grupos = union.UnionFind(grafo.obtener_vertices())
    arbol = graf.Grafo()
    peso_total = 0
    heap = []
    visitados = set()

    datos(grafo, visitados, heap, arbol)

    # for v in grafo:
    #     arbol.agregar_vertice(v)
    #     for w in grafo.adyacentes(v):
    #         if (v, w) not in visitados:
    #             heapq.heappush(heap, (grafo.peso(v, w), (v, w)))
    #     visitados.add(v)

    while heap:
        peso, (v, w) = heapq.heappop(heap)
        if grupos.find(v) == grupos.find(w):  # aca evitamos cerrar un ciclo
            continue
        arbol.agregar_arista(v, w, peso)
        peso_total += peso
        grupos.union(v, w)
    return arbol, peso_total


def datos(grafo, visitados, heap, arbol):
    for v in grafo:
        arbol.agregar_vertice(v)
        for w in grafo.adyacentes(v):
            if (v, w) not in visitados:
                heapq.heappush(heap, (grafo.peso(v, w), (v, w)))
        visitados.add(v)


g = graf.Grafo()

g.agregar_vertice('a')
g.agregar_vertice('b')
g.agregar_vertice('c')
g.agregar_vertice('d')
g.agregar_vertice('e')
g.agregar_vertice('f')

g.agregar_arista('e', 'f', 6)
g.agregar_arista('e', 'a', 8)
g.agregar_arista('e', 'c', 2)
g.agregar_arista('e', 'd', 4)
g.agregar_arista('a', 'c', 6)
g.agregar_arista('a', 'b', 5)
g.agregar_arista('a', 'f', 2)
g.agregar_arista('c', 'd', 3)
g.agregar_arista('c', 'b', 6)
g.agregar_arista('d', 'b', 8)
g.agregar_arista('b', 'f', 7)

arbol, peso = kruskal(g)
print(arbol)
print(peso)
