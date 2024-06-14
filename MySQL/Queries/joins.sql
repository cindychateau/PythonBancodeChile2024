SELECT * FROM usuarios;
-- SELECT columna1, columna2 FROM tabla1
-- JOIN tabla2 ON tabla1.llave_foranea = tabla2.llaveprimaria
-- WHERE
-- ORDER
-- LIMIT

-- 1:1 Desplegar la unión entre usuarios y direcciones
-- Unir en base a direccion_id (columna de usuarios, llave foránea) = id de la tabla de direcciones
SELECT nombre, edad, direccion_id, ciudad FROM usuarios
JOIN direcciones ON usuarios.direccion_id = direcciones.id
ORDER BY ciudad ASC;


-- 1:n Desplegar la unión entre pedidos y usuarios
-- Unir en base a usuario_id (tabla de pedidos, llave foránea) = id de la tabla de usuarios
SELECT nombre, total, envio FROM pedidos
JOIN usuarios ON usuario_id = usuarios.id;

-- 1:n
SELECT * FROM usuarios
JOIN pedidos ON usuarios.id = usuario_id; -- SOLO los que coinciden en ambas tablas

-- 1:n
SELECT * FROM usuarios
LEFT JOIN pedidos ON usuarios.id = usuario_id; -- TODOS los de la primera tabla, y los coincidentes de la segunda

-- n:m
SELECT nombre, edad, actividad AS hobby FROM usuarios
JOIN usuarios_has_hobbies ON usuarios.id = usuarios_has_hobbies.usuario_id
JOIN hobbies ON hobbies.id = usuarios_has_hobbies.hobbie_id;
