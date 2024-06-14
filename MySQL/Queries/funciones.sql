SELECT UPPER(nombre) as nombre_mayus FROM usuarios;

SELECT LOWER(nombre) as nombre_min FROM usuarios;

SELECT * FROM pedidos ORDER BY usuario_id;

SELECT SUM(total) FROM pedidos; -- Suma de la columna total

SELECT AVG(total) FROM pedidos; -- Promedio de la columna total

SELECT COUNT(total) FROM pedidos; -- Contando el total de registros

SELECT SUM(total), usuario_id 
FROM pedidos 
GROUP BY usuario_id;

SELECT AVG(total), usuario_id, nombre
FROM pedidos
JOIN usuarios ON pedidos.usuario_id = usuarios.id
GROUP BY usuario_id;

SELECT COUNT(*), usuario_id, nombre
FROM pedidos
JOIN usuarios ON pedidos.usuario_id = usuarios.id
GROUP BY usuario_id;