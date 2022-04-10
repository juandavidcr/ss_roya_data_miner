from pathlib import Path

def ls3(path):
    return [obj.name for obj in Path(path).iterdir() if obj.is_file()]
files=ls3("/home/david/Escritorio/SERV SOCIAL UAMC/DataMining/bancdata")
for file in files:
    print(file)