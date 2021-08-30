#!/usr/bin/env python
'''
Negocio Fácil [Python]
(Prototipo inicial)
---------------------------
Descripción:
Programa creado como proyecto inicial para administrar un negocio comercial 
en diversas funciones.
Para más información leer el archivo "README.md"
'''

__author__ = "Julián Andrés Koroluk"
__email__ = "julian.koroluk@outlook.com"
__version__ = "0.4"

import csv
from os import write


# Defino el diccionario de manera global ya que se usa en distintas funciones.
perfil = {
    'nombre': 'Nombre',
    'rubro': 'Rubro',
    'cuil': 00000000,
    'localidad': 'Localidad',
    'provincia': 'Provincia',
    'fecha_inicio': 'hoy'
}

iva = 0.21 # Variable global del iva para calcular porcentajes


def crear_perfil():
    '''Crear perfil de usuario

    Se crea el perfil de un único usuario, pidiendole sus datos por consola y 
    luego los almacena en un archivo (perfil_negocio.csv).
    '''
    global perfil # Para modificar el diccionario de manera global

    print('A continuación le pediremos datos sobre su negocio para poder crear',
    ' su perfil.\n')
    perfil['nombre'] = input('Nombre del negocio: ')
    perfil['rubro'] = input('Rubro: ')
    perfil['cuil'] = input('CUIL / CUIT: ')
    perfil['provincia'] = input('Provincia: ')
    perfil['localidad'] = input('Localidad: ')
    perfil['fecha_inicio'] = input('Fecha de apertura: ')
    print('¡Perfil completo!')

    header = list(perfil.keys())
    csvfile = open('perfil_negocio.csv', 'w', newline='')
    writer = csv.DictWriter(csvfile, fieldnames=header)
    writer.writeheader()
    writer.writerow(perfil)
    csvfile.close()
    print('¡Perfil guardado!')
    return perfil


def cargar_perfil():
    '''Cargar perfil de usuario

    Carga los datos de un único perfil previamente guardados en el archivo 
    "perfil_negocio.csv"; en caso de que no exista, envía al usuario a crearse uno nuevo 
    (crear_perfil).
    '''
    global perfil

    try:
        archivo = open('perfil_negocio.csv')
        perfil = list(csv.DictReader(archivo))
        archivo.close()
        print('¡Archivo cargado con éxito!')
    except:
        print('Error de archivo.\nTendrá que crear un nuevo perfil.')
        crear_perfil()


def cargar_proveedor():
    '''Cargar lista de precios del proveedor

    Carga los datos de los productos desde un archivo csv proporcionado por un proveedor.
    En caso de no encontrar el archivo imprime un mensaje de error.
    Y retorna un diccionario con estos datos:
    'producto' -> Nro. del producto
    'cod_barra' -> Código de barras del producto
    'descripcion' -> Descripción del producto
    'precio' -> Precio del producto del proveedor (con IVA)
    'fecha_mod' -> Fecha de última modificación del precio
    '''
    try:
        csvfile = open('lista_proveedor1.csv')
        data = list(csv.DictReader(csvfile, delimiter=";")) # Archivo separado por ";"
        csvfile.close()
        print(f"¡Se han cargado {len(data)} productos con éxito!")
        for i in range(len(data)): # Convertir 'precio' en float
            data[i]['precio'] = data[i]['precio'].replace('$','')
            data[i]['precio'] = data[i]['precio'].replace('.','')
            data[i]['precio'] = data[i]['precio'].replace(',','.')
            data[i]['precio'] = float(data[i]['precio'])
        return data
    except:
        print('Error de archivo.\nNo se encontró la lista del proveedor.')
        return False


def cargar_local():
    '''Cargar lista de productos local
    
    Carga los datos de los productos a la venta del local desde un archivo csv creado anteriormente.
    En caso de no encontrar el archivo imprime un mensaje y continua creando un archivo.
    Y retorna un diccionario con estos datos:
    'producto' -> Nro. del producto
    'cod_barra' -> Código de barras del producto
    'descripcion' -> Descripción del producto
    'precio' -> Precio del producto del proveedor (sin IVA)
    'fecha_mod' -> Fecha de última modificación del precio
    'precio_iva' -> Precio de cada producto con el aumento de IVA (21%)
    'precio_final' -> 'precio_iva' con el aumento de 'ganancia'
    'stock' -> 'True' si hace falta pedir, 'False' no hace nada
    '''
    try:
        csvfile = open('lista_local.csv')
        data = list(csv.DictReader(csvfile))
        csvfile.close()
        print(f"¡Se han cargado {len(data)} productos locales con éxito!")
        return data
    except:
        print('No se ha encontrado ningún archivo de productos locales.\n',
        'A continuación se creará uno a partir de una lista del proveedor.')
        return False


def precio_final(lista_proveedor):
    ''' Calcular precio final de venta

    Calcula el precio con el IVA (21%) y el precio sumando el porcentaje de ganancia deseado
    por el usuario de cada producto de la lista del proveedor.
    Genera un nuevo archivo con estas dos nuevas columnas:
    'iva' -> precio + 21%
    precio_venta -> 'iva' + ganancia%
    
    Retorna una lista de diccionarios con las nuevas 'keys' y 'values' ('lista_final')

    @param lista_proveedor Diccionario con la lista de productos extraido del archivo del proveedor.
    '''
    print('A la información de cada producto se le agregará el 21"%" del IVA y el ',
    '"%" de ganancia para el precio final.')
    # Genero una lista sumando el 21% al precio de cada producto
    precio_iva = [lista_proveedor[x]['precio']+lista_proveedor[x]['precio']*iva for x in range(len(lista_proveedor))]
    # Convierto la lista de precios a vector para operar más rapidamente.
    #precio_prov_vec = np.array(precio_prov)
    # Calculo y sumo el porcentaje del IVA (21%) a cada uno de los precios
    #precio_iva = np.percentile(precio_prov_vec, 21)
    while True:
        ganancia = int(input('Indique el "%" de ganancia que desea:\n'))
        try:
            # Genero una lista sumando el % de 'ganancia' a 'precio_iva'
            precio_final = [precio_iva[i]+precio_iva[i]*(ganancia/100) for i in range(len(precio_iva))]
            break
        except:
            print('Ingreso inválido. Ingrese un número, por favor.')
            continue
    print(f'¡Recarga de precios con éxito!\nSe recargo un {ganancia+21}% al precio del proveedor.')
    lista_final = lista_proveedor # Se crea una nueva lista copiada de la del proveedor
    for i in range(len(lista_final)):
        '''Se agragan tres nuevas columnas:
        'precio_iva' -> Precio de cada producto con el aumento de IVA (21%)
        'precio_final' -> 'precio_iva' con el aumento de 'ganancia'
        'stock' -> 'True' si hace falta pedir, 'False' no hace nada
        '''
        lista_final[i]['precio_iva'] = precio_iva[i]
        lista_final[i]['precio_final'] = precio_final[i]
        lista_final[i]['stock'] = False
    
    # Guarda la lista nueva local en un archivo .csv ('lista_local.csv')
    csvfile = open('lista_local.csv', 'w', newline='')
    header = list(lista_final[0].keys())
    writer = csv.DictWriter(csvfile, fieldnames=header)
    writer.writeheader()
    writer.writerows(map(lambda x: lista_final[x], range(len(lista_final))))
    csvfile.close()

    return lista_final


def editar_producto(lista_local, search):
    '''Editar valores de un producto
    
    Modifica los valores de 'producto', 'cod_barra', 'descripcion' y 'precio_final' de
    la lista de diccionarios de 'lista_local' que contiene los productos locales.
    Retorna la lista modificada.

    @param lista_local Lista de diccionarios con los productos locales
    @param search Índice del producto buscado en lista_local, valor devuelto por 'buscar_producto()'
    '''
    while True:
        param = int(input('Elija qué parametro del producto quiere editar.\n1.Editar nro. producto\n2.Editar codigo de barras\n3. Editar descripción.\n4. Editar precio final.\n0. Salir\n'))
        if param == 1:
            nro_prod = input('Ingrese nuevo Nro. del producto: ')
            lista_local[search]['producto'] = nro_prod
            print('¡Nro. de producto actualizado!')
        elif param == 2:
            cod_barra = input('Ingrese nuevo código de barras del producto: ')
            lista_local[search]['cod_barra'] = cod_barra
            print('¡Código de barras del producto actualizado!')
        elif param == 3:
            desc = input('Ingrese nueva descripción del producto: ')
            lista_local[search]['descripcion'] = desc
            print('¡Descripción del producto actualizado!')
        elif param == 4:
            precio_final = input('Ingrese nuevo precio final del producto: $')
            lista_local[search]['precio_final'] = precio_final
            print('¡Precio final del producto actualizado!')
        elif param == 0:
            break
        else:
            print('Ingrese una de las opciones, por favor.')
            continue
    
    return lista_local


def eliminar_producto(lista_local, search):
    '''Eliminar producto de la lista local
    
    Elimina el diccionario de la 'lista_local' según el índice pasado por 'buscar_producto()' 
    Retorna la lista ya modificada

    @param lista_local Lista de diccionarios con los productos locales
    @param search Índice del producto buscado en lista_local, valor devuelto por 'buscar_producto()'
    '''
    del lista_local[search]
    print('¡Producto eliminado con éxito!')
    return lista_local


def buscar_producto(lista_local):
    '''Buscar un producto de la lista local

    Busca el diccionario de un producto de la lista 'lista_local'.
    Se puede buscar según el nro. de producto, código de barras o descricpión.
    Cuando el resultado es único se da la opción de editar el producto y se llama a
    la función 'editar_producto(lista_local, search)'

    @param lista_local Lista de diccionarios con los productos locales
    '''
    while True:
        tipo = int(input('A continuación elija cómo quiere buscar el producto:\n1. Nro. Producto\n2. Código de barras\n3. Descripción\n0. Salir\n'))
        if tipo == 1: # Por nro. de producto
            nro_prod = input('Ingrese Nro. del producto: ')
            search = next((i for i, prod in enumerate(lista_local) if prod['producto'] == nro_prod), None)
        elif tipo == 2: # Por código de barras
            cod_barra = input('Ingrese código de barras: ')
            search = next((i for i, prod in enumerate(lista_local) if prod['cod_barra'] == cod_barra), None)
        elif tipo == 3: # Por la descripción
            desc = input('Ingrese la descripción: ')
            search = next((i for i, prod in enumerate(lista_local) if desc in prod['descripcion']), None)
        elif tipo == 0: break
        else: 
            print('Ingrese una opción valida, por favor.')
            continue
        if search != None: # Cuando se encuentra el/los producto/s
            print('¡Producto encontrado!\n', lista_local[search])
            sig = int(input('¿Quiere realizar alguna acción con este producto?\n1. Marcar stock como faltante.\n2. Editar producto.\n3. Eliminar producto.\n0. Salir.\n'))
            if sig == 1: # Marcar stock faltante
                lista_local[search]['stock'] = True
                print('¡Stock marcado como faltante!')
            elif sig == 2: # Editar producto
                editar_producto(lista_local, search)
            elif sig == 3: # Eliminar producto
                eliminar_producto(lista_local, search)
            elif sig == 0: break # Salir
            else:
                print('Ingrese una opción correcta, por favor')
                continue
        else: # Cuando no se encuentra el producto
            print('Producto no encontrado.')
            continuar = int(input('¿Quiere seguir buscando?\n1. Si\n2. No\n'))
            if continuar == 1: continue
            elif continuar == 2: break
            else: print('Ingrese una opción correcta, por favor')
    
    return search


def nuevo_producto(lista_local):
    '''Agregar un nuevo producto a la lista local

    Se ingresan los distintos parametros de un producto y se guarda el diccionario al
    final de la lista.
    Retorna la misma lista pero con el nuevo producto

    @param lista_local Lista de diccionarios con los productos locales
    '''
    producto_nuevo = {} # Dict del nuevo producto a agregar
    print('A continuación agregue los datos necesarios del nuevo producto.\n')
    producto_nuevo['producto'] = input('Ingrese un numero de producto: ')
    producto_nuevo['cod_barra'] = input('Ingrese un código de barras: ')
    producto_nuevo['descripcion'] = input('Ingrese el nombre del producto: ')
    producto_nuevo['precio'] = float(input('Ingrese el precio (sin IVA): '))
    producto_nuevo['precio_iva'] = producto_nuevo['precio'] + (producto_nuevo['precio'] * iva)
    print(f"Precio con IVA de {iva*100}%: ${producto_nuevo['precio_iva']}")
    producto_nuevo['precio_final']  = float(input('Ingrese el precio final: $'))
    stock = input('¿Tiene stock de este producto actualmente?\n1. Si\n2. No')
    if stock == 1 or stock in ['si', 'Si', 'SI']: producto_nuevo['stock'] = False
    elif stock == 2 or stock in ['no', 'No', 'NO']: producto_nuevo['stock'] = True
    else: print('Ingreso invalido.')
    lista_local.append(producto_nuevo)
    print('¡Producto nuevo agregado con éxito!')

    return lista_local


def act_precios(lista_local):
    '''Actualizar productos de la lista local

    Actualiza la lista_local leyendo un archivo nuevo del proveedor, rehusando las funciones
    de 'cargar_proveedor()' y 'precio_final()'
    Retorna la nueva lista local actualizada.

    @param lista_local Lista de diccionarios con los productos locales
    '''
    print('A continuación se cargará el archivo con la lista de precios del proveedor.')
    lista_proveedor = cargar_proveedor()
    if lista_proveedor != False: # Si se cargó bien la lista del proveedor
        print('A continuación se creará el archivo con la lista de precios local.')
        lista_local = precio_final(lista_proveedor)
        return lista_local
    else: print('Sin archivo de proveedor no se puede continuar.\n¡Hasta Luego!')


def controlar_stock(lista_local):
    '''Controlar Stock faltante
    
    Imprime los productos marcados como stock faltante ('stock': True) y los guarda en un archivo de texto
    ("stock_faltante.txt").

    @param lista_local Lista de diccionarios con los productos locales
    '''
    print('A continuación le mostraremos los productos marcados con stock faltante y se guardara en un archivo de texto ',
    'para luego pedirle al proveedor.\nSi quiere marcar un producto debe hacerlo ingresando a "1. Buscar producto" ',
    'desde el menú inicial.')
    # Filtro la lista local con los productos marcados como faltantes (True)
    prod_falta = [lista_local[i] for i in range(len(lista_local)) if lista_local[i]['stock'] == True]
    fo = open('stock_faltante.txt', 'w')
    print('Productos faltantes:')
    fo.write("Productos faltantes:\n")
    for item in prod_falta:
        print(item)
        fo.writelines(item.values())
    fo.flush()
    fo.close()
    print('¡Archivo de stock faltante creado con éxito!')


if __name__ == '__main__':
    print('¡Bienvenido a Tu Negocio Fácil!\nUn programa para ayudarte a administrar',
    'tu negocio en diversas tareas.\n')
    while True:
        inicio = int(input('¿Desea crear un nuevo perfil o cargar desde el archivo?\n(Ingrese la opción que desee)\n1. Crear nuevo perfil.\n2. Cargar perfil.\n'))
        if inicio == 1: 
            crear_perfil()
            break
        elif inicio == 2: 
            cargar_perfil()
            break
        else: 
            print('Ingrese una opción correcta, por favor.')
            continue
    
    print(f"Bienvenido/a {perfil[0]['nombre']}!\n")
    print('A continuación se cargará el archivo con la lista de precios local.')
    lista_local = cargar_local()
    while lista_local == False: # Si no se cargó la lista de precios local
        print('A continuación se cargará el archivo con la lista de precios del proveedor.')
        lista_proveedor = cargar_proveedor()
        if lista_proveedor != False: # Si se cargó bien la lista del proveedor
            print('A continuación se creará el archivo con la lista de precios local.')
            lista_local = precio_final(lista_proveedor)
        else: 
            print('Sin archivo de proveedor no se puede continuar.\n¡Hasta Luego!')
            break
    
    while lista_local != False: # Si se cargó bien una lista local
        print('¿Qué desea hacer?\n(Eliga una opción del menú)\n')
        menu = int(input('1. Buscar producto.\n2. Agregar nuevo producto a la lista local.\n3. Actualizar precios.\n4. Controlar stock.\n0. Salir.\n'))
        if menu == 1:
            buscar_producto(lista_local)
            continue
        elif menu == 2:
            lista_local = nuevo_producto(lista_local)
            continue
        elif menu == 3:
            lista_local = act_precios(lista_local)
        elif menu == 4:
            controlar_stock(lista_local)
        elif menu == 0: 
            print('¡Gracias por usar Tu Negocio Fácil!\n¡Hasta la próxima!')
            break
        else:
            print('Ingrese una opción correcta, por favor.')
            continue

      
