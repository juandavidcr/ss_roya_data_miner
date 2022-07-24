#script4.py
from datetime import date



def createFecha(aaaa,mm,dd):
    fecha=date(int(aaaa),int(mm),int(dd))
    print(fecha)

createFecha('2022','05','22')