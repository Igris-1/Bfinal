import heapq

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




