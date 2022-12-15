import heapq
from resources import grafo
from resources import pila
from resource import union_find as union

# Dijkstra
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


# Bellman-Ford
def bellman_ford(grafo, origen):
    dist = {}
    padre = {}

    dist[origen] = 0
    padre[origen] = None
    aristas = grafo.obtener_aristas()

    for _ in range(len(grafo)):
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
            return None # hay un ciclo negativo
    return padre, dist


# Prim
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
        #aca evitamos cerrar un ciclo
        if w in visitados:
            continue
        #agregamos la arista al arbol
        arbol.agregar_arista(v, w, peso)
        visitados.add(w)

        for x in grafo.adyacentes(w):
            if x not in visitados:
                heapq.heappush(heap, (grafo.peso(v, w), (w, x)))
    return arbol


# Kruskal
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
        # aca evitamos cerrar un ciclo
        if grupos.find(v) == grupos.find(w):
            continue
        # agregamos la arista al arbol
        arbol.agregar_arista(v, w, peso)
        grupos.union(v, w)
    return arbol


# Puntos de articulación
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
            dfs_puntos(grafo, w, visitados, padre, orden, mas_bajo, puntos, es_raiz=False)

            if mas_bajo[w] >= orden[v] and not es_raiz:
                puntos.add(v)
            mas_bajo[v] = min(mas_bajo[v], orden[w])

        elif padre[v] != w:
            mas_bajo[v] = min(mas_bajo[v], orden[w])

    if es_raiz and hijos > 1:
        puntos.add(v)


# CFCs
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
            _cfcs(grafo, w, visitados, orden, mas_bajo, pila, apilados, cfcs, contador_global)
        if w in apilados:
            mas_bajo[v] == min(mas_bajo[v], mas_bajo[w])
    
    if orden[v] == mas_bajo[v]:
        nueva_cfc = []
        while True:
            w = pila.desapilar()
            apilados.remove(w)
            nueva_cfc.append(w)
            if w == v:
                break
        cfcs.append(nueva_cfc)