class Product:
    """
    Clase que representa un producto de la tienda.
    """

    def __init__(self, nombre, precio, cantidad):
        """
        Inicializa un nuevo producto.

        Args:
            nombre (str): Nombre del producto.
            precio (float): Precio del producto.
            cantidad (int): Cantidad disponible del producto.
        """
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        """Representación textual del producto."""
        return f"{self.nombre} - Precio: {self.precio}€ - Cantidad: {self.cantidad}"
