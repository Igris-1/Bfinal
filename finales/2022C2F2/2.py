'''
2. Implementar un algoritmo que reciba un Grafo con características 
de árbol (no árbol binario, sino referido a árbol de teoría de grafos) 
y devuelva una lista con los puntos de articulación de dicho árbol. 
Indicar y justificar la complejidad del algoritmo implementado. 
Importante: aprovechar las características del grafo que se recibe 
para que la solución sea lo más simple posible.
'''

def ptos_articulacion(grafo):
    origen = grafo.obtener_vertices()[0]
    puntos = set()
    dfs_ptos(grafo, origen, {origen}, {origen: None}, {}, puntos, True)
    return puntos

def dfs_ptos(grafo, v, visitados, padre, orden, mb, puntos, es_raiz):
	hijos = 0
	mb[v] = orden[v]

	for w in grafo.adyacentes(v):
		if w not in visitados:
			hijos+=1
			orden[w] = orden[v] + 1
			padre[w] = v
			visitados.add(w)
			dfs_ptos(grafo, w, visitados, padre, orden, mb, puntos, es_raiz=False)
			if mb[w] >= orden[v] and not es_raiz:
				puntos.add(v)
			mb[v] = min(mb[v], orden[w])
		elif padre[v] != w:
			mb[v] = min(mb[v], orden[w])
	if es_raiz and hijos > 1:
		puntos.add(v)

# Complejidad: O(V + E)
#	por ser un recorrido DFS