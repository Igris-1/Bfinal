package ejercicio

import (
	heap "material/resources/heap"
)

/*Implementar un algoritmo que reciba un arreglo de n números, y un número k,
y devuelva los k números dentro del arreglo cuya suma sería la máxima
(entre todos los posibles subconjuntos de k elementos de dicho arreglo).
La solución debe ser mejor que O(n log n) si k << n. Indicar y justificar
la complejidad de la función implementada.*/

func KmaxSum(arr []int, k int) []int {
	heap := heap.CrearHeapArr(arr, funcionDeComparacion)
	res := make([]int, k)
	for i := 0; i < k; i++ {
		res[i] = heap.Desencolar()
	}
	return res
}

func funcionDeComparacion(a, b int) int { return a - b }

/*Heapify del arr O()*/