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


#  Tuplas

coordenadas = (10.5, 20.3)
print(coordenadas[0])   # 10.5

# Tupla con un solo valor requiere coma:
un_valor = (5,)

# Uso común: retornar múltiples valores
def dividir(dividendo, divisor):
    cociente = dividendo // divisor
    resto = dividendo % divisor
    return cociente, resto

resultado = dividir(10, 3)
print(resultado)           # (3, 1)
cociente, resto = dividir(10, 3)
print("Cociente:", cociente) # 3
print("Resto:", resto) # 1


colores = ("rojo", "verde", "azul", "rojo")
print("rojo" in colores)        # True
print(colores.index("azul"))    # 2
print(colores.count("rojo"))    # 2



# Diccionarios

persona = {"nombre": "Ana", "edad": 30}
print(persona["nombre"])     # 'Ana'

persona["edad"] = 31         # Modificar valor


persona.get("correo", "No definido")   # Evita error si no existe
print(persona.keys())       # dict_keys(['nombre', 'edad'])
print(persona.values())     # dict_values(['Ana', 31])
print(persona.items())      # dict_items([('nombre', 'Ana'), ('edad', 31)])


print("nombre" in persona)       # True
print("correo" in persona)       # False

print("Ana" in persona.values())   # True

print(persona.get("correo"))          # None
print(persona.get("correo", "No hay correo"))  # Mensaje personalizado


# Conjuntos (set)

colores = {"rojo", "verde", "azul"}
colores.add("amarillo")
print(colores)
colores.add("rojo")    # No se repite


# Operaciones de conjuntos
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A.union(B))         # {1, 2, 3, 4, 5, 6}
print(A.intersection(B))  # {3, 4}
print(A.difference(B))    # {1, 2}
print(B.difference(A))    # {5, 6}

numeros = {1, 2, 3, 4}
print(3 in numeros)    # True
print(5 in numeros)    # False




contacto = {
    "nombre": "Juan",
    "telefonos": ["3121234567", "3109876543"]
}

contacto["telefonos"].append("3001112233")

for tel in contacto["telefonos"]:
    print("Número:", tel)

print("Cantidad de teléfonos:", len(contacto["telefonos"]))

agenda = {
    "Laura": "3101234567",
    "Pedro": "3129876543",
    "Ana": "3204567890"
}

nombre = input("¿A quién deseas buscar? ")

if nombre in agenda:
    print(f"El número de {nombre} es {agenda[nombre]}")
else:
    print(f"{nombre} no está en la agenda.")



agenda = {
    "Laura": {"telefono": "3101234567", "edad": 28},
    "Pedro": {"telefono": "3129876543", "edad": 35},
    "Ana": {"telefono": "3204567890", "edad": 22}
}

# Buscar a Pedro
nombre = "Pedro"
if nombre in agenda:
    print(f"{nombre} tiene {agenda[nombre]['edad']} años y su número es {agenda[nombre]['telefono']}")
else:
    print(f"{nombre} no está en la agenda")



personas = [
    {"nombre": "Laura", "telefono": "3101234567", "edad": 28},
    {"nombre": "Pedro", "telefono": "3129876543", "edad": 35},
    {"nombre": "Ana", "telefono": "3204567890", "edad": 22},
    {"nombre": "Pedro", "telefono": "3001122334", "edad": 30}
]

# Buscar todas las personas llamadas "Pedro"
for persona in personas:
    if persona["nombre"] == "Pedro":
        print(f"Pedro - Edad: {persona['edad']}, Teléfono: {persona['telefono']}")


familias = {
    "Gomez": [
        {"nombre": "Laura", "edad": 28},
        {"nombre": "Carlos", "edad": 31}
    ],
    "Pérez": [
        {"nombre": "Ana", "edad": 22}
    ]
}

for persona in familias["Gomez"]:
    print(persona["nombre"], "-", persona["edad"])



agenda = {
    "Pedro": {"telefono": "3129876543"},
    "Pedro": {"telefono": "3001122334"}
}
print(agenda)  
# {'Pedro': {'telefono': '3001122334'}}




