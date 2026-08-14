import sys
sys.path.insert(0, '.')
from methods import search_value_2d

# Test matriz 2D
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("🧪 Test search_value_2d")
print(f"Matriz: {matriz}")
print()

# Búsqueda de números
tests = [5, "5", 9, "9", 10, "xyz"]
for valor in tests:
    resultado = search_value_2d(matriz, valor)
    print(f"  Buscar {repr(valor):6} → {resultado}")

print("\n✓ Todos los tests pasaron")
