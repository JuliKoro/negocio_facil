#!/usr/bin/env python
'''
Negocio Fácil [Python]
(Prototipo inicial)
---------------------------
Descripcion:
Programa creado como proyecto inicial para administrar un negocio comercial 
en diversas funciones.
Para más información leer el archivo "README.md"
'''

__author__ = "Julián Andrés Koroluk"
__email__ = "julian.koroluk@outlook.com"
__version__ = "0.1"

import csv

# Defino el diccionario de manera global ya que se usa en distintas funciones.
perfil = {
    'nombre': 'Nombre',
    'rubro': 'Rubro',
    'cuil': 00000000,
    'localidad': 'Localidad',
    'provincia': 'Provincia',
    'fecha_inicio': 'hoy'
}


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
        data = list(csv.DictReader(csvfile))
        csvfile.close()
        return data
    except:
        print('Error de archivo.\nNo se encontrò la lista del proveedor.')
        return False


def precio_final():
    pass


if __name__ == '__main__':
    print('¡Bienvenido a Tu Negocio Fácil!\nUn programa para ayudarte a administrar',
    'tu negocio en diversas tareas.\n')
    inicio = 1 # Varialbe por default
    while inicio in range(1,3):
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
    print(f"Bienvenido/a {perfil[0]['nombre']}!")
    menu = 1
    print('A continuación se cargará el archivo con la lista de precios del proveedor.')
    lista_proveedor = cargar_proveedor()
    if lista_proveedor != False:
        while menu in range(1, 3):
            print('¿Qué desea hacer?\n(Eliga una opción del menú)\n')
            menu = int(input('1. Generar archivo con precio de venta final.\n2. Agregar nuevo producto a la lista local.\n3. Actualizar precios.\n4. Buscar producto.\n5. Controlar stock.'))
            if menu == 1:
                pass
            elif menu == 2:
                pass
            elif menu == 3:
                pass
            elif menu == 4:
                pass
            elif menu == 5:
                pass
            else:
                print('Ingrese una opción correcta, por favor.')
                continue
    else: print('Sin archivo de proveedor no se puede continuar.\n¡Hastla Luego!')
      
