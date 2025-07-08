import json

# Cargar inventario guardado o crear uno inicial
try:
    with open('inventario.json', 'r') as archivo:
        inventario = json.load(archivo)
except FileNotFoundError:
    inventario = {
        'pera': 10,
        'naranja': 8,
        'coco': 5
    }

print("Bienvenido al sistema de inventario\n")

while True:
    print("\n--- MENÚ ---")
    print("1. Ver inventario")
    print("2. Vender producto (salida de inventario)")
    print("3. Agregar o reabastecer producto")
    print("4. Salir")
    
    opcion = input("Elige una opción (1-4): ")

    if opcion == '1':
        respuesta = input("¿Quieres ver el inventario? (si/no): ").lower()
        if respuesta == 'si':
            print("\n--- Inventario actual ---")
            for producto, cantidad in inventario.items():
                print(f"{producto}: {cantidad}")
        else:
            print("Ok, no se mostrará el inventario.")

    elif opcion == '2':
        producto_vendido = input("\n¿Qué producto va a comprar? ")
        if producto_vendido in inventario:
            try:
                cantidad_vender = int(input(f"¿Cuántos {producto_vendido} desea comprar? "))
                if cantidad_vender <= 0:
                    print("Cantidad inválida.")
                elif inventario[producto_vendido] >= cantidad_vender:
                    inventario[producto_vendido] -= cantidad_vender
                    print(f"Venta realizada. Quedan {inventario[producto_vendido]} {producto_vendido}(s).")
                else:
                    print("No hay suficiente stock.")
            except ValueError:
                print("Por favor ingresa un número válido.")
        else:
            print("Producto no encontrado en el inventario.")

    elif opcion == '3':
        nuevo_producto = input("\n¿Qué producto quieres agregar o reabastecer? ")
        try:
            cantidad_agregar = int(input(f"¿Cuántos {nuevo_producto} agregar? "))
            if cantidad_agregar <= 0:
                print("Cantidad inválida.")
            else:
                if nuevo_producto in inventario:
                    inventario[nuevo_producto] += cantidad_agregar
                else:
                    inventario[nuevo_producto] = cantidad_agregar
                print(f"{nuevo_producto} ahora tiene {inventario[nuevo_producto]} unidades.")
        except ValueError:
            print("Por favor ingresa un número válido.")

    elif opcion == '4':
        with open('inventario.json', 'w') as archivo:
            json.dump(inventario, archivo)
        print("Inventario guardado. ¡Hasta luego!")
        break

    else:
        print("Opción inválida. Intenta de nuevo.")