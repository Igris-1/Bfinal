package ejercicio5

import (
	hash "material/resources/hash"
)

/*
5. Implementar un algoritmo que reciba un arreglo desordenado de enteros,
su largo (n) y un número K y determinar en O(n) si existe un par de elementos
en el arreglo que sumen exactamente K.
*/

func SumaK(arr []int, n, k int) bool {
	hash := hash.CrearHash[int, bool]()

	for i := 0; i < n; i++ {
		elemento := (k - arr[i])
		if hash.Pertenece(elemento) {
			return true
		}
		hash.Guardar(arr[i], true)
	}
	return false
}
