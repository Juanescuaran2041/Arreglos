def get_second_element(array: list):
    return array[1]
    


def insert_value_1d(array: list, index: int, value):
    if 0 <= index <= len(array):
        array.insert(index, value)
    return array

def search_value_1d(array: list, value):
    for i in range(len(array)):
        if array[i] == value:
            return f"El valor {value} se encuentra en la posición {i}"
    return None

def get_element_2d(array: list, row: int, col: int):
    if 0 <= row < len(array) and 0 <= col < len(array[row]):
        return array[row][col]
    return None


def remove_value_2d(array: list, row: int, col: int):
    array[row].remove(array[row][col])


def search_value_2d(array: list, value):
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == value:
                return f"Valor encontrado en la posición [{i}][{j}]"
    return "Valor no encontrado"