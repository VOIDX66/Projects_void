/*M!999999\- enable the sandbox mode */ 
-- MariaDB dump 10.19  Distrib 10.11.9-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: partidos_db
-- ------------------------------------------------------
-- Server version	10.11.9-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `partidos_db`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `partidos_db` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish_ci */;

USE `partidos_db`;

--
-- Table structure for table `Calificaciones`
--

DROP TABLE IF EXISTS `Calificaciones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Calificaciones` (
  `id_calificacion` int(11) NOT NULL AUTO_INCREMENT,
  `id_jugador_calificado` int(11) DEFAULT NULL,
  `id_jugador` int(11) DEFAULT NULL,
  `id_partido` int(11) DEFAULT NULL,
  `comentario` varchar(255) DEFAULT NULL,
  `puntuacion` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_calificacion`),
  KEY `id_jugador` (`id_jugador_calificado`),
  KEY `id_partido` (`id_partido`),
  KEY `Calificaciones_ibfk_3` (`id_jugador`),
  CONSTRAINT `Calificaciones_ibfk_1` FOREIGN KEY (`id_jugador_calificado`) REFERENCES `Jugadores` (`id_jugador`),
  CONSTRAINT `Calificaciones_ibfk_2` FOREIGN KEY (`id_partido`) REFERENCES `Partidos` (`id_partido`),
  CONSTRAINT `Calificaciones_ibfk_3` FOREIGN KEY (`id_jugador`) REFERENCES `Jugadores` (`id_jugador`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Calificaciones`
--

LOCK TABLES `Calificaciones` WRITE;
/*!40000 ALTER TABLE `Calificaciones` DISABLE KEYS */;
INSERT INTO `Calificaciones` VALUES
(29,3,1,9,'',10),
(30,3,4,9,'',8);
/*!40000 ALTER TABLE `Calificaciones` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Equipos`
--

DROP TABLE IF EXISTS `Equipos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Equipos` (
  `id_equipo` int(11) NOT NULL AUTO_INCREMENT,
  `id_partido` int(11) DEFAULT NULL,
  `nombre` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id_equipo`),
  KEY `id_partido` (`id_partido`),
  CONSTRAINT `Equipos_ibfk_1` FOREIGN KEY (`id_partido`) REFERENCES `Partidos` (`id_partido`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Equipos`
--

LOCK TABLES `Equipos` WRITE;
/*!40000 ALTER TABLE `Equipos` DISABLE KEYS */;
INSERT INTO `Equipos` VALUES
(17,9,'Nacional'),
(18,9,'America'),
(19,10,'Mexico'),
(20,10,'Colombia'),
(21,11,'Canada'),
(22,11,'Venezuela');
/*!40000 ALTER TABLE `Equipos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Infracciones`
--

DROP TABLE IF EXISTS `Infracciones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Infracciones` (
  `id_infraccion` int(11) NOT NULL AUTO_INCREMENT,
  `id_jugador` int(11) DEFAULT NULL,
  `id_partido` int(11) DEFAULT NULL,
  `descripcion` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_infraccion`),
  KEY `id_jugador` (`id_jugador`),
  KEY `id_partido` (`id_partido`),
  CONSTRAINT `Infracciones_ibfk_1` FOREIGN KEY (`id_jugador`) REFERENCES `Jugadores` (`id_jugador`),
  CONSTRAINT `Infracciones_ibfk_2` FOREIGN KEY (`id_partido`) REFERENCES `Partidos` (`id_partido`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Infracciones`
--

LOCK TABLES `Infracciones` WRITE;
/*!40000 ALTER TABLE `Infracciones` DISABLE KEYS */;
INSERT INTO `Infracciones` VALUES
(13,11,11,'Darse de baja sin reemplazo'),
(23,1,11,'Darse de baja sin reemplazo'),
(24,1,9,'pa ver');
/*!40000 ALTER TABLE `Infracciones` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb3 */ ;
/*!50003 SET character_set_results = utf8mb3 */ ;
/*!50003 SET collation_connection  = utf8mb3_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER trigger_infraccion
AFTER INSERT ON Infracciones
FOR EACH ROW
BEGIN
    DECLARE num_infracciones INT;

    -- Crear tabla temporal para almacenar los últimos 10 partidos en los que el jugador ha participado
    CREATE TEMPORARY TABLE UltimosPartidos AS
    SELECT p.id_partido
    FROM Partidos p
    JOIN Equipos e ON e.id_partido = p.id_partido  -- Relacionamos Equipos con Partidos
    JOIN Jugador_Equipo je ON je.id_equipo = e.id_equipo  -- Relacionamos Jugador_Equipo con Equipos
    WHERE je.id_jugador = NEW.id_jugador
    ORDER BY p.fecha DESC
    LIMIT 10;

    -- Contar las infracciones del jugador en esos últimos 10 partidos
    SELECT COUNT(*)
    INTO num_infracciones
    FROM Infracciones i
    JOIN UltimosPartidos up ON up.id_partido = i.id_partido
    WHERE i.id_jugador = NEW.id_jugador;

    -- Si el jugador tiene 2 o más infracciones en los últimos 10 partidos, actualizar es_solidario a 1
    IF num_infracciones >= 2 THEN
        UPDATE Jugadores 
        SET es_solidario = 1
        WHERE id_jugador = NEW.id_jugador;
    END IF;

    -- Eliminar la tabla temporal
    DROP TEMPORARY TABLE IF EXISTS UltimosPartidos;

END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb3 */ ;
/*!50003 SET character_set_results = utf8mb3 */ ;
/*!50003 SET collation_connection  = utf8mb3_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER trigger_infraccion_delete
AFTER DELETE ON Infracciones
FOR EACH ROW
BEGIN
    DECLARE num_infracciones INT;

    -- Crear tabla temporal para almacenar los últimos 10 partidos en los que el jugador ha participado
    CREATE TEMPORARY TABLE UltimosPartidos AS
    SELECT p.id_partido
    FROM Partidos p
    JOIN Equipos e ON e.id_partido = p.id_partido  -- Relacionamos Equipos con Partidos
    JOIN Jugador_Equipo je ON je.id_equipo = e.id_equipo  -- Relacionamos Jugador_Equipo con Equipos
    WHERE je.id_jugador = OLD.id_jugador
    ORDER BY p.fecha DESC
    LIMIT 10;

    -- Contar las infracciones del jugador en esos últimos 10 partidos
    SELECT COUNT(*)
    INTO num_infracciones
    FROM Infracciones i
    JOIN UltimosPartidos up ON up.id_partido = i.id_partido
    WHERE i.id_jugador = OLD.id_jugador;

    -- Si el jugador tiene menos de 2 infracciones en los últimos 10 partidos, actualizar es_solidario a 0
    IF num_infracciones < 2 THEN
        UPDATE Jugadores 
        SET es_solidario = 0
        WHERE id_jugador = OLD.id_jugador;
    END IF;

    -- Eliminar la tabla temporal
    DROP TEMPORARY TABLE IF EXISTS UltimosPartidos;

END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `Jugador_Equipo`
--

DROP TABLE IF EXISTS `Jugador_Equipo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Jugador_Equipo` (
  `id_jugador_equipo` int(11) NOT NULL AUTO_INCREMENT,
  `id_equipo` int(11) DEFAULT NULL,
  `id_jugador` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_jugador_equipo`),
  KEY `id_equipo` (`id_equipo`),
  KEY `id_jugador` (`id_jugador`),
  CONSTRAINT `Jugador_Equipo_ibfk_1` FOREIGN KEY (`id_equipo`) REFERENCES `Equipos` (`id_equipo`),
  CONSTRAINT `Jugador_Equipo_ibfk_2` FOREIGN KEY (`id_jugador`) REFERENCES `Jugadores` (`id_jugador`)
) ENGINE=InnoDB AUTO_INCREMENT=839 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Jugador_Equipo`
--

LOCK TABLES `Jugador_Equipo` WRITE;
/*!40000 ALTER TABLE `Jugador_Equipo` DISABLE KEYS */;
INSERT INTO `Jugador_Equipo` VALUES
(808,17,1),
(809,17,3),
(810,17,4),
(811,17,5),
(812,17,6),
(813,18,7),
(814,18,8),
(815,18,9),
(816,18,10),
(817,18,11),
(818,19,11),
(819,19,8),
(820,19,3),
(821,19,1),
(822,19,7),
(824,20,6),
(825,20,5),
(826,20,9),
(827,20,12),
(828,21,9),
(829,21,13),
(831,21,8),
(832,21,7),
(833,22,11),
(834,22,4),
(835,22,12),
(836,22,5),
(837,22,6);
/*!40000 ALTER TABLE `Jugador_Equipo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Jugadores`
--

DROP TABLE IF EXISTS `Jugadores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Jugadores` (
  `id_jugador` int(11) NOT NULL AUTO_INCREMENT,
  `id_usuario` int(11) DEFAULT NULL,
  `model_sel` varchar(30) NOT NULL DEFAULT 'OCASIONAL',
  `puntuacion` float DEFAULT 0,
  `es_solidario` tinyint(1) DEFAULT 0,
  `disponible` tinyint(1) DEFAULT 1,
  PRIMARY KEY (`id_jugador`),
  KEY `id_usuario` (`id_usuario`),
  CONSTRAINT `Jugadores_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `Usuarios` (`id_usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Jugadores`
--

LOCK TABLES `Jugadores` WRITE;
/*!40000 ALTER TABLE `Jugadores` DISABLE KEYS */;
INSERT INTO `Jugadores` VALUES
(1,1006149333,'OCASIONAL',0,0,1),
(3,1004259897,'OCASIONAL',9,1,1),
(4,1137060795,'FRECUENTE',8,0,1),
(5,1004582530,'OCASIONAL',0,0,1),
(6,1003302080,'OCASIONAL',5,0,1),
(7,1138024562,'OCASIONAL',0,0,1),
(8,1002033542,'FRECUENTE',0,0,1),
(9,1004564103,'OCASIONAL',0,0,1),
(10,1122084333,'OCASIONAL',0,0,1),
(11,1002020222,'FRECUENTE',10,0,1),
(12,1002033845,'OCASIONAL',0,0,1),
(13,1003255205,'OCASIONAL',0,0,1);
/*!40000 ALTER TABLE `Jugadores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Notificaciones`
--

DROP TABLE IF EXISTS `Notificaciones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Notificaciones` (
  `id_notificacion` int(11) NOT NULL AUTO_INCREMENT,
  `id_jugador` int(11) NOT NULL,
  `contenido` varchar(255) NOT NULL,
  `leida` tinyint(1) NOT NULL DEFAULT 0,
  `fecha_partido` datetime DEFAULT curdate(),
  PRIMARY KEY (`id_notificacion`),
  KEY `id_jugador` (`id_jugador`),
  CONSTRAINT `Notificaciones_ibfk_1` FOREIGN KEY (`id_jugador`) REFERENCES `Jugadores` (`id_jugador`)
) ENGINE=InnoDB AUTO_INCREMENT=83 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Notificaciones`
--

LOCK TABLES `Notificaciones` WRITE;
/*!40000 ALTER TABLE `Notificaciones` DISABLE KEYS */;
INSERT INTO `Notificaciones` VALUES
(42,1,'Has sido asignado al equipo Nacional',1,'2024-11-30 15:00:00'),
(43,3,'Has sido asignado al equipo Nacional',1,'2024-11-30 15:00:00'),
(44,4,'Has sido asignado al equipo Nacional',1,'2024-11-30 15:00:00'),
(45,5,'Has sido asignado al equipo Nacional',0,'2024-11-30 15:00:00'),
(46,6,'Has sido asignado al equipo Nacional',0,'2024-11-30 15:00:00'),
(47,7,'Has sido asignado al equipo America',0,'2024-11-30 15:00:00'),
(48,8,'Has sido asignado al equipo America',0,'2024-11-30 15:00:00'),
(49,9,'Has sido asignado al equipo America',0,'2024-11-30 15:00:00'),
(50,10,'Has sido asignado al equipo America',0,'2024-11-30 15:00:00'),
(51,11,'Has sido asignado al equipo America',0,'2024-11-30 15:00:00'),
(53,1,'Usted tiene una nueva Infraccion',1,'2024-11-28 00:00:00'),
(54,11,'Has sido asignado al equipo Mexico',0,'2024-11-29 05:26:00'),
(55,8,'Has sido asignado al equipo Mexico',0,'2024-11-29 05:26:00'),
(56,3,'Has sido asignado al equipo Mexico',1,'2024-11-29 05:26:00'),
(57,1,'Has sido asignado al equipo Mexico',1,'2024-11-29 05:26:00'),
(58,7,'Has sido asignado al equipo Mexico',0,'2024-11-29 05:26:00'),
(59,4,'Has sido asignado al equipo Colombia',1,'2024-11-29 05:26:00'),
(60,6,'Has sido asignado al equipo Colombia',0,'2024-11-29 05:26:00'),
(61,5,'Has sido asignado al equipo Colombia',0,'2024-11-29 05:26:00'),
(62,9,'Has sido asignado al equipo Colombia',0,'2024-11-29 05:26:00'),
(63,12,'Has sido asignado al equipo Colombia',0,'2024-11-29 05:26:00'),
(64,1,'Usted tiene una nueva Infraccion',1,'2024-11-29 00:00:00'),
(65,1,'Usted tiene una nueva Infraccion',1,'2024-11-29 00:00:00'),
(66,1,'Usted tiene una nueva Infraccion',1,'2024-11-29 00:00:00'),
(67,9,'Has sido asignado al equipo Canada',0,'2024-12-02 08:10:00'),
(68,13,'Has sido asignado al equipo Canada',0,'2024-12-02 08:10:00'),
(69,10,'Has sido asignado al equipo Canada',0,'2024-12-02 08:10:00'),
(70,8,'Has sido asignado al equipo Canada',0,'2024-12-02 08:10:00'),
(71,7,'Has sido asignado al equipo Canada',0,'2024-12-02 08:10:00'),
(72,3,'Has sido asignado al equipo Venezuela',1,'2024-12-02 08:10:00'),
(73,4,'Has sido asignado al equipo Venezuela',1,'2024-12-02 08:10:00'),
(74,12,'Has sido asignado al equipo Venezuela',0,'2024-12-02 08:10:00'),
(75,5,'Has sido asignado al equipo Venezuela',0,'2024-12-02 08:10:00'),
(76,6,'Has sido asignado al equipo Venezuela',0,'2024-12-02 08:10:00'),
(77,3,'Has sido reemplazado en un partido por otro jugador.',1,'2024-11-29 00:00:00'),
(78,11,'Has sido reemplazado en el partido por otro jugador.',0,'2024-11-29 00:00:00'),
(79,3,'Has sido reemplazado en un partido por otro jugador.',0,'2024-11-29 00:00:00'),
(80,3,'Has sido asignado a un partido por otro jugador.',0,'2024-11-29 00:00:00'),
(81,3,'Has sido reemplazado en un partido por otro jugador.',0,'2024-11-29 00:00:00'),
(82,1,'Usted tiene una nueva Infraccion',1,'2024-11-29 00:00:00');
/*!40000 ALTER TABLE `Notificaciones` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Partidos`
--

DROP TABLE IF EXISTS `Partidos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Partidos` (
  `id_partido` int(11) NOT NULL AUTO_INCREMENT,
  `fecha` datetime DEFAULT NULL,
  `estado` varchar(30) DEFAULT 'CONFIRMADO',
  PRIMARY KEY (`id_partido`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Partidos`
--

LOCK TABLES `Partidos` WRITE;
/*!40000 ALTER TABLE `Partidos` DISABLE KEYS */;
INSERT INTO `Partidos` VALUES
(9,'2024-11-30 15:00:00','JUGADO'),
(10,'2024-11-29 05:26:00','CONFIRMADO'),
(11,'2024-12-02 08:10:00','JUGADO');
/*!40000 ALTER TABLE `Partidos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Usuarios`
--

DROP TABLE IF EXISTS `Usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Usuarios` (
  `id_usuario` int(11) NOT NULL,
  `nombre` varchar(30) DEFAULT NULL,
  `tipo` varchar(30) DEFAULT 'USER',
  `fecha_creacion` date DEFAULT curdate(),
  `contrasena` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_usuario`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Usuarios`
--

LOCK TABLES `Usuarios` WRITE;
/*!40000 ALTER TABLE `Usuarios` DISABLE KEYS */;
INSERT INTO `Usuarios` VALUES
(1,'Administrador','ADMIN','2024-11-15','admin'),
(1002020222,'Alejandro','USER','2024-11-26','sombreros12_3'),
(1002033542,'Valeria','USER','2024-11-26','huellitasdecafe'),
(1002033845,'Pablo','USER','2024-11-26','futbolmipasion'),
(1003255205,'Hector','USER','2024-11-26','messi23'),
(1003302080,'Fernando','USER','2024-11-26','telefono#3'),
(1004259897,'Jose','USER','2024-11-26','josejose'),
(1004564103,'Sebastian','USER','2024-11-26','granfamilia2'),
(1004582530,'Elizabeth','USER','2024-11-26','silla'),
(1006149333,'Jaider','USER','2024-11-15','123'),
(1122084333,'Jhon','USER','2024-11-26','jhon123'),
(1137060795,'Sara','USER','2024-11-26','sancocho'),
(1138024562,'Cristian','USER','2024-11-26','ositopanda');
/*!40000 ALTER TABLE `Usuarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'partidos_db'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-29  5:55:01
