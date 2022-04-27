Script de Extracción de Información para proyecto de Roya Cafetales
--------------------------------------------------------------------
# Data Mining for Roya project (UAM CUAJIMALPA social service) from Google Earth
## _Documentación_
| Pasos | README |
| ------ | ------ |
| 1 | Instalar las dependencias:   -> es de la version 8|
| 2 | git fetch, git pull |
| 3 | db.sql es donde se encuentra el esquema de las tablas |
| 4 | dbestados.sql es donde se encuentra el catalogo de estados de la República Mexicana |
| 5 | db.py Se encuentra la conexión con mysql y los inserts comentados |
| 6 | script1DataCleanUp.py Extrae la informcaión de los archivos de los municipios de las carpetas donde se lee la información |
| 7 | base.sql |
| 8 | newfile.txt contiene información de las estaciones climatologicas y las dependencias gubernamentales de donde se extrae la información al igual que latitud y longitud para llenar las tablas Estacion_climatologica, Municipio, Organismo |
| 9 | Al momento de correr el script script1DataCleanUp.py |



## Installation


```sh
pip3 install mysql-connector-python
```

```sh
git clone https://github.com/juandavidcr/ss_roya_data_miner.git
```

```sh
python3 script1DataCleanUp.py
```

```sh
python3 db.py
```

```sh
mkdir ss_roya
cd ss_roya
sudo apt install python3.8-venv
python3 -m venv venv
ls
---------
- /venv -
---------
. venv/bin/activate

(venv)your/terminal/~ pip3 install Flask
export FLASK_APP=holamundo.py
flask run
export FLASK_ENV=development
export FLASK_APP=holamundo.py

```