-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost
-- Tiempo de generación: 08-03-2022 a las 16:32:53
-- Versión del servidor: 10.4.21-MariaDB
-- Versión de PHP: 7.4.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `mydb`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `direcciones`
--

CREATE TABLE `direcciones` (
  `id` int(11) NOT NULL,
  `calle` varchar(45) DEFAULT NULL,
  `num` int(11) DEFAULT NULL,
  `ciudad` varchar(45) DEFAULT NULL,
  `cp` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `direcciones`
--

INSERT INTO `direcciones` (`id`, `calle`, `num`, `ciudad`, `cp`) VALUES
(1, 'Norte', 123, 'Lima', 88999),
(2, 'San Antonio', 989, 'Monterret', 77766),
(3, 'Calle A', 654, 'San José', 76434),
(4, 'Av. Julio Cesar', 111, 'Guadalajara', 54445),
(5, 'Blvd. Acapulco', 8765, 'Bogota', 77654),
(6, 'Sócrates', 221, 'Alajuela', 11234),
(7, 'Miguel Alemán', 1212, 'Cusco', 1212);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `hobbies`
--

CREATE TABLE `hobbies` (
  `id` int(11) NOT NULL,
  `actividad` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `hobbies`
--

INSERT INTO `hobbies` (`id`, `actividad`) VALUES
(1, 'Leer'),
(2, 'Patinar'),
(3, 'Correr'),
(4, 'Jugar videojuegos'),
(5, 'Jugar futbol'),
(6, 'Ver películas'),
(7, 'Ver series'),
(8, 'Cocinar'),
(9, 'Bordar'),
(10, 'Programar'),
(11, 'Bailar'),
(12, 'Dormir'),
(13, 'Jugar tenis'),
(14, 'Nadar'),
(15, 'Tocar la guitarra');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pedidos`
--

CREATE TABLE `pedidos` (
  `id` int(11) NOT NULL,
  `total` float DEFAULT NULL,
  `envio` float DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `usuario_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `pedidos`
--

INSERT INTO `pedidos` (`id`, `total`, `envio`, `created_at`, `usuario_id`) VALUES
(1, 550, 30, '2022-01-01 00:00:00', 7),
(2, 123, 30, '2022-01-02 00:00:00', 7),
(3, 1029, 50, '2022-01-02 00:00:00', 2),
(4, 345, 30, '2022-01-03 00:00:00', 3),
(5, 412, 30, '2022-01-05 00:00:00', 2),
(6, 980, 50, '2022-02-02 00:00:00', 2),
(7, 101, 30, '2022-02-16 00:00:00', 6),
(8, 777, 30, '2022-03-01 00:00:00', 4),
(9, 203, 30, '2022-03-02 00:00:00', 5);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) DEFAULT NULL,
  `edad` int(11) DEFAULT NULL,
  `direccion_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id`, `nombre`, `edad`, `direccion_id`) VALUES
(1, 'Alejandro', 25, 3),
(2, 'Martina', 64, 2),
(3, 'Elena', 19, 1),
(4, 'Aureliano', 21, 5),
(5, 'Alma', 52, 4),
(6, 'Cornelio', 37, 6),
(7, 'Esteban', 43, 7);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios_has_hobbies`
--

CREATE TABLE `usuarios_has_hobbies` (
  `usuario_id` int(11) NOT NULL,
  `hobbie_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `usuarios_has_hobbies`
--

INSERT INTO `usuarios_has_hobbies` (`usuario_id`, `hobbie_id`) VALUES
(1, 1),
(1, 2),
(1, 12),
(1, 14),
(2, 2),
(2, 13),
(3, 1),
(3, 2),
(3, 3),
(3, 4),
(3, 15),
(4, 5),
(5, 6),
(5, 7),
(6, 8),
(6, 9),
(6, 10),
(7, 11);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `direcciones`
--
ALTER TABLE `direcciones`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `hobbies`
--
ALTER TABLE `hobbies`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `pedidos`
--
ALTER TABLE `pedidos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_pedidos_usuarios1_idx` (`usuario_id`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_usuarios_direcciones1_idx` (`direccion_id`);

--
-- Indices de la tabla `usuarios_has_hobbies`
--
ALTER TABLE `usuarios_has_hobbies`
  ADD PRIMARY KEY (`usuario_id`,`hobbie_id`),
  ADD KEY `fk_usuarios_has_hobbies_hobbies1_idx` (`hobbie_id`),
  ADD KEY `fk_usuarios_has_hobbies_usuarios1_idx` (`usuario_id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `direcciones`
--
ALTER TABLE `direcciones`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `hobbies`
--
ALTER TABLE `hobbies`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT de la tabla `pedidos`
--
ALTER TABLE `pedidos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `pedidos`
--
ALTER TABLE `pedidos`
  ADD CONSTRAINT `fk_pedidos_usuarios1` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD CONSTRAINT `fk_usuarios_direcciones1` FOREIGN KEY (`direccion_id`) REFERENCES `direcciones` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `usuarios_has_hobbies`
--
ALTER TABLE `usuarios_has_hobbies`
  ADD CONSTRAINT `fk_usuarios_has_hobbies_hobbies1` FOREIGN KEY (`hobbie_id`) REFERENCES `hobbies` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_usuarios_has_hobbies_usuarios1` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
