class _Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.prox = None

class ListaEnlazada:
    """Modela una lista enlazada"""
    def __init__(self):
        """Crea una lista enlazada vacía."""
        # referencia al primer nodo (None si la lista está vacía)
        self.prim = None
        # cantidad de elementos de la lista
        self.len = 0

    #eliminar un elemento de una posicion
    def pop(self, i=None):
        """Elimina el nodo de la posición i, y devuelve el dato contenido.
           Si i está fuera de rango, se levanta la excepción IndexError.
           Si no se recibe la posición, devuelve el último elemento."""

        if i is None:
            i = self.len - 1

        if i < 0 or i >=  self.len:
            raise IndexError('Índice fuera de rango')

        if i == 0:
            #Caso particular: saltear la cabecera de la lista
            dato = self.prim.dato
            self.prim = self.prim.prox
        else:
            #Buscar los nodos en la posicion (i-1) e (i)
            n_ant = self.prim
            n_act = n_ant.prox
            for pos in range(1, i):
                n_ant = n_act
                n_act = n_ant.prox

            #guardar el dato y descartar el nodo
            dato = n_act.dato
            n_ant.prox = n_act.prox

        self.len -= 1
        return dato

    def remove(self, x):
        """Elimina el primer nodo que contenga el dato x.
           Si no se encuentra el dato, se levanta la excepción ValueError."""
        if self.len == 0:
            raise ValueError('La lista está vacía')

        if self.prim.dato == x:
            #Caso particular: saltear la cabecera de la lista
            self.prim = self.prim.prox
        else:
            #Buscar el nodo anterior al que contiene el dato x (n_ant)
            n_ant = self.prim
            n_act = n_ant.prox
            while n_act is not None and n_act.dato != x:
                n_ant = n_act
                n_act = n_act.prox

            if n_act is None:
                raise ValueError('El elemento no existe')

            #eliminar el nodo
            n_ant.prox = n_act.prox
        self.len -= 1

    def insert(self, i, x):
        """Inserta el dato x en la posicion i, si la posicion
           es invalida, levanta IndexError"""
        if i < 0 or i > self.len:
            raise IndexError('Índice fuera de rango')

        nuevo = _Nodo(x)

        if i == 0:
            #Caso particular: insertar al principio
            nuevo.prox = self.prim
            self.prim = nuevo
        else:
            #Buscar el nodo anterior a la posicion deseada
            n_ant = self.prim
            for pos in range(1, i):
                n_ant = n_ant.prox

            #insertar el nuevo nodo
            nuevo.prox = n_ant.prox
            n_ant.prox = nuevo
        self.len += 1

    def append(self, x):
        """Agrega el dato x al final de la lista"""
        self.insert(self.len, x)
    
    def appendleft(self, x):
        """Agrega el dato x al principio de la lista"""
        self.insert(0, x)

    def index(self, x):
        """Devuelve la posición de la primera ocurrencia del dato x.
           Si no se encuentra, levanta ValueError"""
        if self.len == 0:
            raise ValueError('La lista está vacía')

        if self.prim.dato == x:
            return 0
        else:
            n_ant = self.prim
            n_act = n_ant.prox
            for pos in range(1, self.len):
                if n_act.dato == x:
                    return pos
                n_ant = n_act
                n_act = n_act.prox
            raise ValueError('El elemento no existe')

    # Hacer que la lista sea iterable
    def __iter__(self):
        """Devuelve un iterador sobre la lista"""
        return IteradorListaEnlazada(self)

    #15.9.1) Agregar a ListaEnlazada un método extend que reciba una ListaEnlazada
    #        y agregue a la lista actual los elementos que se encuentran en la lista recibida.
    def extend(self, lista):
        """Agrega los elementos de la lista recibida al final de la lista actual"""
        for x in lista:
            self.append(x)

    def __str__(self):
        """Devuelve una representacion en cadena de la lista"""
        if self.prim is None:
            return '[]'
        else:
            nodo = self.prim
            s = '[' + str(nodo.dato)
            nodo = nodo.prox
            while nodo is not None:
                s += ', ' + str(nodo.dato)
                nodo = nodo.prox
            s += ']'
            return s

    def __len__(self):
        """Devuelve la cantidad de elementos de la lista"""
        return self.len

#iterador de lista enlazada (eliminar e insertar son de tiempo constante)
#no recuerdo cuando hice esto ni por que lo hice
class IteradorListaEnlazada:
    """Almacena el estado de una iteración sobre la ListaEnlazada."""
    def __init__(self, lista):
        """Crea un iterador para la lista dada"""
        self.lista= lista
        self.anterior = None
        self.actual = lista.prim

    def avanzar(self):
        """Avanza la iteracion a un pasohacia adelante.
        PRE: la iteracion no debe haber llegado al final
        """
        self.aterior = self.actual
        self.actual = self.actual.prox

    def dato_actual(self):
        """Devuelve el elemento en la posición actual de iteració
        PRE: la iteración no debe haber llegado al final
        """
        return self.actual.dato

    def esta_al_final(self):
        """Devuelve verdadero si la iteracion llego al final de la lista."""
        return self.actual is None

    def insertar(self, x):
        """Insertar un elemento en el lugar de la iteración actual.
           Una vez insertado, el nuevo elemento será el actual de la iteración,
           y el elemento que antes era el actual será el siguiente."""
        nuevo = _Nodo(x)
        if self.anterior:
            nuevo.prox = self.atenrior.prox
            self.anterior.prox = nuevo
        else:
            nuevo.prox = self.lista.prim
            self.lista.prim = nuevo
        self.actual = nuevo

    def eliminar(self):
        """Elimina el elemento en la posición actual de la iteración.
           Una vez eliminado, el elemento que antes era el actual será el siguiente."""
        dato = self.dato_actual()
        if self.anterior:
            self.anterior.prox = self.actual.prox
            self.actual = self.anterior.prox
        else:
            self.lista.prim = self.actual.prox
            self.actual = self.lista.prim
        return dato
    
    def __next__(self):
        """Devuelve el siguiente elemento de la iteración.
           Si la iteración llego al final, levanta StopIteration"""
        if self.esta_al_final():
            raise StopIteration("no hay más elementos en la lista")
        dato = self.dato_actual()
        self.avanzar()
        return dato