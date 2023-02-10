import heapq
from resources import cola as c
from resources import pila as p
from resources import grafo as g
from resources import union_find as union

# RECORRIDOS

"""
Breadth-First Search (BFS):
    - Complejidad: O(V + E)
    - Recorrido radial
    - Es maleable
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
    - Es maleable
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
    grados_e = grados_entrada(grafo)
    cola = c.Cola()

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
    visitados = set()
    pila = p.Pila()
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
            if dist[origen] + peso < dist.get(destino, float("inf")):
                cambio = True
                padre[destino] = origen
                dist[destino] = dist[origen] + peso
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
    for w in grafo.adyacentes(v):
        heapq.heappush(heap, (grafo.peso(v, w), (v, w)))
    for v in grafo:
        arbol.agregar_vertice(v)

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
    grupos = union.UnionFind(grafo.obtener_vertices())
    arbol = grafo.Grafo()
    heap = []
    visitados = set()

    for v in grafo:
        arbol.agregar_vertice(v)
        for w in grafo.adyacentes(v):
            if (v, w) not in visitados:
                heapq.heappush(heap, (grafo.peso(v, w), (v, w)))
        visitados.add(v)

    while heap:
        peso, (v, w) = heapq.heappop(heap)
        if grupos.find(v) == grupos.find(w):  # aca evitamos cerrar un ciclo
            continue
        arbol.agregar_arista(v, w, peso)
        grupos.union(v, w)
    return arbol


"""
Puntos de articulacion:
    - Complejidad: O(V + E)
    - Devuelve los puntos de articulacion de un grafo
    - Un punto de articulacion es un vertice que, si se elimina, separa el grafo en dos o mas componentes
    - Utiliza un recorrido DFS
"""


def puntos_articulacion(grafo):
    origen = grafo.obtener_vertices()[0]
    puntos = set()
    dfs_puntos(grafo, origen, {origen}, {origen: None}, {}, {}, puntos, True)
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
            dfs_puntos(
                grafo, w, visitados, padre, orden, mas_bajo, puntos, es_raiz=False
            )

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


"""
Ccomponentes Fuertemente Conexas:
    - Complejidad: O(V + E)
    - Devuelve las componentes fuertemente conexas de un grafo dirigido
"""


def cfcs(grafo):
    resultado = []
    visitados = set()
    pila = p.Pila()
    for v in grafo:
        if v not in visitados:
            _cfcs(grafo, v, visitados, {}, {}, pila, set(), resultado, 0)
    return resultado


def _cfcs(grafo, v, visitados, orden, mb, pila, apilados, cfcs, contador_global):
    orden[v] = mb[v] = contador_global[0]
    contador_global[0] += 1
    visitados.add(v)
    pila.apilar(v)
    apilados.add(v)

    for w in grafo.adyacentes(v):
        if w not in visitados:
            _cfcs(
                grafo,
                w,
                visitados,
                orden,
                mb,
                pila,
                apilados,
                cfcs,
                contador_global,
            )
        if w in apilados:
            # nos tenemos que fijar que este entre los apilados y que no estamos viendo un vertice visitado
            # en otro dfs hecho antes (no son parte de la misma cfc porque habrian sido visitados en la misma dfs)
            mb[v] == min(mb[v], mb[w])

    if orden[v] == mb[v]:
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
    for v in grafo:
        for w in grafo.adyacentes(v):
            grados[w] = grados.get(w, 0) + 1
    return grados


def pila_a_lista(pila):
    lista = []
    while pila:
        lista.append(pila.desapilar())
    return lista


def obtener_aristas(grafo):
    aristas = []
    for v in grafo:
        for w in grafo.adyacentes(v):
            aristas.append((v, w, grafo.peso(v, w)))
    return aristas
