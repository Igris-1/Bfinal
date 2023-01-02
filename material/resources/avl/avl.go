package diccionario

// I don't need vacations, I need knowledge

type hijo string

const (
	_ESTANDAR         = 0
	_COMPARACION      = 0
	_HIJO_IZQ    hijo = "izq"
	_HIJO_DER    hijo = "der"
	_SIN_HIJOS   hijo = "sin"
)

type nodo[K comparable, V any] struct {
	clave K
	dato  V
	izq   *nodo[K, V]
	der   *nodo[K, V]
}

type avl[K comparable, V any] struct {
	raiz *nodo[K, V]
	cant int
	cmp  func(K, K) int
}

func crearNodo[K comparable, V any](clave K, dato V) *nodo[K, V] {
	return &nodo[K, V]{clave: clave, dato: dato}
}

func CrearAVL[K comparable, V any](cmp func(K, K) int) Diccionario[K, V] {
	return &avl[K, V]{cmp: cmp}
}

func (a *avl[K, V]) Guardar(clave K, dato V)
func (a *avl[K, V]) Pertenece(clave K) bool
func (a *avl[K, V]) Obtener(clave K) V
func (a *avl[K, V]) Borrar(clave K) V
func (a *avl[K, V]) Cantidad() int

func (a *avl[K, V]) buscar(act *nodo[K, V], clave K, ant *nodo[K, V]) (*nodo[K, V], *nodo[K, V]) {
	if act == nil {
		return act, ant
	}
	valor := a.cmp(clave, act.clave)
	if valor == _COMPARACION {
		return act, ant
	} else if valor < _COMPARACION {
		return a.buscar(act.izq, clave, act)
	} else {
		return a.buscar(act.der, clave, act)
	}
}

func (a *avl[K, V]) Iterar(visitar func(clave K, dato V) bool) { a.IterarRango(nil, nil, visitar) }
func (a *avl[K, V]) IterarRango(desde *K, hasta *K, visitar func(clave K, dato V) bool)
func (a *avl[K, V]) Iterador() IterDiccionario[K, V] { return a.IteradorRango(nil, nil) }
func (a *avl[K, V]) IteradorRango(desde *K, hasta *K) IterDiccionario[K, V]
