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

cursor=midb.cursor()
#TODO convertir datos antes de insertar, leer fecha con el metodo date parseados en num, 
# ORDEN DE INSERCIÓN: MUNICIPIO, ORG,ESTACION CLIMATOLOGICA

#sqlQueryMunicipio = 'INSERT INTO Municipio (estado_id,nombre_mun) values (%s,%s)'
#values = (30,'ATZALAN')

#sqlOrg = 'INSERT INTO Organismo (nombre_org) values(%s)'
#valuesOrg = [('CONAGUA-SMN')]


#sql = 'INSERT INTO Estacion_climatologica (num_estacion,nombre_estacion, situacion, municipio_id, organismo_id, latitud, longitud, altitud_msnm, emision_fecha) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
#valuesMet = (30012,'ATZALAN','OPERANDO',1,1,'019.789','-097.246','1,697 msnm',date(2020,4,6))

#cursor.execute(sqlQueryMunicipio, values)
#cursor.execute(sqlOrg, valuesOrg)
#cursor.execute(sql, valuesMet)

null=None
humedadRelativa=None
#TODO: Los siguientes datos provienen del nombre del municipio, por ejemplo: atzalandata.txt 
sqlInsertDatosClimatologicos='''INSERT INTO Datos_Climatologicos (fecha, precipitacion_mm, 
evaporacion_mm, tmax, tmin, humedad_relativa,estacion_id) values(%s,%s,%s,%s,%s,%s,%s)'''
valuesData = (date(1924,7,19),0,null, 20.0 ,12.0,humedadRelativa,1 )
cursor.execute(sqlInsertDatosClimatologicos, valuesData)
midb.commit()
print (cursor.rowcount)
# sqlQuerOrganismo = 'INSERT INTO Organismo ()'
# sqlQuery = 'INSERT INTO Estacion_climatologica (num_estacion,nombre_estacion,situacion,municipio_id,organismo_id,latitud,longitud,altitud_msnm,emision_fecha) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)' 
# values = ('30012','ATZALAN','OPERANDO',)
# cursor.execute('')

