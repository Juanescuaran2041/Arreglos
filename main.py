import tkinter as tk
from tkinter import ttk, simpledialog, messagebox

def get_second_element(array: list):
    if len(array) >= 2:
        return array[1]
    return "Elemento no disponible"

def insert_value_1d(array: list, index: int, value):
    if 0 <= index <= len(array):
        array.insert(index, value)
    return array

def search_value_1d(array: list, value):
    for i in range(len(array)):
        if str(array[i]) == str(value):
            return f"El valor {value} se encuentra en la posición {i}"
    return None

def get_element_2d(array: list, row: int, col: int):
    if 0 <= row < len(array) and 0 <= col < len(array[row]):
        return array[row][col]
    return None

def remove_value_2d(array: list, row: int, col: int):
    if 0 <= row < len(array) and 0 <= col < len(array[row]):
        array[row].pop(col)

def search_value_2d(array: list, value):
    for i in range(len(array)):
        for j in range(len(array[i])):
            if str(array[i][j]) == str(value):
                return f"Valor encontrado en la posición [{i}][{j}]"
    return "Valor no encontrado"

root = tk.Tk()
root.title("Gestión de Arreglos")
root.geometry("600x350")

array_1d = []
n_1d = simpledialog.askinteger("Arreglo 1D", "Ingrese el tamaño del arreglo 1D:")
if n_1d is not None:
    for i in range(n_1d):
        value = simpledialog.askstring("Arreglo 1D", f"Ingrese el valor para la posición {i}:")
        array_1d.append(value)

array_2d = []
n_2d_rows = simpledialog.askinteger("Arreglo 2D", "Ingrese el número de filas del arreglo 2D:")
n_2d_cols = simpledialog.askinteger("Arreglo 2D", "Ingrese el número de columnas del arreglo 2D:")
if n_2d_rows is not None and n_2d_cols is not None:
    for i in range(n_2d_rows):
        row = []
        for j in range(n_2d_cols):
            value = simpledialog.askstring("Arreglo 2D", f"Ingrese el valor para la posición [{i}][{j}]:")
            row.append(value)
        array_2d.append(row)

main_container = tk.Frame(root)
main_container.pack(fill="both", expand=True, padx=15, pady=15)

frame_1d = tk.LabelFrame(main_container, text=" Arreglo 1D ", padx=10, pady=10)
frame_1d.pack(side="left", fill="both", expand=True, padx=(0, 10))

lbl_info_1d = tk.Label(frame_1d, text=f"Actual: {array_1d}", wraplength=250)
lbl_info_1d.pack(pady=5)

lbl_result_1d = tk.Label(frame_1d, text="", fg="blue")
lbl_result_1d.pack(pady=5)

def callback_search_1d():
    result = get_second_element(array_1d)
    if result is not None:
        lbl_result_1d.config(text=f"El segundo elemento es: {result}")

btn_search_1d = tk.Button(frame_1d, text="Buscar en 1D", command=callback_search_1d)
btn_search_1d.pack(fill="x", pady=2)

def callback_insert_1d():
    index = simpledialog.askinteger("Insertar en 1D", "Ingrese el índice:")
    value = simpledialog.askstring("Insertar en 1D", "Ingrese el valor:")
    if index is not None and value is not None:
        insert_value_1d(array_1d, index, value)
        lbl_info_1d.config(text=f"Actual: {array_1d}")

btn_insert_1d = tk.Button(frame_1d, text="Insertar en 1D", command=callback_insert_1d)
btn_insert_1d.pack(fill="x", pady=2)

def callback_search_value_1d():
    value = simpledialog.askstring("Buscar en 1D", "Ingrese el valor a buscar:")
    if value is not None:
        result = search_value_1d(array_1d, value)
        lbl_result_1d.config(text=result if result else "Valor no encontrado")

btn_search_value_1d = tk.Button(frame_1d, text="Buscar valor en 1D", command=callback_search_value_1d)
btn_search_value_1d.pack(fill="x", pady=2)

frame_2d = tk.LabelFrame(main_container, text=" Arreglo 2D ", padx=10, pady=10)
frame_2d.pack(side="right", fill="both", expand=True, padx=(10, 0))

lbl_info_2d = tk.Label(frame_2d, text=f"Actual: {array_2d}", wraplength=250)
lbl_info_2d.pack(pady=5)

lbl_result_2d = tk.Label(frame_2d, text="", fg="blue")
lbl_result_2d.pack(pady=5)

def callback_get_element_2d():
    row = simpledialog.askinteger("Obtener elemento 2D", "Ingrese la fila:")
    col = simpledialog.askinteger("Obtener elemento 2D", "Ingrese la columna:")
    if row is not None and col is not None:
        result = get_element_2d(array_2d, row, col)
        if result is not None:
            lbl_result_2d.config(text=f"El elemento en [{row}][{col}] es: {result}")
        else:
            lbl_result_2d.config(text="Índice fuera de rango")

btn_get_element_2d = tk.Button(frame_2d, text="Obtener elemento 2D", command=callback_get_element_2d)
btn_get_element_2d.pack(fill="x", pady=2)

def callback_remove_value_2d():
    row = simpledialog.askinteger("Eliminar valor 2D", "Ingrese la fila:")
    col = simpledialog.askinteger("Eliminar valor 2D", "Ingrese la columna:")
    if row is not None and col is not None:
        remove_value_2d(array_2d, row, col)
        lbl_info_2d.config(text=f"Actual: {array_2d}")

btn_remove_value_2d = tk.Button(frame_2d, text="Eliminar valor 2D", command=callback_remove_value_2d)
btn_remove_value_2d.pack(fill="x", pady=2)

def callback_search_value_2d():
    value = simpledialog.askstring("Buscar valor 2D", "Ingrese el valor a buscar:")
    if value is not None:
        result = search_value_2d(array_2d, value)
        lbl_result_2d.config(text=result)

btn_search_value_2d = tk.Button(frame_2d, text="Buscar valor en 2D", command=callback_search_value_2d)
btn_search_value_2d.pack(fill="x", pady=2)

root.mainloop()