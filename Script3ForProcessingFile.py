import re
#1.- Detectar los puntos de interes del archivo que se esta leyendo
# ec_num_estacion=[]
archivo = open("./newfile.txt")
# file =open("./atzalandata.txt")
# for line in file:
#     dd=file.readlines(2)
#     linea = line.rstrip("\\s")
#     exStr=line
#     lst = [x for x in linea]

#     print(lst)
#     print(dd,linea,re.findall(r'\\/+', exStr))

    

i = 1
listaEstaciones=[]
listaNombreEstaciones=[]
listaMun=[]
listaOrg=[]
listaLat=[]
listaLon=[]
listaAlt=[]
for linea in archivo:
    linea = linea.rstrip("\\n") 
    listResult=re.split(r'\s+', linea) 
    print(listResult)
    if(listResult[0]=='LONGITUD'):
        listaLon.append(listResult[2])
        print(listaLat)
    if(listResult[0]=='LATITUD'):
        listaLat.append(listResult[2])
        print(listaLon)
    if(listResult[0]=='ORGANISMO'):
        print("organismo-list")
        listaOrg.append(listResult[2])
        print(listaOrg)
    if(listResult[0]=='MUNICIPIO'):
        print("Municipio existe")
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
        print(listaAlt)
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

# sql = 'INSERT INTO Estacion_climatologica (num_estacion,nombre_estacion, situacion, municipio_id, organismo_id, latitud, longitud, altitud_msnm, emision_fecha) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
# valuesMet = (30012,'ATZALAN','OPERANDO',1,1,'019.789','-097.246','1,697 msnm',date(2020,4,6))
# cursor.execute(sql, valuesMet)