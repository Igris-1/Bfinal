import heapq

'''
4. Escribir el Algoritmo de Kruskal para obtener el árbol de tendido mínimo
de un grafo no dirigido y pesado. Si al escribir el algoritmo, sabemos que
en el/los grafos que se va a aplicar los pesos fueran menores a 100,
¿cuál sería la complejidad de dicho algoritmo?
'''


def kruskal(grafo):
    grupos = union.UnionFind(grafo.obtener_vertices())
    arbol = grafo.Grafo()
    aristas = []
    visitados = set()

    for v in grafo.obtener_vertices():
        for w in grafo.adyacentes(v):
            if (v, w) not in visitados:
                heapq.heappush(aristas, (grafo.peso(v, w), (v, w)))
                visitados.add(v, w)
                visitados.add(w, v)
    while aristas:
        peso, (v, w) = heapq.heappop(aristas)
        if grupos.find(v) == grupos.find(w):
            continue
        arbol.agregar_aristas(v, w, peso)
        grupos.union(v, w)
    return arbol


'''
Complejidad del algoritmo de kruskal: O(e*log(e))
    - no afecta en nada que los pesos sean menores a 100 que 
    - los algoritmos de arboles de tendido minimo tomando en cuenta los pesos minimos,
    - la complejidad seria la misma
'''
