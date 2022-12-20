"""
2.  Implementar una función que reciba un grafo no dirigido y determine 
	si el mismo no tiene ciclos de una cantidad impar
	de vértices. Indicar y justificar la complejidad de la función.
"""


def ciclos_par_dfs(grafo):
    visitados = set()
    for v in grafo:
        if v not in visitados:
            visitados.add(v)
            if dfs(grafo, v, visitados, {}):
                return False
    return True


def dfs(grafo, v, visitados, padre):
    for w in grafo.adyacentes(v):
        if w in visitados:
            if w != padre[v]:
                if ciclo_impar(padre, w, v):
                    return True
        else:
            visitados.add(w)
            padre[w] = v
            dfs(grafo, w, visitados, padre)
    return False


def ciclo_impar(padre, inicio, fin):
    v = fin
    cant = 1
    while v != inicio:
        cant += 1
        v = padre[v]
    return cant % 2 == 0


# Complejidad:
# - Recorrido DFS: O(V + E)
# - Ciclo impar: O(V)

# Complejidad final: O(V + E)


'''
Mismo algoritmo pero implementado con un BFS
'''


def ciclos_par_bfs(grafo):
    visitados = {}
    for v in grafo:
        if v not in visitados:
            if bfs(grafo, v, visitados, {}):
                return False
    return True


def bfs(grafo, v, visitados, padre):
    cola = Cola()
    cola.encolar(v)
    visitados[v] = True
    padre[v] = None

    while not cola.esta_vacia():
        v = cola.desencolar()
        for w in grafo.adyacentes(v):
            if w in visitados:
                if w != padre[v]:
                    if ciclo_impar(padre, w, v):
                        return True
            else:
                visitados[v] = True
                padre[w] = v
                cola.encolar(w)
    return False

# Complejidad:
# - Recorrido BFS: O(V + E)
# - Ciclo impar: O(V)

# Complejidad final: O(V + E)
