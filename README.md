# negocio_facil
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
 - SO: Multiplataforma
 - Lenguaje: Python 3.9.5
 - Tipo de archivos a manejar: .csv
 - Entrada de usuario: Por consola

### **Entrada del Sistema:**

El programa inicialmente le pedira al usuario, por consola, crear un perfil de su negocio que se leera desde un archivo .csv ("perfil_negocio.csv") cada vez que se inicie el programa.
Luego el sistema automáticamente buscará si hay algun archivo .csv con la lista de precios local ("lista_local.csv"), o en caso contrario un archivo de proveedor ("lista_proveedor1.csv").
Al crearse la lista local de productos el usuario debera ingresar el porcentaje de aumento que quiere aplicarle a todos los productos en general.
A continuación el usuario debera ingresar por consola la opción del menú que desee ejecutar, donde tiene las funciones de:
 1. Buscar producto: Aquí el usuario debe elegir el parametro de buscqueda del producto, y en caso de que aparezca tiene varias funciones de interactuar con dicho producto:
    1. Marcar stock como faltante.
    2. Editar producto.
    3. Eliminar producto.
 2. Agregar nuevo producto a la lista local: Aquí el usuario ingresa los datos necesarios para incluir un nuevo producto a la lista.
 3. Actualizar precios: Aquí se vuelve a leer un archivo del proveedor nuevo y actualiza los datos de los productos.
 4. Controlar stock: Aquí el usuario puede saber qué productos están con stock faltante.

### **Salida del Sistema:**

El programa genera principalmente varios archivos de salida en formato .csv:
    * Perfil del Negocio: Es un archivo con los datos del negocio. ("perfil_negocio.csv")
    * Lista Local de Productos: Es un archivo con la lista de productos del negocio, ya con sus precios finales. ("lista_local.csv")
    * Stock Faltante: Es un archivo con la lista de productos marcados como faltantes, lista para enviarsela al proveedor y hacer el pedido. ("stock_faltante.csv")

Ademas a medida que el usuario avanza en el programa los resultados y pedidos que va haciendo se muestran por la pantalla de la consola.
