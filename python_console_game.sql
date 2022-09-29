-- MySQL dump 10.13  Distrib 5.5.62, for Win64 (AMD64)
--
-- Host: localhost    Database: python_console_game_w20a
-- ------------------------------------------------------
-- Server version	5.5.5-10.6.9-MariaDB

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
-- Table structure for table `client`
--

DROP TABLE IF EXISTS `client`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `client` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(100) COLLATE utf8mb4_bin DEFAULT NULL,
  `password` varchar(100) COLLATE utf8mb4_bin DEFAULT NULL,
  `joined_on` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `client_un` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `client`
--

LOCK TABLES `client` WRITE;
/*!40000 ALTER TABLE `client` DISABLE KEYS */;
INSERT INTO `client` VALUES (1,'test_user_1','pw123','2022-09-29 13:02:38');
/*!40000 ALTER TABLE `client` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `computer_fighter`
--

DROP TABLE IF EXISTS `computer_fighter`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `computer_fighter` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `move_one` int(10) unsigned DEFAULT NULL,
  `move_two` int(10) unsigned DEFAULT NULL,
  `move_three` int(10) unsigned DEFAULT NULL,
  `move_four` int(10) unsigned DEFAULT NULL,
  `name` varchar(100) COLLATE utf8mb4_bin DEFAULT NULL,
  `health_points` int(10) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `computer_fighter_FK` (`move_one`),
  KEY `computer_fighter_FK_1` (`move_two`),
  KEY `computer_fighter_FK_2` (`move_three`),
  KEY `computer_fighter_FK_3` (`move_four`),
  CONSTRAINT `computer_fighter_FK` FOREIGN KEY (`move_one`) REFERENCES `move` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `computer_fighter_FK_1` FOREIGN KEY (`move_two`) REFERENCES `move` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `computer_fighter_FK_2` FOREIGN KEY (`move_three`) REFERENCES `move` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `computer_fighter_FK_3` FOREIGN KEY (`move_four`) REFERENCES `move` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `computer_fighter`
--

LOCK TABLES `computer_fighter` WRITE;
/*!40000 ALTER TABLE `computer_fighter` DISABLE KEYS */;
INSERT INTO `computer_fighter` VALUES (1,13,14,15,16,'A Random Lightning Shinobi',1000),(2,17,18,19,20,'A Pink Dodoria',20000);
/*!40000 ALTER TABLE `computer_fighter` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fighter`
--

DROP TABLE IF EXISTS `fighter`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fighter` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `client_id` int(10) unsigned DEFAULT NULL,
  `move_one` int(10) unsigned DEFAULT NULL,
  `move_two` int(10) unsigned DEFAULT NULL,
  `move_three` int(10) unsigned DEFAULT NULL,
  `move_four` int(10) unsigned DEFAULT NULL,
  `name` varchar(100) COLLATE utf8mb4_bin DEFAULT NULL,
  `health_points` int(10) unsigned DEFAULT NULL,
  `points` int(10) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fighter_FK` (`client_id`),
  KEY `fighter_FK_1` (`move_one`),
  KEY `fighter_FK_2` (`move_two`),
  KEY `fighter_FK_3` (`move_three`),
  KEY `fighter_FK_4` (`move_four`),
  CONSTRAINT `fighter_FK` FOREIGN KEY (`client_id`) REFERENCES `client` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fighter_FK_1` FOREIGN KEY (`move_one`) REFERENCES `move` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fighter_FK_2` FOREIGN KEY (`move_two`) REFERENCES `move` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fighter_FK_3` FOREIGN KEY (`move_three`) REFERENCES `move` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fighter_FK_4` FOREIGN KEY (`move_four`) REFERENCES `move` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fighter`
--

LOCK TABLES `fighter` WRITE;
/*!40000 ALTER TABLE `fighter` DISABLE KEYS */;
INSERT INTO `fighter` VALUES (1,1,1,2,3,4,'saitama',500000,4),(2,1,5,6,7,8,'Rock',200000,4);
/*!40000 ALTER TABLE `fighter` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `move`
--

DROP TABLE IF EXISTS `move`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `move` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(100) COLLATE utf8mb4_bin DEFAULT NULL,
  `lower_damage_range` int(10) unsigned DEFAULT NULL,
  `upper_damage_range` int(10) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `move`
--

LOCK TABLES `move` WRITE;
/*!40000 ALTER TABLE `move` DISABLE KEYS */;
INSERT INTO `move` VALUES (1,'normal punch',500,1000),(2,'chop',100,200),(3,'consecutive normal punch',5000,20000),(4,'serious punch',100000,300000),(5,'leaf hurrican',200,300),(6,'meteor kick',150,400),(7,'primary lotus',1500,3000),(8,'hidden lotus - ura renge',4000,6000),(9,'short jab',500,1000),(10,'stone throw',10,100),(11,'solar flare',0,1),(12,'destructo-disc',10000,40000),(13,'lariat',300,500),(14,'lightning beast fang',400,700),(15,'thunderbolt',1000,1200),(16,'chidori',2500,5000),(17,'headbutt',1000,1500),(18,'typhoon',2000,2300),(19,'blind meteor',3000,4000),(20,'big blaster',7000,8000);
/*!40000 ALTER TABLE `move` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'python_console_game_w20a'
--
/*!50003 DROP PROCEDURE IF EXISTS `character_selection_list` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_unicode_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'IGNORE_SPACE,STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `character_selection_list`(client_id_input int unsigned)
begin
	select name from fighter
	where id = client_id_input;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `checking_credentials` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_unicode_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'IGNORE_SPACE,STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `checking_credentials`(username_input varchar(100), password_input varchar(100))
BEGIN
	select id from client
	where username = username_input and password = password_input;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `configuring_player` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_unicode_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'IGNORE_SPACE,STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `configuring_player`(client_id_input int unsigned,name_input varchar(100), move_one_input int unsigned, 
move_two_input int unsigned, move_three_input int unsigned, move_four_input int unsigned, health_points_input int unsigned)
    MODIFIES SQL DATA
BEGIN
	insert into fighter (client_id, name, move_one, move_two, move_three, move_four, health_points, points)
	values 
	(client_id_input,name_input, move_one_input, move_two_input, move_three_input, move_four_input, health_points_input, '0');
	commit;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `create_account` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_unicode_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'IGNORE_SPACE,STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `create_account`(username_input varchar(100), password_input varchar(100))
    MODIFIES SQL DATA
BEGIN
	insert into client(username, password, joined_on)
	values
	(username_input, password_input, now());
	commit;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `kill_count` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_unicode_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'IGNORE_SPACE,STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `kill_count`(id_input int unsigned, points_input int unsigned)
    MODIFIES SQL DATA
begin
	update fighter 
	set points =  points + points_input
	where fighter.id = id_input;
	commit;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `mob_list` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_unicode_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'IGNORE_SPACE,STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `mob_list`()
begin
	select id, name, health_points, move_one, move_two, move_three, move_four  from computer_fighter cf;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `skill_selection_list` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_unicode_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'IGNORE_SPACE,STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `skill_selection_list`()
begin
	select id, name, lower_damage_range, upper_damage_range from move;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-09-29 16:24:39
