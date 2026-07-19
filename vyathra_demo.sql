-- MySQL dump 10.13  Distrib 8.0.43, for Linux (x86_64)
--
-- Host: localhost    Database: vyathra
-- ------------------------------------------------------
-- Server version	8.0.43-0ubuntu0.22.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin` (
  `UID` varchar(10) NOT NULL,
  `password` varchar(30) NOT NULL,
  PRIMARY KEY (`UID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
INSERT INTO `admin` VALUES ('admin','password');
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bookings`
--

DROP TABLE IF EXISTS `bookings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bookings` (
  `bookno` int NOT NULL AUTO_INCREMENT,
  `route` varchar(30) NOT NULL,
  `uid` varchar(15) DEFAULT NULL,
  `booking_date` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `busno` varchar(3) DEFAULT NULL,
  `seats` int DEFAULT NULL,
  `book_id` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`bookno`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bookings`
--

LOCK TABLES `bookings` WRITE;
/*!40000 ALTER TABLE `bookings` DISABLE KEYS */;
INSERT INTO `bookings` VALUES (1,'KOTTIYOOR-KOCHI','sg','2025-10-14 04:37:17','2',2,NULL),(2,'KATTIYAD-KOZHIKODE','sg','2025-10-14 05:35:45','9',3,NULL),(3,'KATTIYAD-KOZHIKODE','sg','2025-10-14 05:47:46','9',3,NULL),(4,'KOTTIYOOR-KOCHI','sg','2025-10-14 05:49:26','2',4,NULL),(5,'KOTTIYOOR-KOCHI','sg','2025-10-14 05:52:13','2',1,NULL),(6,'KATTIYAD-KOZHIKODE','sg','2025-10-14 05:55:46','9',5,NULL),(7,'KATTIYAD-KOZHIKODE','sg','2025-10-14 05:58:05','9',3,NULL),(8,'KOTTIYOOR-KOCHI','sg','2025-10-14 06:02:11','2',2,NULL),(9,'KOTTIYOOR-KOCHI','sg','2025-10-14 06:03:43','2',2,NULL),(10,'KOTTIYOOR-KOCHI','sg','2025-10-14 06:04:58','2',1,NULL),(11,'KOTTIYOOR-KOCHI','sg','2025-10-14 06:06:03','2',3,NULL),(12,'KOTTIYOOR-KOCHI','sg','2025-10-14 06:07:37','2',2,NULL),(13,'KATTIYAD-KOZHIKODE','sg','2025-10-14 06:15:38','9',2,NULL),(14,'KOTTIYOOR-KOCHI','sg','2025-10-14 06:16:35','2',2,NULL),(15,'KOTTIYOOR-KOCHI','sg','2025-10-14 06:20:26','2',2,NULL),(16,'KOTTIYOOR-KOCHI','sg','2025-10-14 06:29:41','2',2,NULL),(17,'KOTTIYOOR-KOCHI','sg','2025-10-21 06:04:00','2',3,NULL),(18,'KOTTIYOOR-KOCHI','sg','2025-10-21 06:06:17','2',2,NULL),(19,'KOTTIYOOR-KOCHI','sg','2025-10-21 06:15:42','2',2,NULL),(20,'KATTIYAD-KOZHIKODE','sg','2025-10-21 06:18:23','9',4,NULL),(21,'KATTIYAD-KOZHIKODE','sg','2025-10-21 06:23:02','9',3,NULL),(22,'KOTTIYOOR-KOCHI','sg','2025-10-21 06:25:37','2',4,NULL),(23,'KOTTIYOOR-KOCHI','sg','2025-10-21 06:36:50','2',3,NULL),(24,'KOTTIYOOR-KOCHI','sg','2025-10-21 06:41:04','2',3,NULL),(25,'KOTTIYOOR-KOCHI','sg','2025-10-21 06:41:51','2',2,NULL),(26,'KOTTIYOOR-KOCHI','sg','2025-10-27 09:02:34','2',2,'VSN000026'),(27,'KOTTIYOOR-KOCHI','sg','2025-12-15 09:30:59','2',2,'VSN000027'),(28,'KATTIYAD-KOZHIKODE','sg','2026-07-18 09:39:18','9',8,'VSN000028'),(29,'KOTTIYOOR-KOCHI','sg','2026-07-18 09:51:18','2',2,'VSN000029');
/*!40000 ALTER TABLE `bookings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bussid`
--

DROP TABLE IF EXISTS `bussid`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bussid` (
  `busno` int NOT NULL,
  `route` varchar(30) NOT NULL,
  `STIME` time NOT NULL,
  `ETIME` time NOT NULL,
  `stop1` varchar(20) NOT NULL,
  `stop2` varchar(20) NOT NULL,
  `stop3` varchar(20) NOT NULL,
  `type` varchar(20) NOT NULL,
  `fare` int NOT NULL,
  `seat` int DEFAULT NULL,
  PRIMARY KEY (`busno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bussid`
--

LOCK TABLES `bussid` WRITE;
/*!40000 ALTER TABLE `bussid` DISABLE KEYS */;
INSERT INTO `bussid` VALUES (2,'KOTTIYOOR-KOCHI','18:00:00','06:00:00','PERAVOOR','MATTANUR','KOZHIKODE','semi sleeper AC',999,49),(9,'KATTIYAD-KOZHIKODE','20:00:00','00:00:00','KOLAYAD','MATTANUR','MUSCAT','semi sleeper AC',999,49);
/*!40000 ALTER TABLE `bussid` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cred`
--

DROP TABLE IF EXISTS `cred`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cred` (
  `UID` varchar(10) NOT NULL,
  `name` varchar(20) NOT NULL,
  `email` varchar(30) DEFAULT NULL,
  `password` varchar(30) NOT NULL,
  `date` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`UID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cred`
--

LOCK TABLES `cred` WRITE;
/*!40000 ALTER TABLE `cred` DISABLE KEYS */;
INSERT INTO `cred` VALUES ('adu','adwait','adu@random.org','adda','2025-10-27 09:45:02'),('samllm','sam','samllm@vy.org','llmllm','2026-07-18 13:38:57'),('sg','shilo','sg@random.com','sg1','2025-10-27 09:42:11');
/*!40000 ALTER TABLE `cred` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `curr`
--

DROP TABLE IF EXISTS `curr`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `curr` (
  `UID` varchar(10) NOT NULL,
  `password` varchar(20) NOT NULL,
  `login_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`UID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `curr`
--

LOCK TABLES `curr` WRITE;
/*!40000 ALTER TABLE `curr` DISABLE KEYS */;
/*!40000 ALTER TABLE `curr` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `history`
--

DROP TABLE IF EXISTS `history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `history` (
  `cno` int NOT NULL,
  `route` varchar(20) NOT NULL,
  `STIME` time NOT NULL,
  `ETIME` time NOT NULL,
  `fare` int NOT NULL,
  `type` varchar(10) DEFAULT NULL,
  `seatno` varchar(5) DEFAULT NULL,
  PRIMARY KEY (`cno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `history`
--

LOCK TABLES `history` WRITE;
/*!40000 ALTER TABLE `history` DISABLE KEYS */;
/*!40000 ALTER TABLE `history` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userdata`
--

DROP TABLE IF EXISTS `userdata`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `userdata` (
  `UID` varchar(6) NOT NULL,
  `name` varchar(20) NOT NULL,
  `email` varchar(30) NOT NULL,
  `mobile` char(10) DEFAULT NULL,
  `gender` varchar(1) NOT NULL,
  PRIMARY KEY (`UID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userdata`
--

LOCK TABLES `userdata` WRITE;
/*!40000 ALTER TABLE `userdata` DISABLE KEYS */;
INSERT INTO `userdata` VALUES ('adu','adwait','adu@random.org','4323456543','m'),('samllm','sam','samllm@vy.org','2834839283','m'),('sg','shilo','sg@random.com','9999999999','m');
/*!40000 ALTER TABLE `userdata` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-07-18 19:50:45
