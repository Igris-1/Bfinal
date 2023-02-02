package ejercicio

/*Implementar en Go un algoritmo que reciba un árbol binario y nos devuelva el 
máximo de dicho árbol (no ABB). Indicar y justificar la complejidad del algoritmo 
implementado. A fines del ejercicio, la estructura del árbol es:*/

type ab struct{
	izq *ab
	der *ab
	dato int
}

func maximo(a *ab) int {
	if a == nil {
		return -1
	}
	izq := a.izq.dato
	der := a.der.dato

	if izq > der {
		return izq
	} else {
		return der
	}
}

// Complejidad: O(n) ya que recorre todo el arbol en busca del maximo
