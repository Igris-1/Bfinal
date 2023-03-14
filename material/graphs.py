import heapq
from resources import cola as c
from resources import pila as p
from resources import grafo as g
from resources import union_find as union

# RECORRIDOS cambios

"""
Breadth-First Search (BFS):
    - Complejidad: O(V + E)
    - Recorrido radial
    - Se puede modificar respecto a las necesidades del problema
"""


def bfs0(grafo):
    """Recorre todas las componentes conexas del grafo"""
    visitados = {}
    for v in grafo:
        if v not in visitados:
            _bfs0(grafo, v, visitados)


def _bfs0(grafo, v, visitados):
    cola = c.Cola()
    cola.encolar(v)

    while not cola.esta_vacia():
        v = cola.desencolar()
        for w in grafo.adyacentes(v):
            if w not in visitados:
                cola.encolar(w)
        visitados[v] = True


def bfs1(grafo, v):
    """DOC: Recorre una sola componente conexa del grafo, desde
    un vertice origen"""
    visitados = {}
    cola = c.Cola()
    cola.encolar(v)

    while not cola.esta_vacia():
        v = cola.desencolar()
        for w in grafo.adyacentes(v):
            if w not in visitados:
                cola.encolar(w)
        visitados[v] = True


"""
Depth-First Search (DFS):
    - Complejidad: O(V + E)
    - Recorrido en profundidad
    - Se puede modificar respecto a las necesidades del problema
"""


def dfs0(grafo):
    """Recorre todas las componentes conexas del grafo"""
    visitados = set()
    for v in grafo:
        if v not in visitados:
            visitados.add(v)
            _dfs(grafo, v, visitados)


def _dfs(grafo, v, visitados):
    for w in grafo.adyacentes(v):
        if w not in visitados:
            visitados.add(w)
            _dfs(grafo, w, visitados)


def dfs1(grafo):
    """DOC: Recorre una sola componente conexa del grafo desde
    un vertice aleatorio"""
    visitados = set()
    v = grafo.vertice_aleatorio()
    visitados.add(v)

    for w in grafo.adyacentes(v):
        if w not in visitados:
            visitados.add(w)
            _dfs(grafo, w, visitados)


# ORDEN TOPOLOGICO


"""
Orden topologico tipo BFS:
    - Complejidad: O(V + E)
    - Utiliza una cola como TDA auxiliar
    - Recorrido radial que toma en cuenta los grados de entrada
    - para grafos dirigidos
"""


def orden_bfs(grafo):
    """DOC: https://es.wikipedia.org/wiki/Ordenamiento_topol%C3%B3gico
    https://es.wikipedia.org/wiki/B%C3%BAsqueda_en_anchura
    PRE: Recibe un grafo
    POST: Devuelve un orden topologico de tipo BFS
    """
    orden = []
    grados_e = {}
    cola = c.Cola()

    for v in grafo:
        for w in grafo.adyacentes(v):
            grados_e[w] = grados_e.get(w, 0) + 1

    for v in grafo:
        if grados_e[v] == 0:
            cola.encolar(v)

    while not cola.esta_vacia():
        v = cola.desencolar()
        orden.append(v)
        for w in grafo.adyacentes(v):
            grados_e[w] -= 1
            if grados_e[w] == 0:
                cola.encolar(w)

    if len(orden) != len(grafo):
        return None
    return orden


"""
Orden topologico tipo DFS:
    - Complejidad: O(V + E)
    - Utiliza una pila como TDA auxiliar
    - Recorrido en profundidad que toma en cuenta los visitados
    - para grafos dirigidos
"""


def orden_dfs(grafo):
    """DOC: https://es.wikipedia.org/wiki/Ordenamiento_topol%C3%B3gico
    https://es.wikipedia.org/wiki/B%C3%BAsqueda_en_profundidad
    PRE: Recibe un grafo
    POST: devuelve un orden topologico de tipo DFS"""
    orden = []
    visitados = set()
    pila = p.Pila()

    for v in grafo:
        if v not in visitados:
            visitados.add(v)
            _orden_dfs(grafo, v, visitados, pila)

    while not pila.esta_vacia():
        orden.append(pila.desapilar())
    return orden


def _orden_dfs(grafo, v, visitados, pila):
    for w in grafo.adyacentes(v):
        if w not in visitados:
            visitados.add(w)
            _orden_dfs(grafo, w, visitados, pila)
    pila.apilar(v)


# CAMINOS MINIMOS

"""
Dijkstra:
    - Complejidad: O(E*log(V))
    - Implementado con un heap de minimos
    - No sirve para grafos con pesos negativos ya que se genera un ciclo infinito
    - Si el grafo es conexo, se puede usar para encontrar el camino minimo entre todos los pares de vertices
"""


def dijkstra(grafo, origen):
    """DOC: https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
    PRE: Recibe un grafo y un origen
    POST: Devuelve los caminos minimos desde el origen a todos los vertices,
    un diccionario de padres y distancias"""
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
        for w in grafo.adyacentes(v):
            dist_por_v = dist[v] + grafo.peso(v, w)
            if dist_por_v < dist.get(w, float("inf")):
                dist[w] = dist_por_v
                padre[w] = v
                heapq.heappush(heap, (dist[w], w))
    # si tuviera un destino pasado como parametro y no lo encontre
    # return None, None
    return padre, dist


"""
Bellman-Ford:
    - Complejidad: O(V*E)
    - Solo para grafos dirigidos (sirve en grafos no dirigidos pero en esos casos hay soluciones mas eficientes)
    - Es realmente lento, pero sirve para grafos con pesos negativos
    - Itera V + 1 veces
    - Si se mejora la ultima iteracion quiere decir que hay un ciclo negativo
"""


def bellman_ford(grafo, origen):
    """DOC: https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm
    PRE: Recibe un grafo y un origen
    POST: Devuelve los caminos minimos desde el origen a todos los vertices,
    un diccionario de padres y distancias, caso contrario None"""
    dist = {}
    padre = {}

    dist[origen] = 0
    padre[origen] = None
    aristas = obtener_aristas(grafo)  # O(V + E)

    cambio = None
    for _ in range(len(grafo)):  # O(V * E)
        for origen, destino, peso in aristas:
            if dist.get(origen, float("inf")) + peso < dist.get(destino, float("inf")):
                cambio = True
                dist[destino] = dist[origen] + peso
                padre[destino] = origen
        # si no hubo cambios en la iteracion, corto
        if not cambio:
            break
    # si no hubo cambios en la iteracion, corto
    if not cambio:
        return None
    # si hubo cambios en la iteracion, verifico si hay ciclos negativos
    for v, w, peso in aristas:
        if dist[v] + peso < dist[w]:
            return None  # hay un ciclo negativo
    return padre, dist


# ARBOL DE TENDIDO MINIMO

"""
Prim:
    - Complejidad: O(E*log(V))
    - Implementado con un heap de minimos
    - Devuelve un arbol cuya suma de pesos es minima
"""


def prim(grafo):
    """DOC: https://es.wikipedia.org/wiki/Algoritmo_de_Prim
    PRE: REcibe un grafo
    POST: Devuelve un arbol de tendido minimo"""
    v = grafo.vertice_aleatorio()
    visitados = set()
    arbol = g.Grafo()
    heap = []

    visitados.add(v)
    for v in grafo:
        arbol.agregar_vertice(v)
    for w in grafo.adyacentes(v):
        heapq.heappush(heap, (grafo.peso(v, w), (v, w)))

    while heap:
        peso, (v, w) = heapq.heappop(heap)
        if w in visitados:  # aca evitamos cerrar un ciclo
            continue
        arbol.agregar_arista(v, w, peso)
        visitados.add(w)

        for x in grafo.adyacentes(w):
            if x not in visitados:
                heapq.heappush(heap, (grafo.peso(w, x), (w, x)))
    return arbol


"""
Kruskal:
    - Complejidad: O(E*log(V))
    - Implementado con un heap de minimos
    - Devuelve un arbol cuya suma de pesos es minima
"""


def kruskal(grafo):
    """DOC: https://es.wikipedia.org/wiki/Algoritmo_de_Kruskal
    PRE: REcibe un grafo
    POST: Devuelve un arbol de tendido minimo"""
    visitados = set()
    arbol = grafo.Grafo()
    grupos = union.UnionFind(grafo.obtener_vertices())
    heap = []

    for v in grafo:
        arbol.agregar_vertice(v)
        for w in grafo.adyacentes(v):
            if (v, w) not in visitados:  # evitamos repetir aristas
                heapq.heappush(heap, (grafo.peso(v, w), (v, w)))
                visitados.add((v, w))
                visitados.add((w, v))

    while heap:
        peso, (v, w) = heapq.heappop(heap)
        if grupos.find(v) == grupos.find(w):  # evitamos cerrar un ciclo
            continue
        arbol.agregar_arista(v, w, peso)
        grupos.union(v, w)
    return arbol


"""
Puntos de articulacion:
    - Complejidad: O(V + E)
    - Devuelve los puntos de articulacion de un grafo no dirigido
    - Un punto de articulacion es un vertice que, si se elimina, separa el grafo en dos o mas componentes
    - Utiliza un recorrido DFS
"""


def puntos_de_articulacion(grafo):
    v = grafo.vertice_aleatorio()
    visitados = set()
    padre = {}
    orden = {}
    mb = {}
    puntos = set()
    raiz = True

    padre[v] = None
    orden[v] = 0
    puntos_dfs(grafo, v, visitados, padre, orden, mb, puntos, raiz)
    # puntos_dfs(grafo, v, {v}, {v: None}, {}, {}, puntos, True)
    return puntos


def puntos_dfs(grafo, v, visitados, padre, orden, mb, puntos, raiz):
    hijos = 0
    mb[v] = orden[v]

    for w in grafo.adyacenes(v):
        if w not in visitados:
            visitados.add(w)
            orden[w] = orden[v] + 1
            padre[w] = v
            hijos += 1
            puntos_dfs(grafo, w, visitados, padre, orden, mb, puntos, raiz=False)

            if mb[w] >= orden[v] and not raiz and v not in puntos:
                # No hubo forma de pasar por arriba a este vertice, es punto de articulacion
                puntos.add(v)
            # Al volver me quedo con que puedo ir tan arriba como mi hijo, si es que me supera
            mb[v] = min(mb[v], orden[w])
        elif padre[v] != w:
            # Evitamos considerar la arista con el padre como una de retorno
            # Si es uno ya visitado, significa que puedo subir (si es que no podia ya ir mas arriba)
            mb[v] = min(mb[v], orden[w])
    if raiz and hijos > 1:
        puntos.add(v)


"""
Ccomponentes Fuertemente Conexas:
    - Complejidad: O(V + E)
    - Devuelve las componentes fuertemente conexas de un grafo dirigido
"""


def cfcs(grafo):
    visitados = set()
    orden = {}
    mb = {}
    pila = p.Pila()
    apilados = set()
    cfcs = []
    contador_global = 0

    for v in grafo:
        if v not in visitados:
            _cfcs(grafo, v, visitados, orden, mb, pila, apilados, cfcs, contador_global)
            # _cfcs(grafo, v, visitados, {}, {}, pila, set(), cfcs, contador_global)
    return cfcs


def _cfcs(grafo, v, visitados, orden, mb, pila, apilados, cfcs, contador_global):
    orden[v] = mb[v] = contador_global
    contador_global += 1
    visitados.add(v)
    pila.apilar(v)
    apilados.add(v)

    for w in grafo.adyacentes(v):
        if w not in visitados:
            _cfcs(grafo, w, visitados, orden, mb, pila, apilados, cfcs, contador_global)
            if w in apilados:
                # nos tenemos que fijar que este entre los apilados y que no estamos viendo un vertice visitado
                # en otro dfs hecho antes (no son parte de la misma cfc porque habrian sido visitados en la misma dfs)
                mb[v] = min(mb[v], mb[w])
    if orden[v] == mb[v]:
        # se cumple condicion de cierre de CFC, armo la cfc y saco los elementos de la pila
        nueva_cfc = []
        while True:
            w = pila.desapilar()
            apilados.remove(w)
            nueva_cfc.append(w)
            if w == v:
                break
        cfcs.append(nueva_cfc)


# ALGORITMOS AUXILIARES
def obtener_aristas(grafo):
    aristas = []
    for v in grafo:
        for w in grafo.adyacentes(v):
            aristas.append((v, w, grafo.peso(v, w)))
    return aristas
