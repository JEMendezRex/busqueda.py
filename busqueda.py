# Funciones de búsqueda en Python usando GitHub Copilot

# 1) Implementar una función buscar_elemento(lista, elemento)
#    que reciba una lista y un elemento a buscar.
#    La función debe devolver el índice del elemento si se encuentra
#    y -1 si el elemento no está en la lista.

 def buscar_elemento(lista, elemento):
    """
    Busca un elemento en una lista y devuelve su índice.
    Si no se encuentra, devuelve -1.
    """
    for i, valor in enumerate(lista):
        if valor == elemento:
            return i
    return -1

# 2) Implementar una función buscar_en_diccionarios(lista, clave, valor)
#    que reciba una lista de diccionarios y devuelva el índice del primer
#    diccionario donde dic[clave] == valor, o -1 si no existe.
