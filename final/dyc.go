package main

// las estrellitas demarcan la dificultad de los ejercicios,
// 4 y 5 estrellas son ejercicios de parciales / finales

/*
DATOS: D&C Rules
	- Teorema Maestro: T(n) = AT(n/B) + O(n^C):
		- A: cantidad de llamados recursivos
		- B: proporsion del llamado recursivo
		- C: exponente de la complejidad de todo lo no recursivo

	- Complejidad de las funciones:
		- logB(A) < C => T(n) = O(n^C)
		- logB(A) = C => T(n) = O(n^C * log(n))
		- logB(A) > C => T(n) = O(n^logB(A))
*/

/*
11) (★★★) Se tiene un arreglo tal que [1, 1, 1, ..., 0, 0, ...] (es decir, unos seguidos de ceros).

Se pide:
  - a) una función de orden O(log(n)) que encuentre el índice del primer 0.
    Si no hay ningún 0 (solo hay unos), debe devolver -1.
  - b) demostrar con el Teorema Maestro que la función es, en efecto, O(log(n)).

Ejemplos:

	[1, 1, 0, 0, 0] →  2
	[0, 0, 0, 0, 0] →  0
	[1, 1, 1, 1, 1] → -1
*/
func indiceCero(arr []int) int {
	return _indice(arr, 0, len(arr)-1)
}

func _indice(arr []int, inicio, fin int) int {
	if inicio == fin {
		if arr[inicio] == 0 {
			return inicio
		} else {
			return -1
		}
	}
	medio := (inicio + fin) / 2
	if arr[medio] == 0 && arr[medio-1] == 1 {
		return medio
	}
	if arr[medio] == 1 {
		return _indice(arr, medio+1, fin)
	} else {
		return _indice(arr, inicio, medio-1)
	}
}

/*
Complejidad: T(n) = 1T(n/2) + O(n^0)
	- A: 1
	- B: 2
	- C: 0
	- logB(A) = log2(1) = 0 = C => O(n^C * log(n)) = O(log(n))
*/

/*
12) (★★★★) Implementar un algoritmo que, por división y conquista, permita obtener
la parte entera de la raíz cuadrada de un número n,
en tiempo log(n).

Por ejemplo, para n = 10 debe devolver 3, y para n = 25 debe devolver 5.
*/
func raizParteEntera(n int) int {
	return _parteEntera(n, 0, n)
}

//TODO: terminar
func _parteEntera(n, inicio, fin int) int {
	if inicio > fin {
		return -1
	}
	medio := (inicio + fin) / 2

}



func main() {
	// funcion de testeo
}
