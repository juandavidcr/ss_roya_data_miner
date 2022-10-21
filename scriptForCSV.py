import re
from datetime import date



def createFecha(aaaa,mm,dd):
    fecha = date(int(aaaa),int(mm),int(dd))
    #print(fecha)
    return fecha

def getEstacionId():
    hCddEstacionId=3
    print("Entro a estacionId")
    return hCddEstacionId

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
    print(listResult)
    resultFecha = re.match(patternDeFechas, listResult[0])
    resultPrecipitacion=re.match(patternDePrecip, listResult[1])
    resultEvaporacion=re.match(patternDePrecip, listResult[2])
    resultTmax=re.match(patternTmaxyTmin, listResult[3])
    resultTmin=re.match(patternTmaxyTmin, listResult[4])
    if resultFecha:
        #print("Longitud: ---->ListResult[0]",len(listResult[0]))
        listaDeFechas.append(listResult[0])        
    if resultPrecipitacion:
        listaPrecipitaciones.append(listResult[1])        
    if resultEvaporacion:
        listaEvaporacion.append(listResult[2])
    if resultTmax:
        listTmax.append(listResult[3])
    if resultTmin:
        listTmin.append(listResult[3])
print(listaDeFechas,len(listaDeFechas))
#print(listaPrecipitaciones,len(listaPrecipitaciones))
#print(listaEvaporacion,len(listaEvaporacion))
#print(listTmax,len(listTmax))
#print(listTmin,len(listTmin))
# print(type(listaDeFechas))
strFecha = str(listaDeFechas[0])
#print(strFecha)
#print(type(strFecha))
nuevaLista =strFecha.split('/')
#print("nuevaLista",nuevaLista)
dia=nuevaLista[0]
mes=nuevaLista[1]
anyo=nuevaLista[2]
fechaa = createFecha(anyo,mes,dia)
#INSERT INTO `climatologia_diaria`.`Datos_Climatologicos` (`id_climatologicos`, `fecha`, `precipitacion_mm`, `evaporacion_mm`, `tmax`, `tmin`, `humedad_relativa`, `estacion_id`) VALUES ('2', '1999-01-01', '0.0', '', '12.0', '11.0', '', '1');
#primerDatoPrecipMM = str(listaPrecipitaciones[0])
num_primerDatoPrecipMM = float(listaPrecipitaciones[4])
#primerDatoEvMM=str(listaEvaporacion[0])
num_primerDatoEvMM = float(listaEvaporacion[4])
primerDatoTmax=str(listTmax[4])
num_Tmax=float(primerDatoTmax)
primerDatoTmin=str(listTmin[4])
num_Tmin=float(primerDatoTmin)
hr=None
print(f"INSERT INTO Datos_Climatologicos (fecha, precipitacion_mm,evaporacion_mm,tmax,tmin,humedad_relativa,estacion_id) VALUES('{fechaa}',{num_primerDatoPrecipMM},{num_primerDatoEvMM},{num_Tmax},{num_Tmin},{hr},{getEstacionId()})")
# print("""
# INSERT INTO `climatologia_diaria`.`Datos_Climatologicos` ( `fecha`, `precipitacion_mm`, `evaporacion_mm`, `tmax`, `tmin`, `humedad_relativa`, `estacion_id`) 
# VALUES ( '"+fechaa+"')
# """)