DROP SCHEMA IF EXISTS `testdb_mp3` ;
CREATE SCHEMA IF NOT EXISTS `testdb_mp3` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ;
USE `testdb_mp3` ;

DROP TABLE IF EXISTS `testdb_m3`.`files` ;

CREATE TABLE IF NOT EXISTS `testdb_mp3`.`files` (
 `id` INT(11) NOT NULL AUTO_INCREMENT,
  
	`link` VARCHAR(245) NOT NULL,
	`album` VARCHAR(245)  NULL,
	`artist` VARCHAR(245)  NULL,
	`year` VARCHAR(45)  NULL,
	`genre` VARCHAR(245)  NULL,
	`comment` VARCHAR(245)  NULL,
	`track` VARCHAR(45)  NULL,
	`bitrate` VARCHAR(45)  NULL,
	`songtitle` VARCHAR(245)  NULL,
	`length` VARCHAR(45)  NULL,
	`size` VARCHAR(45)  NULL,	
		
	PRIMARY KEY (`id`),
	UNIQUE INDEX `link` (`link`)
)
ENGINE = InnoDB
AUTO_INCREMENT=3286;