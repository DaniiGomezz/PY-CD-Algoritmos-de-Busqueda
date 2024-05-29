import time

"""
la búsqueda binaria, aplicable solo en listas ordenadas, divide repetidamente la lista en mitades, descartando 
la mitad donde el elemento no puede estar y reduciendo así el espacio de búsqueda de manera eficiente 
"""

start_time = time.time()


def busqueda_binaria_recursiva(x, lista, izquierda, derecha):
    if izquierda > derecha:
        return None  # Caso base: el elemento no se encuentra en la lista

    medio = (izquierda + derecha) // 2  # Calculamos el índice medio del rango

    if (
        lista[medio] == x
    ):  # Si el elemento en el medio es igual a 'x', lo hemos encontrado
        return medio
    elif lista[medio] < x:  # Si 'x' es mayor, buscamos en la mitad derecha del rango
        return busqueda_binaria_recursiva(x, lista, medio + 1, derecha)
    else:  # Si 'x' es menor, buscamos en la mitad izquierda del rango
        return busqueda_binaria_recursiva(x, lista, izquierda, medio - 1)


# Ejemplo de uso:
lista_ordenada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Lista ordenada
elemento = 9  # Elemento que queremos buscar

# Llamamos a la función de búsqueda binaria recursiva
resultado = busqueda_binaria_recursiva(
    elemento, lista_ordenada, 0, len(lista_ordenada) - 1
)

if resultado is not None:
    print(f"El elemento {elemento} se encuentra en el índice {resultado} de la lista.")
else:
    print(f"El elemento {elemento} no se encuentra en la lista.")


end_time = time.time()
execution_time = end_time - start_time
print("Tiempo de ejecución:", execution_time, "segundos")
