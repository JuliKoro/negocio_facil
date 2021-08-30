# ¡Mi Negocio Fácil! (Inicial/Prototipo)
Proyecto inicial en Python para administrar algunas funciones básicas de un negocio comercial.

## Especificación de requisitos:

### **Requisitos Funcionales:**
 - Tener un menú inicial por donde se pueda elegir qué hacer.
 - Poder leer los archivos de listas de precios de proveedores.
 - Calcular el precio de venta final de los productos y guardarlo en un archivo.
 - Poder buscar cualquier próducto y saber su precio.
 - Poder agregar un producto con toda su información a la lista de productos del negocio propio.
 - Poder editar los datos de cualquier producto.
 - Poder eliminar cualquier producto.
 - Poder actualizar los precios a partir de un nuevo archivo del proveedor.
 - Poder marcar productos con stock faltante y generar un arhivo con los productos que haya que pedir a los proveedores.

### **Requisitos No Funcionales:**
 - _SO:_ Multiplataforma
 - _Lenguaje:_ Python 3.9.5
 - _Tipo de archivos a manejar:_ .csv
 - _Entrada de usuario:_ Por consola

### **Entrada del Sistema:**

El programa inicialmente le pedira al usuario, por consola, crear un perfil de su negocio que se leera desde un archivo .csv ("perfil_negocio.csv") cada vez que se inicie el programa.
Luego el sistema automáticamente buscará si hay algun archivo .csv con la lista de precios local ("lista_local.csv"), o en caso contrario un archivo de proveedor ("lista_proveedor1.csv").
![lista_proveedor1.csv](/screenshots/lista_proveedor1_ss.png)

Al crearse la lista local de productos el usuario debera ingresar el porcentaje de aumento que quiere aplicarle a todos los productos en general.
A continuación el usuario debera ingresar por consola la opción del menú que desee ejecutar, donde tiene las funciones de:
 1. **Buscar producto:** Aquí el usuario debe elegir el parametro de buscqueda del producto, y en caso de que aparezca tiene varias funciones de interactuar con dicho producto:
    1. Marcar stock como faltante.
    2. Editar producto.
    3. Eliminar producto.
 2. **Agregar nuevo producto a la lista local:** Aquí el usuario ingresa los datos necesarios para incluir un nuevo producto a la lista.
 3. **Actualizar precios:** Aquí se vuelve a leer un archivo del proveedor nuevo y actualiza los datos de los productos.
 4. **Controlar stock:** Aquí el usuario puede saber qué productos están con stock faltante.

### **Salida del Sistema:**

El programa genera principalmente varios archivos de salida en formato .csv:
 * **Perfil del Negocio:** Es un archivo con los datos del negocio. ("perfil_negocio.csv")
![perfil_negocio.csv](/screenshots/perfil_negocio_ss.png)

 * **Lista Local de Productos:** Es un archivo con la lista de productos del negocio, ya con sus precios finales. ("lista_local.csv")
![lista_local.csv](/screenshots/lista_local_ss.png)

 * **Stock Faltante:** Es un archivo con la lista de productos marcados como faltantes, lista para enviarsela al proveedor y hacer el pedido. ("stock_faltante.csv")
![stock_faltante.csv](/screenshots/stock_faltante_ss.png)

Ademas a medida que el usuario avanza en el programa los resultados y pedidos que va haciendo se muestran por la pantalla de la consola.

### **Notas:**

Este prototipo/proyecto de Python Inicial se usará como esqueleto de un proyecto mucho más desarrollado y con herramientas más sofisticadas, cómo bases de datos, JSON, Flask, etc.
