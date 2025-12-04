# Funciones de búsqueda en Python usando GitHub Copilot

# 1) Implementar una función buscar_elemento(lista, elemento)
#    que reciba una lista y un elemento a buscar.
#    La función debe devolver el índice del elemento si se encuentra
#    y -1 si el elemento no está en la lista.

def buscar_elemento(lista, elemento):
    """
    Busca `elemento` en `lista` usando un bucle while.
    Devuelve el índice del primer elemento coincidente o -1 si no se encuentra.
    """
    i = 0
    while i < len(lista):
        if lista[i] == elemento:
            return i
        i += 1
    return -1


# Ejemplos de uso
if __name__ == "__main__":
    datos = [10, 20, 30, "hola", 50]
    print(buscar_elemento(datos, 30))    # Salida: 2
    print(buscar_elemento(datos, "adiós"))  # Salida: -1
