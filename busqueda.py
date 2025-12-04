# Funciones de búsqueda en Python usando GitHub Copilot

# 1) Implementar una función buscar_elemento(lista, elemento)
#    que reciba una lista y un elemento a buscar.
#    La función debe devolver el índice del elemento si se encuentra
#    y -1 si el elemento no está en la lista.
def buscar_en_diccionarios(lista, clave, valor):
    """
    Busca el primer diccionario en `lista` donde dic[clave] == valor.
    Devuelve el índice del primer diccionario coincidente, o -1 si no se encuentra ninguno.

    - Ignora elementos de la lista que no sean diccionarios.
    - No lanza KeyError si la clave no está en un diccionario; simplemente continúa.
    """
    i = 0
    while i < len(lista):
        dic = lista[i]
        if isinstance(dic, dict) and clave in dic and dic[clave] == valor:
            return i
        i += 1
    return -1


# Ejemplos de uso
if __name__ == "__main__":
    lista = [
        {"id": 1, "nombre": "Ana"},
        {"id": 2, "nombre": "Luis"},
        {"id": 3, "nombre": "María"},
        "no es un diccionario",
        {"id": 4, "nombre": "Luis"},
    ]

    print(buscar_en_diccionarios(lista, "nombre", "Luis"))  # Salida: 1
    print(buscar_en_diccionarios(lista, "id", 3))           # Salida: 2
    print(buscar_en_diccionarios(lista, "edad", 30))       # Salida: -1
    print(buscar_en_diccionarios(lista, "nombre", "Pedro"))# Salida: -1

# 2) Implementar una función buscar_en_diccionarios(lista, clave, valor)
#    que reciba una lista de diccionarios y devuelva el índice del primer
#    diccionario donde dic[clave] == valor, o -1 si no existe.
