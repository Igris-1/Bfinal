package main

import "strconv"

func countingSort(arr []int) int {
	count := make([]int, 10) // creo un arreglo con el rango acotado
	out := make([]int, len(arr)) // creo un arreglo del rango del arreglo original
	for i := 0; i < len(arr); i++ { // recorro el len() del arreglo original
		count[arr[i]]++ // aumento el contador del arreglo acotado
	}
	for i := 1; i < len(count); i++ { // recorro el len() del arreglo acotado
		count[i] += count[i-1] // sumo el contador del arreglo acotado
	}
	for i := 0; i < len(arr); i++ { // recorro el len() del arreglo original
		out[count[arr[i]]-1] = arr[i] // asigno el valor del arreglo original al arreglo acotado
		count[arr[i]]-- // disminuyo el contador del arreglo acotado
	}
	return arreglo_a_numero(out) // retorno el arreglo acotado convertido a numero
}

func arreglo_a_numero(arr []int) int {
	var num string
	for i := len(arr) - 1; i >= 0; i-- {
		num += strconv.Itoa(arr[i])
	}
	num2, _ := strconv.Atoi(num)
	return num2
}

func main() {
	arr := []int{1, 4, 1, 2, 7, 5, 2}
	println(countingSort(arr))
}