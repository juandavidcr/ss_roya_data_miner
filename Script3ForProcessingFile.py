#!/usr/bin/env python
# decoding: utf-8
#
# 
# Script que separa la información de los txt
#
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

import re
from datetime import date
import mysql.connector

#     datos para conectarse a la BD
#     host='localhost',
#     user='root',
#     password='',
#     database='climatologia_diaria'
# 
# #

midb =mysql.connector.connect(
    host='localhost',
    user='root',
    password='psytranc3',
    database='climatologia_diaria',
    auth_plugin='mysql_native_password'
)
#dar formato de entrada de la base de datos
def createFecha(aaaa,mm,dd):
    fecha=date(int(aaaa),int(mm),int(dd))
    print(fecha)
    #return fecha
# ec_num_estacion=[]
cursor=midb.cursor()
# resultadoMunicipioId = 
#definicion de constantes
null=None
humedadRelativa=None
Estado_ID=30
archivo = open("./newfile.txt")
#query de ejemplo
#sqlQueryMunicipio = 'INSERT INTO Municipio (estado_id,nombre_mun) values (%s,%s)'
#sqlOrg = 'INSERT INTO Organismo (nombre_org) values(%s)'
#createFecha('2022','05','22')
#sql = 'INSERT INTO Estacion_climatologica (num_estacion,nombre_estacion, situacion, municipio_id, organismo_id, latitud, longitud, altitud_msnm, emision_fecha) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
#valuesMet = (30012,'ATZALAN','OPERANDO',1,1,'019.789','-097.246','1,697 msnm',date(2020,4,6))

#definicion de lista de data 
i = 1
listaMun=[]
listaOrg=[]
listaEstaciones=[]
listaNombreEstaciones=[]
listaSituacion=[]
listaLat=[]
listaLon=[]
listaAlt=[]
#lectura linea por linea encontrando el texto de interés y almacenandolo en una lista
for linea in archivo:
    linea = linea.rstrip("\\n") 
    listResult=re.split(r'\s+', linea) 
    print(listResult)
    if(listResult[0]=='LONGITUD'):
        listaLon.append(listResult[2])
    if(listResult[0]=='LATITUD'):
        listaLat.append(listResult[2])
        #print(listaLon)
    if(listResult[0]=='ORGANISMO'):
        #SELECT id_organismo FROM Organismo WHERE nombre_org='CONAGUA-DGE';
        #select id_organismo from Organismo where nombre_org='CONAGUA-SMN';
        print("---organismo-list---")
        listaOrg.append(listResult[2])
        #valuesOrg = [(listResult[2])]
        #cursor.execute(sqlOrg, valuesOrg)
        print(listaOrg)
    # Armar query de Estacion Climatologica
    if(listResult[0]=='MUNICIPIO'):
        sqlListMunNombre = "SELECT nombre_mun FROM Municipio;"
        cursor.execute(sqlListMunNombre)
        resultadoMunNombre=cursor.fetchall()
        numMunicipios = len(resultadoMunNombre)
        print("resultadoMunNombre: ",resultadoMunNombre)
        for j in range(numMunicipios):
            sqlSelectMunId="SELECT id_municipio FROM Municipio WHERE nombre_mun="+str(resultadoMunNombre[j])+";";
            cleaningx = sqlSelectMunId.replace(",)", "")
            cleaningx2=cleaningx
            cleanedSQL=cleaningx2.replace("(","")
            print(cleanedSQL)
            cursor.execute(cleanedSQL)
            resultadoMunId=cursor.fetchall()
            #numMunId=len(resultadoMunId)
            #print("Municipio Id: ",resultadoMunId)
            cleaningy1 = str(resultadoMunId).replace("[","",1)
            cleanedy2=cleaningy1.replace("(","")
            cleanedMunId=cleanedy2.replace(",)","",1)
            MunicipioIdCleaned=cleanedMunId.replace("]","",1)
            print("cleanedMunId: ",MunicipioIdCleaned)

            #print("numMunId: ",numMunId)
            #print("Municipio existe id: ",sqlSelectMunId)
            #print("Municipio existe id: ",resultadoMunId)
        #values = (Estado_ID,listResult[2])
        #cursor.execute(sqlQueryMunicipio, values)
        listaMun.append(listResult[2])
        print("Municipios: ",listaMun)
    if(listResult[0]=='ESTACION'):
        print("Existe Estacion")
        listaEstaciones.append(listResult[2])
        print(listaEstaciones)
    if(listResult[0]=='NOMBRE'):
        print("Existe nombre-estacion")
        listaNombreEstaciones.append(listResult[2])
        print(listaNombreEstaciones)
    if(listResult[0]=='ALTITUD'):
        listaAlt.append(listResult[2]+' '+listResult[3])
        print(listaAlt)
    #midb.commit()
    #print (cursor.rowcount)
    #if(type(linea)=='str'):
    #   ec_num_estacion=re.split(r'\s+', linea)
        #if(ec_num_estacion[0]):
        #lista2 = ec_num_estacion.copy()
    #print(" %4d: %s" % (i, linea))
    i+=1
archivo.close()


