import tkinter as tk
from tkinter import ttk, simpledialog, messagebox

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



# CAPA DE UI

root = tk.Tk()
root.title("Gestión de Arreglos")
root.geometry("400x300")

#Inicializar los arrays de forma dinamica

array_1d =[]
n_1d = simpledialog.askinteger("Arreglo 1D", "Ingrese el tamaño del arreglo 1D:")
for i in range(n_1d):
    value = simpledialog.askinteger("Arreglo 1D", f"Ingrese el valor para la posición {i}:")
    array_1d.append(value)

array_2d = []
n_2d_rows = simpledialog.askinteger("Arreglo 2D", "Ingrese el número de filas del arreglo 2D:")
n_2d_cols = simpledialog.askinteger("Arreglo 2D", "Ingrese el número de columnas del arreglo 2D:")

for i in range(n_2d_rows):
    row = []
    for j in range(n_2d_cols):
        value = simpledialog.askinteger("Arreglo 2D", f"Ingrese el valor para la posición [{i}][{j}]:")
        row.append(value)
    array_2d.append(row)

# Busqueda 1d

label_search_1d = tk.Label(root, text="Arreglo 1d")
label_search_1d.pack()

lbl_info = tk.Label(root, text=f"arreglo_actual: {array_1d}")
lbl_info.pack()

lbl_result = tk.Label(root, text="")
lbl_result.pack()

def callback_search_1d():
    result = get_second_element(array_1d)
    if result is not None:
        lbl_result.config(text=f"El segundo elemento es: {result}")

btn_search_1d = tk.Button(root, text="Buscar en 1D", command=callback_search_1d)
btn_search_1d.pack()


def callback_insert_1d():
    index = simpledialog.askinteger("Insertar en 1D", "Ingrese el índice:")
    value = simpledialog.askinteger("Insertar en 1D", "Ingrese el valor:")
    if index is not None and value is not None:
        insert_value_1d(array_1d, index, value)
        lbl_info.config(text=f"arreglo_actual: {array_1d}")

btn_insert_1d = tk.Button(root, text="Insertar en 1D", command=callback_insert_1d)
btn_insert_1d.pack()

def callback_search_value_1d():
    value = simpledialog.askinteger("Buscar en 1D","Ingrese el valor a buscar:")
    if value is not None:
        result = search_value_1d(array_1d, value)
        lbl_result.config(text=result if result else "Valor no encontrado")

btn_search_value_1d = tk.Button(root, text="Buscar valor en 1D", command=callback_search_value_1d)
btn_search_value_1d.pack()


# mostrar array 2d
label_search_2d = tk.Label(root, text="Arreglo2d")
label_search_2d.pack()

lbl_info_2d = tk.Label(root, text=f"Arreglo actual: {array_2d}")
lbl_info_2d.pack()

lbl_result_2d = tk.Label(root, text="")
lbl_result_2d.pack()

def callback_get_element_2d():
    row = simpledialog.askinteger("Obtener elemento 2D", "Ingrese la fila:")
    col = simpledialog.askinteger("Obtener elemento 2D", "Ingrese la columna:")
    if row is not None and col is not None:
        result = get_element_2d(array_2d,row, col)
        if result is not None:
            lbl_result_2d.config(text=f"El elemento en [{row}][{col}] es: {result}")
        else:
            lbl_result_2d.config(text="Índice fuera de rango")

btn_get_element_2d = tk.Button(root, text="Obtener elemento 2D", command=callback_get_element_2d)
btn_get_element_2d.pack()

def callback_remove_value_2d():
    row = simpledialog.askinteger("Eliminar valor 2D", "Ingrese la fila:")
    col = simpledialog.askinteger("Eliminar valor 2D", "Ingrese la columna:")
    if row is not None and col is not None:
        remove_value_2d(array_2d, row, col)
        lbl_info_2d.config(text=f"Arreglo actual: {array_2d}")

btn_remove_value_2d = tk.Button(root, text="Eliminar valor 2D", command=callback_remove_value_2d)
btn_remove_value_2d.pack()

def callback_search_value_2d():
    value = simpledialog.askinteger("Buscar valor 2D", "Ingrese el valor a buscar:")
    if value is not None:
        result = search_value_2d(array_2d, value)
        lbl_result_2d.config(text=result)

btn_search_value_2d = tk.Button(root, text="Buscar valor en 2D", command=callback_search_value_2d)
btn_search_value_2d.pack()

root.mainloop()