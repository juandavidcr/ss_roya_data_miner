import re
from datetime import date



def createFecha(aaaa,mm,dd):
    fecha = date(int(aaaa),int(mm),int(dd))
    #print(fecha)
    return fecha

patternDeFechas = '^(0?[1-9]|[12][0-9]|3[01])[\/\-](0?[1-9]|1[012])[\/\-]\d{4}$'
patternDePrecip = '[0-9]*\.?[0-9]*'
patternDeEvap = '(\w*)|([0-9]*\.?[0-9]*)'
patternTmaxyTmin='(\w*)|([0-9]*\.?[0-9]*)'

listaDeFechas = []
listaPrecipitaciones=[]
listaEvaporacion=[]
listTmax=[]
listTmin=[]
nuevaLista=[]
archivo = open("./coatepecdata.txt")
#archivo = open("./brionesdata.txt")
for linea in archivo:
    linea = linea.rstrip("\\s") 
    listResult=re.split(r'\s+', linea)
    #print(listResult)
    resultFecha = re.match(patternDeFechas, listResult[0])
    resultPrecipitacion=re.match(patternDePrecip, listResult[1])
    resultEvaporacion=re.match(patternDePrecip, listResult[2])
    resultTmax=re.match(patternTmaxyTmin, listResult[3])
    resultTmin=re.match(patternTmaxyTmin, listResult[4])
    if resultFecha:
        listaDeFechas.append(listResult[0])        
    if resultPrecipitacion:
        listaPrecipitaciones.append(listResult[1])        
    if resultEvaporacion:
        listaEvaporacion.append(listResult[2])
    if resultTmax:
        listTmax.append(listResult[3])
    if resultTmin:
        listTmin.append(listResult[3])
#print(listaDeFechas,len(listaDeFechas))
#print(listaPrecipitaciones,len(listaPrecipitaciones))
#print(listaEvaporacion,len(listaEvaporacion))
#print(listTmax,len(listTmax))
#print(listTmin,len(listTmin))
#print(type(listaDeFechas))
strFecha = str(listaDeFechas[0])
#print(strFecha)
#print(type(strFecha))
nuevaLista =strFecha.split('/')
print()
dia=nuevaLista[0]
mes=nuevaLista[1]
anyo=nuevaLista[2]
fechaa = createFecha(anyo,mes,dia)
#INSERT INTO `climatologia_diaria`.`Datos_Climatologicos` (`id_climatologicos`, `fecha`, `precipitacion_mm`, `evaporacion_mm`, `tmax`, `tmin`, `humedad_relativa`, `estacion_id`) VALUES ('2', '1999-01-01', '0.0', '', '12.0', '11.0', '', '1');
print(f"INSERT INTO Datos_Climatologicos (fecha, precipitacion_mm,evaporacion_mm,tmax,tmin,humedad_relativa,estacion_id) VALUES('{fechaa}',")
print("""
INSERT INTO `climatologia_diaria`.`Datos_Climatologicos` ( `fecha`, `precipitacion_mm`, `evaporacion_mm`, `tmax`, `tmin`, `humedad_relativa`, `estacion_id`) 
VALUES ( '"+fechaa+"')
""")