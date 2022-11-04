-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3306
-- Tiempo de generación: 04-11-2022 a las 21:12:01
-- Versión del servidor: 5.7.31
-- Versión de PHP: 7.3.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `future`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estado`
--

DROP TABLE IF EXISTS `estado`;
CREATE TABLE IF NOT EXISTS `estado` (
  `Id_Estado` int(4) NOT NULL AUTO_INCREMENT,
  `Nombre_Estado` varchar(50) NOT NULL,
  PRIMARY KEY (`Id_Estado`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `estado`
--

INSERT INTO `estado` (`Id_Estado`, `Nombre_Estado`) VALUES
(1, 'Venta'),
(2, 'Alquiler'),
(3, 'Prestamo'),
(4, 'Cesion'),
(8, 'Comisión'),
(7, 'Arriendo');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `operatoriacomercial`
--

DROP TABLE IF EXISTS `operatoriacomercial`;
CREATE TABLE IF NOT EXISTS `operatoriacomercial` (
  `Id_OperatoriaComercial` int(4) NOT NULL AUTO_INCREMENT,
  `Nombre_OperatoriaComercial` varchar(50) NOT NULL,
  PRIMARY KEY (`Id_OperatoriaComercial`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `operatoriacomercial`
--

INSERT INTO `operatoriacomercial` (`Id_OperatoriaComercial`, `Nombre_OperatoriaComercial`) VALUES
(1, 'Pendiente'),
(2, 'Alquilada'),
(3, 'Vendida'),
(4, 'Cedida');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `propiedad`
--

DROP TABLE IF EXISTS `propiedad`;
CREATE TABLE IF NOT EXISTS `propiedad` (
  `Id_Propiedad` int(6) NOT NULL AUTO_INCREMENT,
  `Id_Tipo` int(4) NOT NULL,
  `Id_Estado` int(4) NOT NULL,
  `Id_OperatoriaComercial` int(4) NOT NULL,
  `Id_Propietario` int(6) NOT NULL,
  `Nombre` varchar(50) NOT NULL,
  `Direccion` varchar(50) NOT NULL,
  `Contacto` varchar(100) NOT NULL,
  PRIMARY KEY (`Id_Propiedad`),
  KEY `FK_Tipo` (`Id_Tipo`),
  KEY `FK_Estado` (`Id_Estado`),
  KEY `FK_OperatoriaComercial` (`Id_OperatoriaComercial`),
  KEY `FK_Propietario` (`Id_Propietario`)
) ENGINE=MyISAM AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `propiedad`
--

INSERT INTO `propiedad` (`Id_Propiedad`, `Id_Tipo`, `Id_Estado`, `Id_OperatoriaComercial`, `Id_Propietario`, `Nombre`, `Direccion`, `Contacto`) VALUES
(6, 1, 1, 3, 1, 'casa blanca', 'colon 1112', 'Pedro'),
(7, 2, 2, 1, 2, 'Juan', 'Santa Rosa 715', 'Inmobiliaria Rural'),
(8, 3, 3, 1, 3, 'Ramona', 'San Martin 13983', 'Inmobiliaria Rural'),
(9, 2, 2, 2, 1, 'Lolo', 'Belgrano 123', 'Inmobiliaria Rural'),
(10, 2, 1, 2, 3, 'Rafaela', 'San Martin 454', 'Inmobiliaria San Jose'),
(11, 7, 2, 1, 5, 'Playa de est. centro', 'Humberto Prima 300', 'Luis'),
(14, 4, 1, 1, 3, 'prueba modificacion', 'prueba', 'hhj'),
(15, 3, 7, 1, 2, 'campo grande', 'san justo', 'Lucho');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `propietario`
--

DROP TABLE IF EXISTS `propietario`;
CREATE TABLE IF NOT EXISTS `propietario` (
  `Id_Propietario` int(6) NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(50) NOT NULL,
  `Direccion` varchar(50) NOT NULL,
  `Contacto` varchar(100) NOT NULL,
  PRIMARY KEY (`Id_Propietario`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `propietario`
--

INSERT INTO `propietario` (`Id_Propietario`, `Nombre`, `Direccion`, `Contacto`) VALUES
(1, 'Alfredo Palacios', 'Cuenca 1468', '351 3466187 3544 428058 '),
(2, 'Evangelina', 'Usandivaras 945', '351'),
(3, 'Juan Domingo', 'Claudio Cuenca 1468', 'no tiene'),
(4, 'Roberto Perez', 'Mexico 123 Dpto A', '351 3664879'),
(5, 'Federico Chan', 'Cerrito 889', 'bs as');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipo`
--

DROP TABLE IF EXISTS `tipo`;
CREATE TABLE IF NOT EXISTS `tipo` (
  `Id_Tipo` int(4) NOT NULL AUTO_INCREMENT,
  `Nombre_Tipo` varchar(50) NOT NULL,
  PRIMARY KEY (`Id_Tipo`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `tipo`
--

INSERT INTO `tipo` (`Id_Tipo`, `Nombre_Tipo`) VALUES
(1, 'Casa'),
(2, 'Departamento'),
(3, 'Campo'),
(4, 'Quinta'),
(5, 'Lote'),
(6, 'Galpon'),
(7, 'Playa Esta.'),
(8, 'C. Deportivo'),
(9, 'Canchas tenis'),
(10, 'Canchas futbol');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
