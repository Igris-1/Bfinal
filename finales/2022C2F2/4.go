package ejercicio4

import "strconv"

/*
4. Implementar un algoritmo que dado un arreglo de dígitos (0-9)
determine cuál es el número más grande que se puede formar con dichos dígitos.
*/

func seleccion(arr []int) int {
	for i := 0; i < len(arr); i++ {
		max := i
		for j := i + 1; j < len(arr); j++ {
			if arr[j] > arr[max] {
				max = j
			}
		}
		arr[i], arr[max] = arr[max], arr[i]
	}
	return arreglo_a_numero(arr)
}

func arreglo_a_numero(arr []int) int {
	var num string
	for _, v := range arr {
		num += strconv.Itoa(v)
	}
	num2, _ := strconv.Atoi(num)
	return num2
}
