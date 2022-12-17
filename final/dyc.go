package main

import "fmt"

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

// TODO: terminar
func _parteEntera(n, inicio, fin int) int {
	if inicio > fin {
		return -1
	}
	medio := (inicio + fin) / 2
	if medio*medio <= n && (medio+1)*(medio+1) > n {
		return medio
	}
	if medio*medio > n {
		return _parteEntera(n, inicio, medio)
	} else {
		return _parteEntera(n, medio+1, fin)
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
13) (★★★) Se tiene un arreglo de N >= 3 elementos en forma de pico,
esto es: estrictamente creciente hasta una determinada posición p,
y estrictamente decreciente a partir de ella (con 0 <= p < N-1).
Por ejemplo, en el arreglo [1, 2, 3, 1, 0, -2] la posición del pico es p = 2
*/

func indicePico(arr []int) int {
	return _indicePico(arr, 0, len(arr)-1)
}

func _indicePico(arr []int, inicio, fin int) int {
	if inicio == fin {
		return -1
	}
	medio := (inicio + fin) / 2
	if arr[medio] > arr[medio-1] && arr[medio] > arr[medio+1] {
		return medio
	}
	if arr[medio] > arr[medio-1] {
		return _indicePico(arr, medio+1, fin)
	} else {
		return _indicePico(arr, inicio, medio-1)
	}
}

/*
Complejidad: T(n) = 1T(n/2) + O(n^C)
	- A: 1
	- B: 2
	- C: 0
	- logB(A) = log2(1) = 0 = C => O(n^C * log(n)) = O(log(n))
*/

/*
18) (★★★★★) Tenemos un arreglo de tamaño 2n de la forma {C1, C2, C3, … Cn, D1, D2, D3, … Dn},
tal que la cantidad total de elementos del arreglo es potencia de 2 (por ende, n también lo es).
Implementar un algoritmo de División y Conquista que modifique el arreglo de tal
forma que quede con la forma {C1, D1, C2, D2, C3, D3, …, Cn, Dn},
sin utilizar espacio adicional (obviando el utilizado por la recursividad).
¿Cual es la complejidad del algoritmo?

Pista: Pensar primero cómo habría que hacer si el arreglo tuviera 4 elementos
({C1, C2, D1, D2}). Luego, pensar a partir de allí el caso de 8 elementos,
etc… para encontrar el patrón.
*/

func reordenar(arr []string) []string {
	if len(arr) == 2 {
		return arr
	}
	izq := reordenar(arr[:len(arr)/2])
	der := reordenar(arr[len(arr)/2:])
	for i := 0; i < len(arr)/2; i += 2 {
		izq[i+1], der[i] = der[i], izq[i+1]
	}
	return arr
}

/*
Complejidad: T(n) = 2T(n/2) + O(n^C)
	- A: 2
	- B: 2
	- C: 0
	- logB(A) = log2(2) = 1 > C => O(n^logB(A)) = O(n)
*/

func main() {
	// funcion de testeo
	arr := []string{"a1", "a2", "a3", "a4", "c1", "c2", "c3", "c4"}
	fmt.Println(reordenar(arr))
}
