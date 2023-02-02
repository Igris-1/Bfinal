package ejercicio

import "strconv"

/*
4. Implementar un algoritmo que dado un arreglo de dígitos (0-9)
determine cuál es el número más grande que se puede formar con dichos dígitos.
*/

func countingSort(arr []int) int {
	count := make([]int, 10)
	out := make([]int, len(arr))
	for i := 0; i < len(arr); i++ {
		count[arr[i]]++
	}
	for i := 1; i < len(count); i++ {
		count[i] += count[i-1]
	}
	for i := len(arr) - 1; i >= 0; i-- {
		out[count[arr[i]]-1] = arr[i]
		count[arr[i]]--
	}
	return arreglo_a_numero(out)
}

func arreglo_a_numero(arr []int) int {
	var num string
	for i := len(arr) - 1; i >= 0; i-- {
		num += strconv.Itoa(arr[i])
	}
	num2, _ := strconv.Atoi(num)
	return num2
}
