import os
import re
import itertools

patternDeFechas = '^(0?[1-9]|[12][0-9]|3[01])[\/\-](0?[1-9]|1[012])[\/\-]\d{4}$'
patternDePrecip = '[0-9]*\.?[0-9]*'
patternDeEvap = '(\w*)|([0-9]*\.?[0-9]*)'
patternTmaxyTmin='(\w*)|([0-9]*\.?[0-9]*)'

listaDeFechas = []
listaPrecipitaciones=[]
listaEvaporacion=[]
listTmax=[]
listTmin=[]

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
        #print("Search successful.")
        listaDeFechas.append(listResult[0])        
    else:
        print("Search unsuccessful.")
    if resultPrecipitacion:
        #print("Search successful.")
        listaPrecipitaciones.append(listResult[1])        
    else:
        print("Search unsuccessful.")
    if resultEvaporacion:
        #print("Search successful.")
        listaEvaporacion.append(listResult[2])
    else:
        print("Search unsuccessful.")
    if resultTmax:
        #print("Search successful.")
        listTmax.append(listResult[3])
    else:
        print("Search unsuccessful.")
    if resultTmin:
        #print("Search successful.")
        listTmin.append(listResult[3])
    else:
        print("Search unsuccessful.")    
print(listaDeFechas,len(listaDeFechas))
print(listaPrecipitaciones,len(listaPrecipitaciones))
print(listaEvaporacion,len(listaEvaporacion))
print(listTmax,len(listTmax))
print(listTmin,len(listTmin))
        #print(listResult[0])

# archivo2 = open("briones.csv","a")
# for line in itertools.islice(archivo, 1, len(listResult)):
#     archivo2.writelines(line)
# archivo2.close()
# archivo.close()
