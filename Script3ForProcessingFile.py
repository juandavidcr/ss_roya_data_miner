import re
from datetime import date
import mysql.connector

midb =mysql.connector.connect(
    host='localhost',
    user='root',
    password='psytranc3',
    database='climatologia_diaria'
#
#     host='localhost',
#     user='root',
#     password='',
#     database='climatologia_diaria'
# 
# #

)

#1.- Detectar los puntos de interes del archivo que se esta leyendo
# ec_num_estacion=[]
cursor=midb.cursor()
# resultadoMunicipioId = 
null=None
humedadRelativa=None
Estado_ID=30
archivo = open("./newfile.txt")
# file =open("./atzalandata.txt")
# for line in file:
#     dd=file.readlines(2)
#     linea = line.rstrip("\\s")
#     exStr=line
#     lst = [x for x in linea]

#     print(lst)
#     print(dd,linea,re.findall(r'\\/+', exStr))

#sqlQueryMunicipio = 'INSERT INTO Municipio (estado_id,nombre_mun) values (%s,%s)'

#sqlOrg = 'INSERT INTO Organismo (nombre_org) values(%s)'

#sql = 'INSERT INTO Estacion_climatologica (num_estacion,nombre_estacion, situacion, municipio_id, organismo_id, latitud, longitud, altitud_msnm, emision_fecha) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
#valuesMet = (30012,'ATZALAN','OPERANDO',1,1,'019.789','-097.246','1,697 msnm',date(2020,4,6))


i = 1
listaMun=[]
listaOrg=[]
listaEstaciones=[]
listaNombreEstaciones=[]
listaSituacion=[]
listaLat=[]
listaLon=[]
listaAlt=[]
for linea in archivo:
    linea = linea.rstrip("\\n") 
    listResult=re.split(r'\s+', linea) 
    print(listResult)
    if(listResult[0]=='LONGITUD'):
        listaLon.append(listResult[2])
        #print(listaLat)
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
            #print(cleanedSQL)
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
        #    print("Municipio existe id: ",sqlSelectMunId)
            #print("Municipio existe id: ",resultadoMunId)
        #values = (Estado_ID,listResult[2])
        #cursor.execute(sqlQueryMunicipio, values)
        listaMun.append(listResult[2])
        print(listaMun)
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
        #print(listaAlt)
    #midb.commit()
    #print (cursor.rowcount)
    #if(type(linea)=='str'):
    #   ec_num_estacion=re.split(r'\s+', linea)
        #if(ec_num_estacion[0]):
        #lista2 = ec_num_estacion.copy()
    #print(" %4d: %s" % (i, linea))
    i+=1
archivo.close()

# TODO: Encuentra  NombreEstacion
# a = open("./newfile.txt",'r')
# b=a.read()
# nombre_del_munic_ocurrencias_num = "NOMBRE    : "
# count = b.count(nombre_del_munic_ocurrencias_num)
# print (count)


#2.- Indentificar la palabra 'EMISION   : ','DD/MM/AAAA' ESTO PARA INSERTAR EN LA BD EN LA TABLA 
# CREATE TABLE Estacion_climatologica (
#     id_estacion int(20) NOT NULL AUTO_INCREMENT ,
#     num_estacion varchar(50),
#     nombre_estacion varchar(255),
#     situacion varchar(255),
#     municipio_id int(10), #idMunicipio
#     organismo_id int(10), #id_Org
#     latitud varchar(50), 
#     longitud varchar(50),
#     altitud_msnm varchar(50),
#     emision_fecha DATE, #TODO separar la cadena '/' DD/MM/AAAA
#     PRIMARY KEY (id_estacion),
#     FOREIGN KEY (municipio_id) REFERENCES Municipio(id_municipio),
#     FOREIGN KEY (organismo_id) REFERENCES Organismo(id_organismo)
# );


# script de ejemplo funcional: #:- TODO uncomment next line

