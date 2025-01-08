class Customer:
    """
    Clase que representa un cliente de la tienda.
    """

    def __init__(self, nombre, email):
        """
        Inicializa un cliente con nombre, email y compras vacías.

        Args:
            nombre (str): Nombre del cliente.
            email (str): Correo electrónico del cliente.
        """
        self.nombre = nombre
        self.email = email
        self.compras = {}

    def agregar_compra(self, producto, cantidad, costo_total):
        """
        Agrega una compra al historial del cliente.

        Args:
            producto (str): Nombre del producto.
            cantidad (int): Cantidad comprada.
            costo_total (float): Costo total de la compra.
        """
        if producto in self.compras:
            self.compras[producto]['cantidad'] += cantidad
            self.compras[producto]['costo_total'] += costo_total
        else:
            self.compras[producto] = {'cantidad': cantidad, 'costo_total': costo_total}

    def __str__(self):
        """Representación textual del cliente."""
        return f"Cliente: {self.nombre} - Email: {self.email}"
