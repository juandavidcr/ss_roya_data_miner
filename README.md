Script de Extracción de Información para proyecto de Roya Cafetales
--------------------------------------------------------------------
pyt
| Pasos | README |
| ------ | ------ |
| 1 | Instalar las dependencias: pip3 install mysql-connector-python  -> es de la version 8|
| 2 | git fetch, git pull |
| 3 | db.sql es donde se encuentra el esquema de las tablas |
| 4 | dbestados.sql es donde se encuentra el catalogo de estados de la República Mexicana |
| 5 | db.py Se encuentra la conexión con mysql y los inserts comentados |
| 6 | script1DataCleanUp.py Extrae la informcaión de los archivos de los municipios de las carpetas donde se lee la información |
| 7 | base.sql |
| 8 | newfile.txt contiene información de las estaciones climatologicas y las dependencias gubernamentales de donde se extrae la información al igual que latitud y longitud para llenar las tablas Estacion_climatologica, Municipio, Organismo |
| 9 |  |



## Installation


```sh
python3 script1DataCleanUp.py
```

```sh
python3 db.py
```