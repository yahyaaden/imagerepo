-- MySQL dump 10.13  Distrib 5.7.37, for Linux (x86_64)
--
-- Host: localhost    Database: imagerepo
-- ------------------------------------------------------
-- Server version	5.7.37

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `birds`
--

DROP TABLE IF EXISTS `birds`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `birds` (
  `species` varchar(500) DEFAULT NULL,
  `location` varchar(500) DEFAULT NULL,
  `genus` varchar(500) DEFAULT NULL,
  `diet` varchar(500) DEFAULT NULL,
  `imagelink` varchar(1000) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `birds`
--

LOCK TABLES `birds` WRITE;
/*!40000 ALTER TABLE `birds` DISABLE KEYS */;
INSERT INTO `birds` VALUES ('Red-bearded bee-eater','Southeast Asia','Nyctyornis','Insects, bees, wasps and hornets','https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Nyctyornis_amictus_-_Kaeng_Krachan.jpg/320px-Nyctyornis_amictus_-_Kaeng_Krachan.jpg'),('Blue-bearded bee-eater','Southeast Asia','Nyctyornis','Bees','https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Nyctyornis_athertoni_-_Khao_Yai.jpg/320px-Nyctyornis_athertoni_-_Khao_Yai.jpg'),('Little bee-eater','Sub-Saharan Africa','Merops','Insects','https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/Little_bee-eater_%28Merops_pusillus_argutus%29_Namibia.jpg/390px-Little_bee-eater_%28Merops_pusillus_argutus%29_Namibia.jpg'),('African green bee-eater','Africa','Merops','Insects','https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/Merops_viridissimus_cleopatra_at_Fayoum%2C_Egypt_1.jpg/320px-Merops_viridissimus_cleopatra_at_Fayoum%2C_Egypt_1.jpg');
/*!40000 ALTER TABLE `birds` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-03-22 13:39:20
