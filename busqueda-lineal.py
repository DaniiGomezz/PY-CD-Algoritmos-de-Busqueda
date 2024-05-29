import time

start_time = time.time()

def busqueda(x, l):
    for ix, i in enumerate(l):
        if i == x:
            return ix  # Devuelve el índice si encuentra el elemento
    return -1  # Devuelve -1 si el elemento no se encuentra en la lista

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
elemento = 9
resultado = busqueda(elemento, lista)  # Almacenamos el resultado de la búsqueda en una variable

if resultado != -1:
    print(f"El elemento {elemento} se encuentra en el índice {resultado} de la lista.")
else:
    print("El elemento no se encuentra en la lista.")

end_time = time.time()
execution_time = end_time - start_time
print("Tiempo de ejecución:", execution_time, "segundos")
