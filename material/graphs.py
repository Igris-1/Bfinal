from resource import union_find as union
from resources import pila
from resources import cola
from resources import grafo
import heapq


# RECORRIDOS

'''
Breadth-First Search (BFS):
    - Complejidad: O(V + E)
    - Recorrido radial
    - Es maleable
'''


def bfs(grafo):
    visitados = set()
    for v in grafo.obtener_vertices():
        if v not in visitados:
            _bfs(grafo, v, {})


def _bfs(grafo, origen, visitados):
    cola = cola.Cola()
    cola.encolar(origen)

    while cola:
        v = cola.desencolar()
        for w in grafo.adyacentes(v):
            if w not in visitados:
                visitados[v] = True
                cola.encolar(w)


'''
Depth-First Search (DFS):
    - Complejidad: O(V + E)
    - Recorrido en profundidad
    - Es maleable
'''


def dfs(grafo):
    visitados = set()
    for v in grafo.obtener_vertices():
        if v not in visitados:
            visitados.add(v)
            _dfs(grafo, v, visitados)


def _dfs(grafo, v, visitados):
    for w in grafo.adyacentes(v):
        if w not in visitados:
            visitados.add(w)
            _dfs(grafo, w, visitados)


# ORDEN TOPOLOGICO

'''
Orden topologico tipo BFS:
    - Complejidad: O(V + E)
    - Utiliza una cola como TDA auxiliar
    - Recorrido radial que toma en cuenta los grados de entrada
    - para grafos dirigidos
'''


def orden_bfs(grafo):
    orden = []
    grados_e = grados_entrada(grafo)
    cola = cola.Cola()

    for v in grafo.obtener_vertices():
        if grados_e[v] == 0:
            cola.encolar(v)

    while cola:
        v = cola.desencolar()
        orden.append(v)
        for w in grafo.adyacentes(v):
            grados_e[w] -= 1
            if grados_e[w] == 0:
                cola.encolar(w)

    if len(orden) != len(grafo.obtener_vertices()):
        return None
    return orden


'''
Orden topologico tipo DFS:
    - Complejidad: O(V + E)
    - Utiliza una pila como TDA auxiliar
    - Recorrido en profundidad que toma en cuenta los visitados
    - para grafos dirigidos
'''


def orden_dfs(grafo):
    visitados = set()
    pila = pila.Pila()
    for v in grafo.obtener_vertices():
        if v not in visitados:
            visitados.add(v)
            _orden_dfs(grafo, v, visitados, pila)
    return pila_a_lista(pila)


def _orden_dfs(grafo, v, visitados, pila):
    for w in grafo.adyacentes(v):
        if w not in visitados:
            visitados.add(w)
            _orden_dfs(grafo, w, visitados, pila)
    pila.apilar(v)


# CAMINOS MINIMOS

'''
Dijkstra:
    - Complejidad: O(E log V)
    - Implementado con un heap de minimos
    - No sirve para grafos con pesos negativos ya que se genera un ciclo infinito
    - Si el grafo es conexo, se puede usar para encontrar el camino minimo entre todos los pares de vertices
'''


def dijkstra(grafo, origen):
    dist = {}
    padre = {}
    heap = []

    dist[origen] = 0
    padre[origen] = None
    heapq.heappush(heap, (0, origen))

    while heap:
        _, v = heapq.heappop(heap)
        # si tuviera un destino pasado como parametro
        # if v == destino:
        #    return padre, dist
        for w in grafo.adyacentes():
            distacia_por_v = dist.get(v, 0) + grafo.peso(v, w)
            if distacia_por_v < dist.get(w, 0):
                dist[w] = distacia_por_v
                padre[w] = v
                heapq.heappush(heap, (dist[w], w))
    # si tuviera un destino pasado como parametro y no lo encontre
    # return None, None
    return padre, dist


'''
Bellman-Ford:
    - Complejidad: O(V*E)
    - Solo para grafos dirigidos
    - Es realmente lento, pero sirve para grafos con pesos negativos
    - Itera V veces + 1
    - Si se mejora la ultima iteracion quiere decir que hay un ciclo negativo
'''


def bellman_ford(grafo, origen):
    dist = {}
    padre = {}

    dist[origen] = 0
    padre[origen] = None
    aristas = grafo.obtener_aristas()  # O(V + E)

    for _ in range(len(grafo)):  # O(V * E)
        cambio = None
        for origen, destino, peso in aristas:
            if dist.get(origen, 0) + peso < dist.get(destino, 0):
                cambio = True
                padre[destino] = origen
                dist[destino] = dist[origen] + peso
        # si no hubo cambios en la iteracion, corto
        if not cambio:
            break

    # si no hubo cambios en la iteracion, corto
    if not cambio:
        return padre, dist

    # si hubo cambios en la iteracion, verifico si hay ciclos negativos
    for v, w, peso in aristas:
        if dist[v] + peso < dist[w]:
            return None  # hay un ciclo negativo
    return padre, dist


# ARBOL DE TENDIDO MINIMO

'''
Prim:
    - Complejidad: O(E log(V))
    - Implementado con un heap de minimos
    - Devuelve un arbol cuya suma de pesos es minima
'''


def prim(grafo):
    v = grafo.obtener_vertices()[0]
    visitados = set()
    heap = []

    visitados.add(v)

    for w in grafo.adyacentes(v):
        heapq.heappush(heap, (grafo.peso(v, w), (v, w)))

    arbol = grafo.Grafo()
    for v in grafo.obtener_vertices():
        arbol.agregar_vertice(v)

    while heap:
        peso, (v, w) = heapq.heappop(heap)
        if w in visitados:  # aca evitamos cerrar un ciclo
            continue
        arbol.agregar_arista(v, w, peso)
        visitados.add(w)

        for x in grafo.adyacentes(w):
            if x not in visitados:
                heapq.heappush(heap, (grafo.peso(v, w), (w, x)))
    return arbol


'''
Kruskal:
    - Complejidad: O(E log(V))
    - Implementado con un heap de minimos
    - Devuelve un arbol cuya suma de pesos es minima
'''


def kruskal(grafo):
    grupos = union.UnionFind(grafo.obtener_vertices())
    arbol = grafo.Grafo()
    aristas = []
    visitados = set()

    for v in grafo.adyacentes(v):
        for w in grafo.adyacentes(w):
            if (v, w) not in visitados:
                heapq.heappush(aristas, (grafo.peso(v, w), (v, w)))
                visitados.add(v, w)
                visitados.add(w, v)

    while aristas:
        peso, (v, w) = heapq.heappop(aristas)
        if grupos.find(v) == grupos.find(w):  # aca evitamos cerrar un ciclo
            continue
        arbol.agregar_arista(v, w, peso)
        grupos.union(v, w)
    return arbol


'''
Puntos de articulacion:
    - Complejidad: O(V + E)
    - Devuelve los puntos de articulacion de un grafo
    - Un punto de articulacion es un vertice que, si se elimina, separa el grafo en dos o mas componentes
    - Utiliza un recorrido DFS
'''


def puntos_articulacion(grafo):
    origen = grafo.obtener_vertices()[0]
    puntos = set()
    dfs_puntos(grafo, origen, {origen}, {origen: None}, {}, puntos, True)
    return puntos


def dfs_puntos(grafo, v, visitados, padre, orden, mas_bajo, puntos, es_raiz):
    hijos = 0
    mas_bajo[v] = orden[v]

    for w in grafo.adyacentes(v):
        if w not in visitados:
            hijos += 1
            orden[w] = orden[v] + 1
            padre[w] = v
            visitados.add(w)
            dfs_puntos(grafo, w, visitados, padre, orden,
                       mas_bajo, puntos, es_raiz=False)

            if mas_bajo[w] >= orden[v] and not es_raiz:
                # No hubo forma de pasar por arriba a este vertice, es punto de articulacion
                # se podria agregar como condicion "and v not in ptos" (ya que podria darse por mas de una rama)
                puntos.add(v)
            # Al volver me quedo con que puedo ir tan arriba como mi hijo, si es que me supera
            mas_bajo[v] = min(mas_bajo[v], orden[w])

        elif padre[v] != w:
            # evitamos considerar la arista con el padre como una de retorno
            # Si es uno ya visitado, significa que puedo subir (si es que no podia ya ir mas arriba)
            mas_bajo[v] = min(mas_bajo[v], orden[w])

    if es_raiz and hijos > 1:
        puntos.add(v)


'''
Ccomponentes Fuertemente Conexas:
    - Complejidad: O(V + E)
    - Devuelve las componentes fuertemente conexas de un grafo dirigido
'''


def cfcs(grafo):
    resultado = []
    visitados = set()
    p = pila.Pila()
    for v in grafo:
        if v not in visitados:
            _cfcs(grafo, v, visitados, {}, {}, p, set(), resultado, 0)
    return resultado


def _cfcs(grafo, v, visitados, orden, mas_bajo, pila, apilados, cfcs, contador_global):
    orden[v] = mas_bajo[v] = contador_global[0]
    contador_global[0] += 1
    visitados.add(v)
    pila.apilar(v)
    apilados.add(v)

    for w in grafo.adyacentes(v):
        if w not in visitados:
            _cfcs(grafo, w, visitados, orden, mas_bajo,
                  pila, apilados, cfcs, contador_global)
        if w in apilados:
            # nos tenemos que fijar que este entre los apilados y que no estamos viendo un vertice visitado
            # en otro dfs hecho antes (no son parte de la misma cfc porque habrian sido visitados en la misma dfs)
            mas_bajo[v] == min(mas_bajo[v], mas_bajo[w])

    if orden[v] == mas_bajo[v]:
        # se cumple condicion de cierre de CFC, armo la cfc
        # y saco los elementos de la pila
        nueva_cfc = []
        while True:
            w = pila.desapilar()
            apilados.remove(w)
            nueva_cfc.append(w)
            if w == v:
                break
        cfcs.append(nueva_cfc)


# ALGORITMOS AUXILIARES
def grados_entrada(grafo):
    grados = {}
    for v in grafo.obtener_vertices():
        for w in grafo.adyacentes(v):
            grados[w] = grados.get(w, 0) + 1
    return grados


def pila_a_lista(pila):
    lista = []
    while pila:
        lista.append(pila.desapilar())
    return lista
