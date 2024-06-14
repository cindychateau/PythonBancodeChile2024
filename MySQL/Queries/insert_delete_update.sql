SELECT * FROM usuarios;

-- Guardar un nuevo registro en la tabla de usuarios
-- INSERT INTO tabla (columna1, columnas2) VALUES ("Valor1", "valor2");
INSERT INTO usuarios (nombre, edad, direccion_id) VALUES ("Juana", 18, 2); -- no me da un resultado

-- Borrar un registro
DELETE FROM usuarios WHERE id = 8;

-- Actualizamos un registro
-- UPDATE tabla SET columna1 = "valor1", columna2 = "valor2" WHERE id = x
UPDATE usuarios SET edad = 19 WHERE id = 10;
UPDATE usuarios SET edad = 20, nombre = "Juanita" WHERE id = 10;

-- Mas de un registro en un solo insert
INSERT INTO usuarios (nombre, edad, direccion_id) VALUES 
("Pablo", 55, 2),
("Mare", 21, 3),
("Pastora", 22, 4);

INSERT INTO cursos (nombre) VALUES
("Python"),
("Java"), 
("Fundamentos de la Web");