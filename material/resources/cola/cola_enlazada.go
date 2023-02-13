package cola

// nodo
type nodo[T any] struct {
	dato T
	prox *nodo[T]
}

// funcion auxiliar que crea un nodo
func nuevoNodo[T any](dato T) *nodo[T] {
	return &nodo[T]{dato: dato}
}

// ColaEnlazada
type colaEnlazada[T any] struct {
	prim *nodo[T]
	ult  *nodo[T]
}

func CrearColaEnlazada[T any]() *colaEnlazada[T] {
	return &colaEnlazada[T]{}
}

// EstaVacia
func (c *colaEnlazada[T]) EstaVacia() bool {
	return c.prim == nil
}

// VerPrimero
func (c *colaEnlazada[T]) VerPrimero() T {
	if c.EstaVacia() {
		panic("La cola esta vacia")
	}
	return c.prim.dato
}

// Encolar
func (c *colaEnlazada[T]) Encolar(dato T) {
	nuevo := nuevoNodo(dato)
	if c.EstaVacia() {
		c.prim = nuevo
	} else {
		c.ult.prox = nuevo
	}
	c.ult = nuevo
}

// Desencolar
func (c *colaEnlazada[T]) Desencolar() T {
	if c.EstaVacia() {
		panic("La cola esta vacia")
	}
	dato := c.prim.dato
	c.prim = c.prim.prox
	if c.prim == nil {
		c.ult = nil
	}
	return dato
}
