-- MySQL dump 10.13  Distrib 8.0.25, for Linux (x86_64)
--
-- Host: localhost    Database: climatologia_diaria
-- ------------------------------------------------------
-- Server version	8.0.28-0ubuntu0.20.04.4

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Datos_Climatologicos`
--

DROP TABLE IF EXISTS `Datos_Climatologicos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Datos_Climatologicos` (
  `id_climatologicos` int NOT NULL AUTO_INCREMENT,
  `fecha` date DEFAULT NULL,
  `precipitacion_mm` float(3,1) DEFAULT NULL,
  `evaporacion_mm` float(3,1) DEFAULT NULL,
  `tmax` float(3,1) DEFAULT NULL,
  `tmin` float(3,1) DEFAULT NULL,
  `humedad_relativa` float(4,2) DEFAULT NULL,
  `estacion_id` int DEFAULT NULL,
  PRIMARY KEY (`id_climatologicos`),
  KEY `estacion_id` (`estacion_id`),
  CONSTRAINT `Datos_Climatologicos_ibfk_1` FOREIGN KEY (`estacion_id`) REFERENCES `Estacion_climatologica` (`id_estacion`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Datos_Climatologicos`
--

LOCK TABLES `Datos_Climatologicos` WRITE;
/*!40000 ALTER TABLE `Datos_Climatologicos` DISABLE KEYS */;
INSERT INTO `Datos_Climatologicos` VALUES (1,'1924-07-19',0.0,NULL,20.0,12.0,NULL,1);
/*!40000 ALTER TABLE `Datos_Climatologicos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Estacion_climatologica`
--

DROP TABLE IF EXISTS `Estacion_climatologica`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Estacion_climatologica` (
  `id_estacion` int NOT NULL AUTO_INCREMENT,
  `num_estacion` varchar(50) DEFAULT NULL,
  `nombre_estacion` varchar(255) DEFAULT NULL,
  `situacion` varchar(255) DEFAULT NULL,
  `municipio_id` int DEFAULT NULL,
  `organismo_id` int DEFAULT NULL,
  `latitud` varchar(50) DEFAULT NULL,
  `longitud` varchar(50) DEFAULT NULL,
  `altitud_msnm` varchar(50) DEFAULT NULL,
  `emision_fecha` date DEFAULT NULL,
  PRIMARY KEY (`id_estacion`),
  KEY `municipio_id` (`municipio_id`),
  KEY `organismo_id` (`organismo_id`),
  CONSTRAINT `Estacion_climatologica_ibfk_1` FOREIGN KEY (`municipio_id`) REFERENCES `Municipio` (`id_municipio`),
  CONSTRAINT `Estacion_climatologica_ibfk_2` FOREIGN KEY (`organismo_id`) REFERENCES `Organismo` (`id_organismo`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Estacion_climatologica`
--

LOCK TABLES `Estacion_climatologica` WRITE;
/*!40000 ALTER TABLE `Estacion_climatologica` DISABLE KEYS */;
INSERT INTO `Estacion_climatologica` VALUES (1,'30012','ATZALAN','OPERANDO',1,1,'019.789','-097.246','1,697 msnm','2020-04-06');
/*!40000 ALTER TABLE `Estacion_climatologica` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Estados_Republica_Mex`
--

DROP TABLE IF EXISTS `Estados_Republica_Mex`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Estados_Republica_Mex` (
  `id_estado` int NOT NULL AUTO_INCREMENT,
  `nombre_estado` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_estado`)
) ENGINE=InnoDB AUTO_INCREMENT=100 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Estados_Republica_Mex`
--

LOCK TABLES `Estados_Republica_Mex` WRITE;
/*!40000 ALTER TABLE `Estados_Republica_Mex` DISABLE KEYS */;
INSERT INTO `Estados_Republica_Mex` VALUES (1,'Aguascalientes'),(2,'Baja California'),(3,'Baja California Sur'),(4,'Campeche'),(5,'Coahuila de Zaragoza'),(6,'Colima'),(7,'Chiapas'),(8,'Chihuahua'),(9,'Distrito Federal'),(10,'Durango'),(11,'Guanajuato'),(12,'Guerrero'),(13,'Hidalgo'),(14,'Jalisco'),(15,'México'),(16,'Michoacán de Ocampo'),(17,'Morelos'),(18,'Nayarit'),(19,'Nuevo León'),(20,'Oaxaca de Juárez'),(21,'Puebla'),(22,'Querétaro'),(23,'Quintana Roo'),(24,'San Luis Potosí'),(25,'Sinaloa'),(26,'Sonora'),(27,'Tabasco'),(28,'Tamaulipas'),(29,'Tlaxcala'),(30,'Veracruz de Ignacio de la Llave'),(31,'Yucatán'),(32,'Zacatecas');
/*!40000 ALTER TABLE `Estados_Republica_Mex` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Municipio`
--

DROP TABLE IF EXISTS `Municipio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Municipio` (
  `id_municipio` int NOT NULL AUTO_INCREMENT,
  `estado_id` int DEFAULT NULL,
  `nombre_mun` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_municipio`),
  KEY `estado_id` (`estado_id`),
  CONSTRAINT `Municipio_ibfk_1` FOREIGN KEY (`estado_id`) REFERENCES `Estados_Republica_Mex` (`id_estado`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Municipio`
--

LOCK TABLES `Municipio` WRITE;
/*!40000 ALTER TABLE `Municipio` DISABLE KEYS */;
INSERT INTO `Municipio` VALUES (1,30,'ATZALAN');
/*!40000 ALTER TABLE `Municipio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Organismo`
--

DROP TABLE IF EXISTS `Organismo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Organismo` (
  `id_organismo` int NOT NULL AUTO_INCREMENT,
  `nombre_org` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_organismo`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Organismo`
--

LOCK TABLES `Organismo` WRITE;
/*!40000 ALTER TABLE `Organismo` DISABLE KEYS */;
INSERT INTO `Organismo` VALUES (1,'CONAGUA-SMN');
/*!40000 ALTER TABLE `Organismo` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-26  1:58:01
