# Listas
frutas = ["manzana", "banana", "naranja"]
print(frutas[0])          # 'manzana'

frutas[1] = "pera"        # Modificar un valor
print(frutas)             # ['manzana', 'pera', 'naranja']

frutas.append("kiwi")     # Agrega un elemento al final
print(frutas)

frutas.remove("manzana")  # Elimina por valor
print(frutas)

frutas.sort()             # Ordena la lista
print(frutas)

print(len(frutas))        # Longitud de la lista

# in
frutas = ["manzana", "pera", "kiwi"]
print("kiwi" in frutas)       # True
print("naranja" in frutas)    # False

# index
indice = frutas.index("pera")
print("La posición de 'pera' es:", indice)

# contar
numeros = [1, 2, 3, 2, 4, 2]
print(numeros.count(2))   # 3

