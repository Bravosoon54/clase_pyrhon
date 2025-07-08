for i in range(0,5):
    print(i)
    
for i in range(1,5):
    print(i)
    
for i in range(10, 30, 2):
    print(i)

frutas = ['pera', 'naranja', 'coco', 'uva', 'banano'] #lista

for fruta in frutas:
    print(fruta)
    
for indice, fruta in enumerate(frutas):
    print(f"{indice} - {fruta}")
    
# averiguar como hacer los ciclos for, while, do whlie, como agregar datos, editar y eliminar datos a un arreglo en python
# 1 ver inventario
# 2 salida de inmventario se le pregunta al usuario que producto va a comprar para restar del inventario 
# 3 agregar producto al inventario y aumentar cantidad disponible

contador = 0
while contador<=50:
    print(contador)
    contador += 1
    
numero = 0
while True:
    print(numero)
    numero += 1
    if numero <= 5:
        break