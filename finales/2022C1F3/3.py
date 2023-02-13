"""Implementar el Algoritmo de Kruskal para obtener el Árbol de Tendido Mínimo de un grafo pesado. Aplicar dicho
algoritmo al grafo del dorso. Responder: ¿Para qué se utiliza la estructura Union-Find (o conjunto disjunto) en este
algoritmo? ¿qué problema viene a resolver?"""



def kruskal(grafo):
    grupos = UnionFind(grafo.obtener_vertices())
    arbol = Grafo()
    heap = []
    visitados = set()
    datos_kruskal(grafo, visitados, heap, arbol)

    while heap:
        peso, (v, w) = heapq.heappop(heap)
        if grupos.find(v) == grupos.find(w):
            continue
        arbol.agregar_arista(v, w, peso)
    return arbol

def datos_kruskal(grafo, visitados, heap, arbol):
    for v in grafo:
        arbol.agregar(v)
        for w in grafo.adyacentes(v):
            if (v, w) not in visitados:
                heapq.heappush(heap, (grafo.peso(v, w), (v, w)))
        visitados.add(v)

'''Kruskal
complejidad O(E*log(V))
Utiliza la estructura Union-Find para unir los vertices
que no estan en el mismo grupo con una complejidad de
O(Ackerman^-1), y asi poder formar el arbol
de tendido minimo de una forma mas eficiente'''