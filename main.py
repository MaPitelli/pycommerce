from store import TiendaOnline

def main():
    tienda = TiendaOnline()

    # Ver inventario vacío
    tienda.ver_inventario()

    # Agregar productos
    tienda.agregar_producto("Camisa", 20, 50)
    tienda.agregar_producto("Pantalón", 30, 30)
    tienda.agregar_producto("Zapatos", 50, 20)

    # Ver inventario con productos
    tienda.ver_inventario()

    # Buscar Producto
    tienda.buscar_producto('CAMISA') # Producto que existe
    tienda.buscar_producto('gafas') # Producto que no existe

    # Actualizar stock
    tienda.actualizar_stock('camisa', 200) # Producto que existe
    tienda.actualizar_stock('gafas', 200) # Producto que no existe

    # Eliminar producto
    tienda.eliminar_producto('pantalón') # Producto que existe
    tienda.ver_inventario() # Producto eliminado del inventario
    tienda.eliminar_producto('gafas') # Producto que no existe

    # Mostrar clientes que no existen
    tienda.ver_clientes()

    # Agregar clientes
    tienda.agregar_cliente("Maria", "maria@example.com") # Email valido de cliente nuevo
    tienda.agregar_cliente("Carlos", "@.com") # Email no valido
    tienda.agregar_cliente("Maria", "maria@example.com") # Email valido de cliente existente
    tienda.agregar_cliente("Carlos", "carlos@example.com") # Email valido de cliente nuevo

    # Mostrar clientes existentes
    tienda.ver_clientes()

    # Realizar compras
    tienda.realizar_compra("Maria")
    tienda.realizar_compra("Carlos")

    # Mostrar información
    tienda.ver_clientes()
    tienda.ver_compras_cliente("Maria")
    tienda.ver_compras_cliente("Carlos")
    tienda.calcular_valor_inventario()
    tienda.calcular_ventas_totales()


if __name__ == "__main__":
    main()
