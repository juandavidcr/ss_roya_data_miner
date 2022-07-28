#!/usr/bin/env python
# decoding: utf-8
#
# 
# Script que separa la información de los txt
#
# TODO: CREAR FUNCION DE CREACION DE DATE
# LEER DEL ARCHIVO newfile.txt 
# TODOS LOS DATOS
#
# ESTACION  : 30012
# NOMBRE    : ATZALAN
# ESTADO    : VERACRUZ DE IGNACIO DE LA LLAVE
# MUNICIPIO : ATZALAN
# SITUACI�N : OPERANDO
# ORGANISMO : CONAGUA-SMN
# CVE-OMM   : Nulo
# LATITUD   : 019.789�
# LONGITUD  : -097.246�
# ALTITUD   : 1,697 msnm
# EMISION   : 06/04/2020
#  
# #
import os
import re
import itertools

from pexpect import EOF

directorio = "./bancdata/"
routeF = directorio+"atzalan/atzalan.txt"
routeF2 = directorio+"briones/briones.txt"
routeF3 = directorio+"chicontepec-suspendida/chicontepec.txt"
routeF4 = directorio+"coatepec-suspendida/coatepec.txt"
routeF5 = directorio+"cordoba-suspendida/cordoba.txt"
routeF6 = directorio+"huatusco-suspendida/huatusco.txt"
routeF7 = directorio+"los-tuxtlas/san-andres.txt"
routeF8 = directorio+"los-tuxtlas/santiago-tuxtla.txt"
routeF9 = directorio+"los-tuxtlas/sihuapan.txt"
routeF10 = directorio+"los-tuxtlas/tapalapa.txt"
routeF11 = directorio+"misantla/misantla.txt"
routeF12 = directorio+"papantla/papantla.txt"
routeF13 = directorio+"tezonapa-suspendida/tezonapa-1.txt"
routeF14 = directorio+"tezonapa-suspendida/tezonapa-2.txt"
routeF15 = directorio+"zongolica-suspendida/zongolica.txt"

sufixFile = ".txt"

listaData = [routeF,routeF2,routeF3,routeF4,routeF5,routeF6,routeF7,routeF8,routeF9,routeF10,routeF11,routeF12,routeF13,routeF14,routeF15]

namefile = "data"
listNames = [
    "atzalan"+namefile+sufixFile,
    "briones"+namefile+sufixFile,
    "chicontepec"+namefile+sufixFile,
    "coatepec"+namefile+sufixFile,
    "cordoba"+namefile+sufixFile,
    "huatusco"+namefile+sufixFile,
    "san-andres"+namefile+sufixFile,
    "santiago-tuxtla"+namefile+sufixFile,
    "sihuapan"+namefile+sufixFile,
    "tapalapa"+namefile+sufixFile,
    "misantla"+namefile+sufixFile,
    "papantla"+namefile+sufixFile,
    "tezonapa-1."+namefile+sufixFile,
    "tezonapa-2"+namefile+sufixFile,
    "zongolica"+namefile+sufixFile
]
#se agregan todas las rutas de los archivos a depurar
#Funcion encargada de separar las cabeceras de los datos en bruto
def getInfoDataTable(route):
    print(route)
    if os.path.exists(route):
        with open(route, "r") as text_file:
            #se dividen las cabeceras de los datos de todas las estaciones
            archivo = open("newfile.txt","a")
            #de la linea 4 del archivo se identifica un patron de información de las estaciones que ayudara a crear las tablas de municipio, organismo, Estado de la Republica Mexicana y Estación Climatológica.
            for line in itertools.islice(text_file, 4, 17):
                texto=line
                archivo.writelines(texto)
            archivo.close()
            text_file.close()
    else:
        print('El archivo no existe')

def getInfoData(route):
    print(route)
    if os.path.exists(route):
        with open(route, "r") as text_file:
            #nombre de la estación climatologica a cargar
            for name in listNames:
                archivo = open(name,"a")
                #de la linea 17 en adelante se encuentra la data en bruto por cada estación climatologica dependiendo del numero de líneas por cada archivo
                for line in itertools.islice(text_file, 17, countlines(route)):
                    #print(line)
                    texto=line
                    archivo.writelines(texto)
                #se descubre que debemos cerrar el archivo antes de abrir el siguiente por eso lo mandaba a un solo archivo
                archivo.close() 
            text_file.close()
    else:
        print('El archivo no existe')

def countlines(filein):
    fin = open(filein, "r")
    n=0
    for linea in fin:
        n+=1    
    fin.close()
    print(n)
    return n
#funcion para hacer pruebas de lectura de lineas y escritura de lineas por archivo recibe la rurta del archivo
def printlineas(route):
    print(route)
    if os.path.exists(route):
        datos=[]
        # with open(route, "r") as text_file:
        archivo = open(route)
        file_lines = archivo.readlines()
        for linea in file_lines:
           # datos.append(linea.strip('\n'))
            print(linea)
            #gnerar un diccionario por cada llave de dicc nombre del dicc: Identificacion [ESTACION]= 
            #datos = linea.split(" : ") 
            #obtner llave y valor en el 
            #identificacion[datos[0]] = datos[1] 
            #de que lienas estoy leyendo el archivo
            #validar :\s
            #
            # 1. Leer línea por línea del archivos:
            # 1.1. Comparar si es línea de identificación:
            # -- Si tiene como subcadena alguna de las líneas de 1 a 19:
            # ---Generar el SQL para insertar en la tabla de identificaciones
            # -- Si es línea de datos, debe tener "/"
            # ---Generar el SQL para insertar en la tabla de datos 
            # por cada archivo txt que tengo correr el script de la base
            # insert primero la estacion id
            # convertir 
            # #
    else:
        print('El archivo no existe')
    print(datos) 
     

#Genera elarchivo de los encabezados y el archivo de los datos de cada estación por nombre dejandole un sufijo de la siguiente manera 'nombredelarchivo'+'data'+.txt y newfile.txt contendra las cabeceras de las estaciones para saber el numero de estaciones.
for x in listaData:
    #getInfoDataTable(x)
    getInfoData(x)
