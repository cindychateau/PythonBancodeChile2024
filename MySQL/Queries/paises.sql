-- ¿Qué consulta ejecutarías para obtener todos los países que hablan español? 
-- Tu consulta debe devolver el nombre del país, el idioma y el porcentaje de habla del idioma.  
-- Tu consulta debe ordenar el resultado por porcentaje de habla del idioma en orden descendente.
SELECT nombre, idioma, porcentage FROM paises
JOIN idiomas ON paises.id = idiomas.pais_id
WHERE idioma = "Español"
ORDER BY porcentage DESC;

-- ¿Qué consulta ejecutarías para mostrar el número total de ciudades de cada país?  
-- Tu consulta debe devolver el nombre del país y el número total de ciudades. 
-- Tu consulta debe ordenar el resultado por el número de ciudades en orden descendente.
SELECT paises.nombre, COUNT(*) as total_ciudades FROM paises
JOIN ciudades ON ciudades.pais_id = paises.id
GROUP BY pais_id;
