class TablaEstaciones:
    def __init__(self,id_estacion,num_estacion,nombre_estacion,municipio_id,situacion,organismo_id,latitud,longitud,altitud_msnm,emision_fecha):
        self.id_estacion=id_estacion
        self.num_estacion=num_estacion
        self.nombre_estacion=nombre_estacion
        self.municipio_id=municipio_id
        self.situacion=situacion
        self.organismo_id=organismo_id
        self.latitud=latitud
        self.longitud=longitud
        self.altitud_msnm=altitud_msnm
        self.emision_fecha=emision_fecha


class TablaOrganismo:
    def __init__(self, id_organismo,nombre_org):
        self.id_organismo=id_organismo
        self.nombre_org=nombre_org

class TablaMunicipio:
    def __init__(self,id_municipio,estado_id,nombre_mun):
        self.id_municipio=id_municipio
        self.estado_id=estado_id
        self.nombre_mun=nombre_mun

class TablaEdosRepMex:
    def __init_(self,id_estado,nombre_est):
        self.id_estado=id_estado
        self.nombre_est=nombre_est

class TablaDataClimatologia:
    def __init__(self,id_climatologicos,fecha,precipitacion_mm,evaporacion_mm,tmax,tmin,humedad_relativa,estacion_id):
        self.id_climatologicos=id_climatologicos
        self.fecha=fecha
        self.precipitacion=precipitacion_mm
        self.evaporacion=evaporacion_mm
        self.tmax=tmax
        self.tmin=tmin
        self.humedad_rel=humedad_relativa
        self.estacion_id=estacion_id
