#!/usr/bin/env python
# decoding: utf-8
from distutils import text_file
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

def getInfoDataTable(route):
    print(route)
    if os.path.exists(route):
        with open(route, "r") as text_file:
            archivo = open("newfile.txt","a")
            for line in itertools.islice(text_file, 4, 17):
                #print(line)
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
            for name in listNames:
                archivo = open(name,"a")
                for line in itertools.islice(text_file, 17, countlines(route)):
                    #print(line)
                    texto=line
                    archivo.writelines(texto)
                archivo.close() #se descubre que debemos cerrar el archivo antes de abrir el siguiente por eso lo manda aun solo archivo
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
    else:
        print('El archivo no existe')
    print(datos) 
     
for x in listaData:
    #getInfoDataTable(x)
    getInfoData(x)
