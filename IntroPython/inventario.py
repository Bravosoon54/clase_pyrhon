# 1 ver inventario
# 2 salida de inmventario se le pregunta al usuario que producto va a comprar para restar del inventario 
# 3 agregar producto al inventario y aumentar cantidad disponible
import json
#leer inventario guardado
try:
    with open('inventario.json', 'r') as archivo:
        inventario = json.load(archivo)
except FileNotFoundError:
    inventario = {
    'pera':10,
    'naranja':8,
    'coco': 5
}

# ver inventario al seleccionar si/no
respuesta = input('Ver inventario? (si/no): ').lower()
if respuesta == 'si':
    for fruta, cantidad in inventario.items():
        print(f'Fruta: {fruta}, Cantidad: {cantidad}')
else:
    print('no hay nada que ver entonces')

# vender, salida de inventario, compra
producto_vendido = input('¿Qué producto deseas comprar? ')
if producto_vendido in inventario:
    cantidad_vender = int(input('¿Cuántos productos deseas comprar? '))
    if inventario [producto_vendido] >= cantidad_vender:
        inventario [producto_vendido] -= cantidad_vender
        print(f"venta realizada. quedan {inventario[producto_vendido]}, {producto_vendido}(s).")
    else:
        print(f"No hay suficiente {producto_vendido} para la venta.")
else:
    print(f"No tenemos {producto_vendido} en stock.")
    
#3 agregar producto al inventario o aumentar cantidad de producto
nuevo_producto = input('¿Qué producto deseas agregar al inventario o reabastecer? ')
cantidad_agregar = int(input(f'¿Cuántos {nuevo_producto} deseas agregar? '))
if nuevo_producto in inventario:
    inventario[nuevo_producto] += cantidad_agregar
else:
    inventario[nuevo_producto] = cantidad_agregar
print (f'Inventario actualizado')
for producto, cantidad in inventario.items():
    print(f'Producto: {producto}, Cantidad: {cantidad}')
    
#guardar cambios
with open('inventario.json', 'w') as archivo:
    json.dump(inventario, archivo)