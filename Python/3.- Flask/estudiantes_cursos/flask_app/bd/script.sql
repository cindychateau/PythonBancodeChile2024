-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema esquema_estudiantes_cursos
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `esquema_estudiantes_cursos` ;

-- -----------------------------------------------------
-- Schema esquema_estudiantes_cursos
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `esquema_estudiantes_cursos` DEFAULT CHARACTER SET utf8 ;
USE `esquema_estudiantes_cursos` ;

-- -----------------------------------------------------
-- Table `esquema_estudiantes_cursos`.`cursos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_estudiantes_cursos`.`cursos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `esquema_estudiantes_cursos`.`estudiantes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_estudiantes_cursos`.`estudiantes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  `apellido` VARCHAR(45) NULL,
  `edad` INT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `curso_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_estudiantes_cursos_idx` (`curso_id` ASC),
  CONSTRAINT `fk_estudiantes_cursos`
    FOREIGN KEY (`curso_id`)
    REFERENCES `esquema_estudiantes_cursos`.`cursos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
