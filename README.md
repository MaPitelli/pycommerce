# 🛍️ Tienda Online con Python (POO y Modularidad)

![PyCommerce](assets/banner.png)

Este es un proyecto de una **tienda online** desarrollado en Python, con un enfoque profesional y modular utilizando **Programación Orientada a Objetos (POO)**. La aplicación permite gestionar un inventario de productos, clientes y ventas de forma eficiente y escalable.

---

## 📦 Estructura del Proyecto

El proyecto está organizado de forma modular para mejorar la legibilidad, el mantenimiento y la escalabilidad del código:

```
pycommerce/
├── assets/             # Imágenes utilizadas en el proyecto
├── main.py             # Punto de entrada de la aplicación
├── store.py            # Clase principal TiendaOnline
├── customer.py         # Gestión de clientes con la clase Customer
├── product.py          # Gestión de productos con la clase Product
├── utils.py            # Funciones auxiliares (validación de email)
├── README.md           # Documentación del proyecto
```

---

## 🎯 Características

- ✅ **Gestión de Inventario:** Agregar, eliminar, actualizar y visualizar productos con control total del inventario.  
- ✅ **Gestión de Clientes:** Registrar y consultar clientes de forma organizada.  
- ✅ **Realización de Compras:** Control de stock y registro detallado de ventas.  
- ✅ **Historial de Compras:** Registro individual de compras por cliente.  
- ✅ **Cálculos Automáticos:** Valor total del inventario y ventas totales calculados automáticamente.  
- ✅ **Validación de Email:** Incluye una función para validar correos electrónicos con expresiones regulares (`regex`).  
- ✅ **Modularidad:** Separación clara de responsabilidades mediante múltiples módulos.  
- ✅ **Orientación a Objetos:** Uso de clases `TiendaOnline`, `Product` y `Customer` con `docstrings` explicativos.  

---

## 🚀 Instalación y Ejecución

Para ejecutar este proyecto en tu máquina local, sigue estos pasos:

1. Clona este repositorio:  
   ```bash
   git clone https://github.com/MaPitelli/pycommerce.git
   cd pycommerce
   ```
2. Asegúrate de tener **Python 3.8+** instalado.  
3. Ejecuta el archivo principal:  
   ```bash
   python main.py
   ```
4. ¡Listo! 🎉 La tienda estará lista para gestionar productos, clientes y realizar ventas.

---

## 📚 Ejemplos de Uso

### 📦 Agregar un Producto
```python
tienda.agregar_producto("Camiseta", 15.0, 50)
```

### 👥 Agregar un Cliente
```python
tienda.agregar_cliente("Juan Pérez", "juan@example.com")
```

### 🛒 Realizar una Compra
```python
tienda.realizar_compra("Juan Pérez")
```

### 📊 Calcular Valor del Inventario
```python
tienda.calcular_valor_inventario()
```

---

## 🧩 Clases Implementadas

### `Product` (Clase Producto)
- Representa un producto de la tienda con atributos: `nombre`, `precio` y `cantidad`.  
- Métodos: `__init__()` y `__str__()`.

### `Customer` (Clase Cliente)
- Representa un cliente de la tienda con atributos: `nombre`, `email` y un historial de compras (`compras`).  
- Métodos: `agregar_compra()` y `__str__()`.

### `TiendaOnline` (Clase Principal)
- Gestión centralizada de la tienda: inventario, clientes y ventas totales.  
- Métodos: 
   - `agregar_producto()`
   - `ver_inventario()`
   - `buscar_producto()`
   - `actualizar_stock()`
   - `eliminar_producto()`
   - `calcular_valor_inventario()`
   - `agregar_cliente()`
   - `realizar_compra()`
   - `ver_clientes()`
   - `ver_compras_cliente()`
   - `calcular_ventas_totales()`  

---

## 🛠️ Mejoras Futuras
- [ ] Implementar persistencia de datos con base de datos SQLite.  
- [ ] Crear una interfaz gráfica con `tkinter` o `PyQt`.  
- [ ] Agregar un sistema de descuentos y promociones.  
- [ ] Implementar exportación de datos a formatos CSV o JSON.  

---

## 🤝 Feedback y Contribución

¡Tu opinión es importante! Si encuentras algún error o tienes sugerencias para mejorar este proyecto, no dudes en abrir un **issue** o enviar un **pull request** al repositorio.

---

## 📧 Contacto
- **Autor:** [Maíra Pitelli](https://github.com/MaPitelli)  
- **Correo:** mairapitelli@hotmail.com  
- **LinkedIn:** [Perfil de LinkedIn](https://www.linkedin.com/in/mairapitelli/)  

---