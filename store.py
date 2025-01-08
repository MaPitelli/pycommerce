from product import Product
from customer import Customer
from utils import validar_email

class TiendaOnline:
    """
    Clase principal que representa una tienda en línea.
    """

    def __init__(self):
        """Inicializa la tienda con inventario, clientes y ventas totales."""
        self.inventario = []
        self.clientes = {}
        self.ventas_totales = 0.0

    def agregar_producto(self, nombre, precio, cantidad):
        """
        Agrega un producto al inventario o actualiza su cantidad si ya existe.
        """
        for producto in self.inventario:
            if producto.nombre == nombre.title() and producto.precio == precio:
                producto.cantidad += cantidad
                print(f"\nLa cantidad del producto {nombre.title()} ha sido actualizada con éxito.")
                return

        nuevo_producto = Product(nombre, precio, cantidad)
        self.inventario.append(nuevo_producto)
        print(f"El producto '{nombre.title()}' ha sido agregado con éxito.")

    def ver_inventario(self):
        """Muestra todo el inventario."""
        print("\n\t***** INVENTARIO *****\n")
        if self.inventario:
            for producto in self.inventario:
                print(producto)
            return
        print('El inventario no tiene productos.\n')

    def buscar_producto(self, nombre):
        """Busca un producto por nombre."""
        for producto in self.inventario:
            if producto.nombre == nombre.title():
                print(f"\n{producto}")
                return producto
        print(f"\nProducto '{nombre.title()}' no encontrado.")
        return None

    def actualizar_stock(self, nombre, cantidad):
        """Actualiza la cantidad de un producto."""
        producto = self.buscar_producto(nombre)
        if producto:
            if producto.cantidad + cantidad < 0:
                print(f"\nNo es posible reducir el stock de {nombre.title()} por debajo de cero.")
            else:
                producto.cantidad += cantidad
                print(f"Nuevo stock de {nombre}: {producto.cantidad}")

    def eliminar_producto(self, nombre):
        """Elimina un producto del inventario."""
        producto = self.buscar_producto(nombre)
        if producto:
            self.inventario.remove(producto)
            print(f"{nombre.title()} ha sido eliminado del inventario.")

    def calcular_valor_inventario(self):
        """Calcula el valor total del inventario."""
        total = sum(p.precio * p.cantidad for p in self.inventario)
        print(f"\nValor total del inventario: {total}€\n")
        return total

    def agregar_cliente(self, nombre, email):
        """Agrega un cliente al registro, verificando duplicados y el formato del email."""
        nombre = nombre.title()
        if nombre in self.clientes:
            print(f"\nEl cliente '{nombre}' ya está registrado.")
        elif any(cliente.email == email for cliente in self.clientes.values()):
            print("\nEl correo electrónico ya está en uso.")
        elif validar_email(email):
            self.clientes[nombre] = Customer(nombre, email)
            print(f"\nCliente {nombre} agregado con éxito.")
        else:
            print("\nEmail inválido.")

    def realizar_compra(self, nombre_cliente):
        """Permite a un cliente realizar una compra."""
        if nombre_cliente not in self.clientes:
            print("Cliente no registrado.")
            return

        carrito = {}
        while True:
            self.ver_inventario()
            producto = input("Ingrese el nombre del producto a comprar (o 'salir'): ").title()
            if producto.lower() == 'salir':
                break
            cantidad = int(input("Cantidad a comprar: "))
            item = self.buscar_producto(producto)
            if item and item.cantidad >= cantidad:
                item.cantidad -= cantidad
                carrito[producto] = {'precio': item.precio, 'cantidad': cantidad}
            else:
                print("Cantidad insuficiente o producto no encontrado.")

        total = sum(item['precio'] * item['cantidad'] for item in carrito.values())
        print(f"Total a pagar: {total}€")
        self.ventas_totales += total
        for producto, detalles in carrito.items():
            self.clientes[nombre_cliente].agregar_compra(producto, detalles['cantidad'], detalles['precio'] * detalles['cantidad'])

    def ver_clientes(self):
        """Muestra la lista de clientes."""
        print("\n\t***** CLIENTES *****\n")
        if self.clientes:
            for cliente in self.clientes.values():
                print(cliente)
        else:
            print("No hay clientes registrados.")

    def ver_compras_cliente(self, nombre_cliente):
        """Muestra el historial de compras de un cliente."""
        cliente = self.clientes.get(nombre_cliente)
        if cliente:
            print(f"Historial de compras de {nombre_cliente}: {cliente.compras}")
        else:
            print("Cliente no encontrado.")

    def calcular_ventas_totales(self):
        """Muestra las ventas totales de la tienda."""
        print(f"Ventas totales: {self.ventas_totales}€")
