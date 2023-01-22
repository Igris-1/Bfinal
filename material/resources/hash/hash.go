package diccionario

import (
	"fmt"
)

type estado int

const (
	_VACIO estado = iota
	_OCUPADO
	_BORRADO
	_CAPACIDAD_INICIAL = 20
	_FACTOR_CARGA      = 0.75
	_AUMENTAR_CAP      = 2.5
	_REDUCIR_CAP       = 0.5
	_ESTANDAR          = 4
	_INICIAL           = 0
)

type campo[K comparable, V any] struct {
	clave  K
	dato   V
	estado estado
}

type hash[K comparable, V any] struct {
	capacidad int
	cantidad  int
	borrados  int
	campos    []campo[K, V]
}

func CrearHash[K comparable, V any]() Diccionario[K, V] {
	return &hash[K, V]{capacidad: _CAPACIDAD_INICIAL, campos: crearTabla[K, V](_CAPACIDAD_INICIAL)}
}

func crearTabla[K comparable, V any](cap int) []campo[K, V] { return make([]campo[K, V], cap) }

func (h *hash[K, V]) Guardar(clave K, dato V) {
	if (h.cantidad + h.borrados) >= int(float64(h.capacidad)*_FACTOR_CARGA) {
		h.redimensionar(_AUMENTAR_CAP)
	}
	valor := buscar(h, clave)
	if h.campos[valor].estado != _VACIO && h.campos[valor].clave == clave {
		h.campos[valor].dato = dato
	} else {
		h.campos[valor].clave = clave
		h.campos[valor].dato = dato
		h.campos[valor].estado = _OCUPADO
		h.cantidad++
	}
}

func (h *hash[K, V]) Pertenece(clave K) bool {
	valor := buscar(h, clave)
	return h.campos[valor].estado != _VACIO
}

func (h *hash[K, V]) Obtener(clave K) V {
	valor := buscar(h, clave)
	if h.campos[valor].estado == _VACIO {
		panic("La clave no pertenece al diccionario")
	}
	return h.campos[valor].dato
}

func (h *hash[K, V]) Borrar(clave K) V {
	if (h.cantidad) <= (h.capacidad/_ESTANDAR) && h.capacidad > _CAPACIDAD_INICIAL {
		h.redimensionar(_REDUCIR_CAP)
	}
	valor := buscar(h, clave)
	if h.campos[valor].estado == _VACIO {
		panic("La clave no pertenece al diccionario")
	} else {
		h.campos[valor].estado = _BORRADO
		h.cantidad--
		h.borrados++
	}
	return h.campos[valor].dato
}

func buscar[K comparable, V any](h *hash[K, V], clave K) int {
	pos := posicion(h, clave, h.capacidad)
	for i := pos; i < h.capacidad; i++ {
		esta, vacio := pertenece(i, h, clave)
		if esta || vacio {
			return i
		} else if i == h.capacidad-1 {
			i = _INICIAL
		}
	}
	return -1
}

func pertenece[K comparable, V any](pos int, h *hash[K, V], clave K) (bool, bool) {
	var pertenece bool
	var vacio bool
	if h.campos[pos].estado == _OCUPADO && h.campos[pos].clave == clave {
		pertenece = true
	} else if h.campos[pos].estado == _VACIO {
		vacio = true
	}
	return pertenece, vacio
}

func (h hash[K, V]) Cantidad() int { return h.cantidad }

func (h *hash[K, V]) redimensionar(num float64) {
	cap_int := int(float64(h.capacidad) * num)
	tablaVieja := h.campos
	h.campos = crearTabla[K, V](cap_int)
	h.capacidad = cap_int
	h.borrados = 0
	h.cantidad = 0
	for i := 0; i < len(tablaVieja); i++ {
		if tablaVieja[i].estado == _OCUPADO {
			h.Guardar(tablaVieja[i].clave, tablaVieja[i].dato)
		}
	}
}

func (h *hash[K, V]) Iterar(f func(clave K, dato V) bool) {
	for i := 0; i < h.capacidad; i++ {
		if h.campos[i].estado == _OCUPADO {
			if !f(h.campos[i].clave, h.campos[i].dato) {
				break
			}
		}
	}
}

type iteradorHash[K comparable, V any] struct {
	hash *hash[K, V]
	pos  int
}

func (h *hash[K, V]) Iterador() IterDiccionario[K, V] {
	iter := &iteradorHash[K, V]{h, _INICIAL}
	iter.pos = buscarIter(iter)
	return iter
}

func (iter *iteradorHash[K, V]) HaySiguiente() bool { return iter.pos < iter.hash.capacidad }

func (iter *iteradorHash[K, V]) VerActual() (clave K, dato V) {
	if !iter.HaySiguiente() {
		panic("El iterador termino de iterar")
	}
	return iter.hash.campos[iter.pos].clave, iter.hash.campos[iter.pos].dato
}

func (iter *iteradorHash[K, V]) Siguiente() (clave K) {
	if !iter.HaySiguiente() {
		panic("El iterador termino de iterar")
	}
	valor := iter.hash.campos[iter.pos].clave
	iter.pos++
	iter.pos = buscarIter(iter)
	return valor
}

func buscarIter[K comparable, V any](iter *iteradorHash[K, V]) int {
	for i := iter.pos; i < iter.hash.capacidad; i++ {
		if iter.hash.campos[i].estado == _OCUPADO {
			return i
		}
	}
	return iter.hash.capacidad
}

// https://en.wikipedia.org/wiki/Fowler%E2%80%93Noll%E2%80%93Vo_hash_function
func posicion[K comparable, V any](h *hash[K, V], clave K, capacidad int) int {
	var hash uint32 = 2166136261
	bytes := []byte(fmt.Sprintf("%v", clave))
	for _, c := range bytes {
		hash ^= uint32(c)
		hash *= 16777619
	}
	return int(hash) % capacidad
}
