
print('bienveido a galllinasG.S.A.S')

print('   ')
print('ingrese 1 si desea visualizar el inventario')
print('ingrese 2 si desea ingresar al inventario')
opcion=int(input("-"))
gallinas=[
    {"id":"1", "nombre":"paquita","cantidad_huevos":10,},
    {"id":"2", "nombre":"paquito","cantidad_huevos":0,},
]
contador_while=0
if opcion==1 :
   for gallina in range(len(gallinas)):
       print("gallina," , gallina+1)
       print(gallinas[gallina])

else:
    if opcion==2 :
        while contador_while==0 :
            id_gallina=input("ingrese el id de la gallina:   ")
            nombre_gallina=input("ingrese el nombre de la gallina:   ")
            cantidad_huevos=int(input("ingrese la cantidad de huevos:   "))
           
            gallinas.append({"id":id_gallina ,"nombre":nombre_gallina,"caantidad_huevos":cantidad_huevos} )
            
            print(nombre_gallina,id_gallina)
            print(gallinas)
                
            
            contador_while=input('ingrese 1 si desea salir ')


















# import json
# import os

# # Ruta del archivo donde se guardarán los datos
# ARCHIVO_DATOS = "gallinas.json"

# # Cargar datos si ya existen, si no, usar datos iniciales
# if os.path.exists(ARCHIVO_DATOS):
#     with open(ARCHIVO_DATOS, "r") as f:
#         gallinas = json.load(f)
# else:
#     gallinas = [
#         {"id": "1", "nombre": "paquita", "cantidad_huevos": 10},
#         {"id": "2", "nombre": "paquito", "cantidad_huevos": 0},
#     ]

# print("Bienvenido a Gallinas G.S.A.S\n")
# print("Ingrese 1 si desea visualizar el inventario")
# print("Ingrese 2 si desea ingresar al inventario")
# opcion = input("- ")

# if opcion == "1":
#     print("\n--- INVENTARIO ---")
#     for i, gallina in enumerate(gallinas, start=1):
#         print(f"Gallina {i}:")
#         print(f"  ID: {gallina['id']}")
#         print(f"  Nombre: {gallina['nombre']}")
#         print(f"  Huevos: {gallina['cantidad_huevos']}\n")

# elif opcion == "2":
#     while True:
#         id_gallina = input("Ingrese el ID de la gallina: ")
#         nombre_gallina = input("Ingrese el nombre de la gallina: ")
#         cantidad_huevos = int(input("Ingrese la cantidad de huevos: "))

#         nueva_gallina = {
#             "id": id_gallina,
#             "nombre": nombre_gallina,
#             "cantidad_huevos": cantidad_huevos
#         }

#         gallinas.append(nueva_gallina)

#         print("\nGallina agregada con éxito.")
#         print(nueva_gallina)

#         salir = input("\nIngrese '1' si desea salir, cualquier otra tecla para continuar: ")
#         if salir == "1":
#             break

#     # Guardar los datos actualizados en el archivo
#     with open(ARCHIVO_DATOS, "w") as f:
#         json.dump(gallinas, f, indent=4)

#     print("\nDatos guardados correctamente.")
# else:
#     print("Opción no válida.")

















# def crear_matriz(filas, columnas):
#   """
#   Crea una matriz (lista de listas) vacía con el número especificado de filas y columnas.
#   """
#   matriz = []
#   for _ in range(filas):
#     fila = []
#     for _ in range(columnas):
#       fila.append(0)  # Inicializar con un valor por defecto (puedes cambiarlo)
#     matriz.append(fila)
#   return matriz

# def ingresar_datos(matriz):
#   """
#   Ingresa nuevo en la matriz proporcionada por el usuario.
#   """
#   filas = len(matriz)
#   columnas = len(matriz[0]) if filas > 0 else 0

#   for i in range(filas):
#     for j in range(columnas):
#       while True:
#         try:
#           valor = float(input(f"Ingrese el valor para la posición ({i+1}, {j+1}): "))
#           matriz[i][j] = valor
#           break
#         except ValueError:
#           print("Por favor, ingrese un número válido.")

# def imprimir_matriz(matriz):
#   """
#   Imprime la matriz en la consola.
#   """
#   for fila in matriz:
#     print(fila)

# # Ejemplo de uso:
# filas = int(input("Ingrese el número de filas: "))
# columnas = int(input("Ingrese el número de columnas: "))

# mi_matriz = crear_matriz(filas, columnas)
# ingresar_datos(mi_matriz)
# print("\nMatriz ingresada:")
# imprimir_matriz(mi_matriz)
    