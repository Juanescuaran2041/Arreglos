"""
Métodos para manipular Arrays 1D y 2D
Los métodos deben ser completados por el estudiante
"""


# ═══════════════════════════════════════════════════════════════════════════
# MÉTODOS ARRAY 1D
# ═══════════════════════════════════════════════════════════════════════════

def get_second_element(array: list):
    """Obtiene el segundo elemento del array 1D (índice 1)"""
    if len(array) > 1:
        return array[1]
    return None


def insert_value_1d(array: list, index: int, value):
    """Inserta un valor en la posición especificada (1D)"""
    if 0 <= index <= len(array):
        array.insert(index, value)
        return True
    return False


def search_value_1d(array: list, value):
    """Busca un valor en el array 1D y retorna la posición"""
    try:
        return array.index(value)
    except ValueError:
        return -1


# ═══════════════════════════════════════════════════════════════════════════
# MÉTODOS ARRAY 2D
# ═══════════════════════════════════════════════════════════════════════════

def get_element_2d(array: list, row: int, col: int):
    """Obtiene el elemento en posición [row][col]"""
    if 0 <= row < len(array) and 0 <= col < len(array[row]):
        return array[row][col]
    return None


def remove_value_2d(array: list, row: int, col: int):
    """Elimina un elemento en [row][col]"""
    if 0 <= row < len(array) and 0 <= col < len(array[row]):
        array[row][col] = None
        return True
    return False


def search_value_2d(array: list, value):
    """Busca un valor en el array 2D y retorna (row, col)"""
    for row in range(len(array)):
        for col in range(len(array[row])):
            if array[row][col] == value:
                return (row, col)
    return None