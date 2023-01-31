import heapq
from resources import union_find as union

def prim(grafo):
    v = grafo.vertice_aleatorio() # vertice inicial random
    visitados = set() # set de visitados
    heap = [] # heap de minimos
    visitados.add(v) # agrego el vertice inicial a visitados
    for w in grafo.adyacentes(v): # recorro los adyacentes de v
        heapq.heappush(heap, (grafo.peso(v, w), (v, w))) # agrego la arista v-w al heap
    arbol = grafo.Grafo() # creo un arbol 
    for v in grafo: # recorro el grafo
        arbol.agregar_vertice(v) # agrego los vertices al arbol

    while heap: # mientras el heap no este vacio
        peso, (v, w) = heapq.heappop(heap) # desencolo un vertice
        if w in visitados: # si w esta en visitados
            continue # salteo la iteracion
        arbol.agregar_vertice(v, w, peso) # agrego el vertice al arbol
        visitados.add(w) # agrego w a visitados
        for x in grafo.adyacentes(w): # recorro los adyacentes de w
            if x not in visitados: #si x no esta en visitados
                heapq.heappush(heap, (grafo.peso(w, x), (w, x))) # agrego la arista w-x al heap
    return arbol

def kruskal (grafo): 
    grupos = union.UnionFind(grafo) # creo los grupos
    arbol = grafo.Grafo() # creo un arbol
    heap = [] # creo un heap
    visitados = set() # set de visitados
    for v in grafo: # recorro los vertices
        for w in grafo.adyacentes(w): # recorro los adyancetes de v
            if (v, w) not in visitados: # si la arista v-w no esta en visitados
                heapq.heappush(heap, (grafo.peso(v, w), (v, w))) # agrego la arista v-w al heap
                visitados.add((v, w)) # agrego la arista v-w a visitados
                visitados.add((w, v)) # agrego la arista w-v a visitados
    while heap: # mientras el heap no este vacio
        peso, (v, w) = heapq.heappop(heap) # desencolo una arista
        if grupos.find(v) == grupos.find(w): # si el grupo de v es igual al grupo de w
            continue # salteo una iteracion para no cerrar ciclos
        arbol.agregar_arista(v, w, peso) # agrego la arista v-w al arbol
        grupos.union(v, w) # unifico los grupos de v y w
    return arbol # devuelvo el arbol de tendido minimo