import pandas as pd
import random
df1=pd.read_csv("./ATZALAN.csv")
def calcularHR(TMAX):
    g = random.randint(2,130)
    et = g
    etd = (g*1.0000133-133) *-1
    hr = 100*(etd/et)
    return hr
df1["HUMEDAD_RELATIVA"] = df1["HUMEDAD_RELATIVA"].apply(calcularHR)    
print(df1)
