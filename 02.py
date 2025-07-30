from datetime import datetime
from typing import List

class Producto:
    def __init__(self, id_producto: int, nombre: str, precio: float, stock: int):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.fecha_creacion = datetime.now()

    def reducir_stock(self, cantidad: int) -> bool:
        if self.stock >= cantidad:
            self.stock -= cantidad
            return True
        return False
    
    def __str__(self):
        return f"{self.nombre} - {self.precio} - Stock: {self.stock} - Fecha de registro: {self.fecha_creacion}"

# producto1 = Producto(id_producto=1, nombre="Laptop", precio=1500.00, stock=10)
# print(producto1)

# otroProducto = Producto(id_producto=30, nombre="Monitor LG 21p", precio=200.00, stock=20)
# print(otroProducto)

# # Reducir stock
# exito = producto1.reducir_stock(3)
# print(f"¿Reduccion exitosa?", exito)
# print(producto1)

# exito = producto1.reducir_stock(20)
# print(f"¿Reduccion exitosa?", exito)
# print(producto1)

# exito = otroProducto.reducir_stock(5)
# print(f"¿Reduccion exitosa?", exito)
# print(otroProducto)

class CarritoCompras:
    def __init__(self, usuario_id: int):
        self.usuario_id = usuario_id
        self.productos: List[dict] = []
        self.fecha_creacion = datetime.now()

    def agregar_producto(self, producto: Producto, cantidad: int) -> bool:
        if producto.stock >= cantidad:
            item = {
                'producto': producto,
                'cantidad': cantidad,
                'precio_unitario': producto.precio
            }
            self.productos.append(item)
            return True
        return False

    def calcular_total(self) -> float:
        total = 0
        for item in self.productos:
            total += item['precio_unitario'] * item['cantidad']
        return total
    
    def obtener_resumen(self) -> str:
        resumen = f"Carrito de compras del usuario {self.usuario_id}:\n"
        for item in self.productos:
            producto = item['producto']
            cantidad = item['cantidad']
            precio_unitario = item['precio_unitario']
            subtotal = item['precio_unitario'] * cantidad
            resumen += f" - {producto.nombre} x {cantidad} - Precio unitario: {precio_unitario} = ${subtotal:.2f}\n" #imprimir con 2 decimales :.2f
        resumen += f"Total: ${self.calcular_total():.2f}"
        return resumen
    
    def confirmar_compra(self):
        for item in self.productos:
            producto = item['producto']
            cantidad = item['cantidad']
            producto.reducir_stock(cantidad) 

#crear tres objetos de la clase producto
producto1 = Producto(1, "Laptop", 1500.0, 10)
producto2 = Producto(2, "Mouse", 25.0, 50)
producto3 = Producto(3, "Teclado", 45.0, 30) 

#crear un objeto de la clase CarritoCompras
carrito = CarritoCompras(usuario_id=1001)

#usando el objeto para llamar al metodo agregar_producto
carrito.agregar_producto(producto1, 1) #agregar 1 laptop
carrito.agregar_producto(producto2, 2) #agregar 2 mouse
carrito.agregar_producto(producto3, 1) #agregar 1 teclado

total = carrito.calcular_total()
print(f"Total del carrito: ${total:.2f}") 

print(carrito.obtener_resumen())

# confirmar compra directamente desde el objeto
carrito.confirmar_compra()

# verificar si cambio el stock
print(producto1)
print(producto2)
print(producto3)