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
10) (★★) Implementar, por división y conquista, una función que dado
un arreglo sin elementos repetidos y casi ordenado
(todos los elementos se encuentran ordenados, salvo uno),
obtenga el elemento fuera de lugar. Indicar y justificar el orden.
*/
func fueraDeLugar(arr []int) int {
	return _fueraDeLugar(arr, 0, len(arr)-1)
}

func _fueraDeLugar(arr []int, inicio, fin int) int {
	if inicio == fin {
		return -1
	}
	if inicio+1 == fin && arr[inicio] > arr[fin] {
		return arr[fin]
	}
	medio := (inicio + fin) / 2
	if medio >= 1 {
		if arr[medio] > arr[medio+1] && arr[medio] > arr[medio-1] {
			return arr[medio+1]
		} else if arr[medio] < arr[medio-1] {
			return arr[medio-1]
		}
	}
	return _fueraDeLugar(arr, inicio, medio-1) + _fueraDeLugar(arr, medio+1, fin)
}

/*
Complejidad: T(n) = 2T(n/2) + O(n^C)
	- A: 2
	- B: 2
	- C: 0
	- logB(A) = log2(2) = 1 > C => O(n^logB(A)) = O(n)
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
17) (★★★★★) Implementar una función (que utilice división y conquista) de orden
O(n*log(n)) que dado un arreglo de n números enteros devuelva true
o false según si existe algún elemento que aparezca más de la mitad de las veces.
Justificar el orden de la solución. Ejemplos:

	[1, 2, 1, 2, 3]		-> false
	[1, 1, 2, 3]		-> false
	[1, 2, 3, 1, 1, 1] 	-> true
	[1] 				-> true
*/

func mdm(arr []int) bool {
	cand := _mdm(arr, 0, len(arr)-1)
	cont := 0
	for i := 0; i < len(arr); i++ {
		if arr[i] == cand {
			cont++
		}
	}
	return cont > len(arr)/2
}

func _mdm(arr []int, inicio, fin int) int {
	if inicio == fin {
		return arr[inicio]
	}
	medio := (inicio + fin) / 2
	cand1 := _mdm(arr, inicio, medio)
	cand2 := _mdm(arr, medio+1, fin)

	cont1, cont2 := 0, 0
	for i := inicio; i < fin; i++ {
		if arr[i] == cand1 {
			cont1++
		} else if arr[i] == cand2 {
			cont2++
		}
	}
	if cont1 > cont2 {
		return cand1
	} else {
		return cand2
	}
}

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

func merge(arr []int, start, mid, end int) {
	// Calcula el tamaño de los arreglos C y D
	sizeC := mid - start + 1
	sizeD := end - mid

	// Crea los arreglos C y D
	C := make([]int, sizeC)
	D := make([]int, sizeD)

	// Copia los elementos del arreglo original a los arreglos C y D
	copy(C, arr[start:mid+1])
	copy(D, arr[mid+1:end+1])

	// Variables de índice para los arreglos C y D
	i := 0
	j := 0

	// Variables de índice para el arreglo original
	k := start

	// Itera sobre los arreglos C y D
	for i < sizeC && j < sizeD {
		if C[i] <= D[j] {
			arr[k] = C[i]
			i++
		} else {
			arr[k] = D[j]
			j++
		}
		k++
	}

	// Copia los elementos restantes de C al arreglo original
	for i < sizeC {
		arr[k] = C[i]
		i++
		k++
	}

	// Copia los elementos restantes de D al arreglo original
	for j < sizeD {
		arr[k] = D[j]
		j++
		k++
	}
}

func divideAndConquer(arr []int, start, end int) {
	if start < end {
		// Calcula el punto medio del arreglo
		mid := (start + end) / 2

		// Divide y conquista el primer y segundo subarreglo
		divideAndConquer(arr, start, mid)
		divideAndConquer(arr, mid+1, end)

		// Mezcla los subarreglos
		merge(arr, start, mid, end)
	}
}

/*
Complejidad:
	T(n) = 2T(n/2) + O(n)
	- A: 2
	- B: 2
	- C: 1
	logB(A) = log2(2) = 1 = C => T(n) = O(n*log(n))
*/

/*
19) (★★★★) Dado un arrego de numeros enteros, implementar una
func ceros(vector []int) int que retorne la cantidad de numeros 0
en el vector utilizando la téctnica de "División y conquista". El vector
únicamente contiene los números 1s y 0s. El vector inicialmente tiene solamente
1s seguidos por únicamente 0s, por ejemplo: [1,1,1,1,0,0,0]
¿Cual es el orden del algoritmo? Justificar utilizando el Teorema Maestro
*/

func ceros(vector []int) int {
	return _ceros(vector, 0, len(vector)-1)
}

func _ceros(vector []int, inicio, fin int) int {
	if inicio == fin {
		return len(vector) - inicio
	}
	medio := (inicio + fin) / 2
	if vector[medio] == 0 {
		if vector[medio-1] == 1 {
			return len(vector) - medio
		} else {
			return _ceros(vector, inicio, medio-1)
		}
	} else {
		return _ceros(vector, medio+1, fin)
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
20) (★★★) Dado un arreglo desordenado de numeross enteros devolver
el indice del primer 0 en el arreglo, ej: [1,2,0,4,3,0] -> indice: 2
*/
func indice2(arr []int) int {
	indice, bool := _indice2(arr, 0, len(arr)-1)
	if bool {
		return indice
	}
	return -1
}

func _indice2(arr []int, inicio, fin int) (int, bool) {
	if inicio == fin {
		if arr[inicio] == 0 {
			return inicio, true
		} else {
			return inicio, false
		}
	}
	medio := (inicio + fin) / 2
	izq, bool1 := _indice2(arr, inicio, medio)
	der, bool2 := _indice2(arr, medio+1, fin)
	if bool1 && bool2 {
		if izq < der {
			return izq, bool1
		}
	}
	if bool1 {
		return izq, bool1
	} else if bool2 {
		return der, bool2
	}
	return -1, false
}

/*
Complejidad: T(n) = 2T(n/2) + O(n^C)
	- A: 2
	- B: 2
	- C: 0
	- logB(A) = log2(2) = 1 > C => O(n^logB(A)) = O(n)
*/
