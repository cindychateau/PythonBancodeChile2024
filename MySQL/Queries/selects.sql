-- Queries = Consultas
-- SELECTS -> buscar/seleccionar registros de una tabla
SELECT * FROM usuarios; -- SELECT *(todas las columnas) FROM tabla;

-- Selecciono solo las columnas de nombre y edad
SELECT nombre, edad FROM usuarios; 

-- Seleccionando solo las columnas de nombre y edad DONDE el id del registro sea 2
SELECT nombre, edad FROM usuarios WHERE id = 2;

-- Seleccionando solo las columnas de nombre y edad DONDE el nombre sea Alejandro
SELECT nombre, edad FROM usuarios WHERE nombre LIKE "Alejandro"; -- = "Alejandro"

-- Seleccionando todas las columnas de usuarios donde el nombre comienza con Al
SELECT * FROM usuarios WHERE nombre LIKE "Al%"; -- % = comodin, es decir CUALQUIER caracter

-- Seleccionando todas las columnas de usuarios donde el nombre termina con o
SELECT * FROM usuarios WHERE nombre LIKE "%o";

-- Seleccionando todas las columnas de usuarios donde el nombre termina con o y la edad mayor a 24
SELECT * FROM usuarios WHERE nombre LIKE "%o" AND edad > 24;

-- Seleccionando todas las columnas de usuarios donde el nombre termina con o O la edad mayor a 24
SELECT * FROM usuarios WHERE nombre LIKE "%o" OR edad > 24;

-- Seleccionando todas las columnas de usuarios donde nombre contenga la letra a
SELECT * FROM usuarios WHERE nombre LIKE "%a%";

-- Seleccionando todas las columnas de usuarios donde nombre contenga la letra a ordenado por edad de mayor a menor
SELECT * FROM usuarios WHERE nombre LIKE "%a%" ORDER BY edad DESC;

-- SELECT columnas FROM tabla WHERE condicional ORDER BY columna LIMIT 0,cantidad

SELECT * FROM usuarios 
WHERE nombre LIKE "%a%" 
ORDER BY edad DESC 
LIMIT 2, 3; -- donde comenzar, cantidad


