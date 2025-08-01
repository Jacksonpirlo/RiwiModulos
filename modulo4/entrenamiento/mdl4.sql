-- CREATING TABLES
CREATE TABLE IF NOT EXISTS estudiantes (id_estudiante INT AUTO_INCREMENT PRIMARY KEY, nombre_completo VARCHAR(100) NOT NULL, correo_electronico VARCHAR(100), genero VARCHAR(20), identificacion INT UNIQUE, carrera VARCHAR(100), fecha_nacimiento DATE, fecha_ingreso DATE);
CREATE TABLE IF NOT EXISTS docentes  (id_docente INT AUTO_INCREMENT PRIMARY KEY, nombre_completo VARCHAR(100) NOT NULL, correo_institucional VARCHAR(100), departamento_academico VARCHAR(100), anios_experiencia INT);
CREATE TABLE IF NOT EXISTS cursos (id_curso INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(50) NOT NULL, codigo INT UNIQUE NOT NULL, creditos INT, semestre INT, id_docente INT, FOREIGN KEY (id_docente) REFERENCES docentes(id_docente));
CREATE TABLE IF NOT EXISTS inscripciones (id_inscripcion INT AUTO_INCREMENT PRIMARY KEY, id_estudiante INT, id_curso INT, fecha_inscripcion DATE NOT NULL, calificacion_final INT CHECK (calificacion_final <= 5), FOREIGN KEY (id_estudiante) REFERENCES estudiantes(id_estudiante), FOREIGN KEY (id_curso) REFERENCES cursos(id_curso));

-- HANDLE QUERYES
-- Estudiantes
INSERT INTO estudiantes (nombre_completo, correo_electronico, genero, identificacion, carrera, fecha_nacimiento, fecha_ingreso) VALUES('Yonkleiverson Daniel Agudelo Rivera', 'yoonk@gmail.com', 'masculino', 312335671, 'Ingenieria En Sistemas', '2007/10/2007', '2024/12/15');
INSERT INTO estudiantes (nombre_completo, correo_electronico, genero, identificacion, carrera, fecha_nacimiento, fecha_ingreso) VALUES('Yosneiker Sebastian Ramirez Lopez', 'yosker@gmail.com', 'masculino', 30455678, 'Musica', '2006/10/10', '2020/05/01');
INSERT INTO estudiantes (nombre_completo, correo_electronico, genero, identificacion, carrera, fecha_nacimiento, fecha_ingreso) VALUES('Yusleidy Alejandra Florez Uzcategui', 'yuslee@gmai.com', 'Femenino', 31455612, 'Ingenieria De Materiales', '2007/01/20', '2020/05/05');
INSERT INTO estudiantes (nombre_completo, correo_electronico, genero, identificacion, carrera, fecha_nacimiento, fecha_ingreso) VALUES('Walker Ferney Torres Torres', 'walkert@gmail.com', 'Masculino', 31368611, 'Ingenieria De Materiales', '2008/01/11', '2019/01/20');
INSERT INTO estudiantes (nombre_completo, correo_electronico, genero, identificacion, carrera, fecha_nacimiento, fecha_ingreso) VALUES('Sandra Estefany Rodriguez Rondon', 'teffRondon@gmail.com', 'Femenino', 29318631, 'Ingenieria Automotriz', '2005/12/26', '2014/12/12');

-- Docentes
INSERT INTO docentes (nombre_completo, correo_institucional, departamento_academico, anios_experiencia) VALUES('Carlos Roberto Rodriguez Mendez', 'baladaCarl@eti.com', 'Ingenieria', 15);
INSERT INTO docentes (nombre_completo, correo_institucional, departamento_academico, anios_experiencia) VALUES('Luisa Carolina Lopez Rincon', 'Lucaroli@eti.com', 'Musica', 5);
INSERT INTO docentes (nombre_completo, correo_institucional, departamento_academico, anios_experiencia) VALUES('Harol Santiago Florez Hincapie', 'harolfh@eti.com', 'Ingenieria', 10);

-- Cursos
INSERT INTO cursos (nombre, codigo, creditos, semestre, id_docente) VALUES('Matematicas basicas', 3109071, 4, 1, 1);
INSERT INTO cursos (nombre, codigo, creditos, semestre, id_docente) VALUES('Instrumentos 1', 3087812, 1, 2, 2);
INSERT INTO cursos (nombre, codigo, creditos, semestre, id_docente) VALUES('Calculo 2', 12332167, 4, 2, 3);
INSERT INTO cursos (nombre, codigo, creditos, semestre, id_docente) VALUES('Fisica', 23127091, 4, 3, 1);

-- Inscripciones
INSERT INTO inscripciones (id_estudiante, id_curso, fecha_inscripcion, calificacion_final) VALUES(2, 1, '2019/03/22', 4);
INSERT INTO inscripciones (id_estudiante, id_curso, fecha_inscripcion, calificacion_final) VALUES(4, 2, '2020/06/15', 3);
INSERT INTO inscripciones (id_estudiante, id_curso, fecha_inscripcion, calificacion_final) VALUES(1, 1, '2015/01/20', 5);
INSERT INTO inscripciones (id_estudiante, id_curso, fecha_inscripcion, calificacion_final) VALUES(5, 1, '2025/02/1', 5);
INSERT INTO inscripciones (id_estudiante, id_curso, fecha_inscripcion, calificacion_final) VALUES(3, 3, '2020/07/01', 2);
INSERT INTO inscripciones (id_estudiante, id_curso, fecha_inscripcion, calificacion_final) VALUES(4, 4, '2020/07/08', 1);
INSERT INTO inscripciones (id_estudiante, id_curso, fecha_inscripcion, calificacion_final) VALUES(5, 3, '2025/03/01', 5);
INSERT INTO inscripciones (id_estudiante, id_curso, fecha_inscripcion, calificacion_final) VALUES(1, 3, '2015/05/1', 3);

-- Obtener el listado de todos los estudiantes junto con sus inscripciones y cursos (JOIN).

SELECT e.id_estudiante, e.nombre_completo, c.nombre AS nombre_curso, i.fecha_inscripcion FROM estudiantes e JOIN inscripciones i ON e.id_estudiante = i.id_estudiante JOIN cursos c ON i.id_inscripcion = c.id_curso;

-- Listar los cursos dictados por docentes con más de 5 años de experiencia.

SELECT d.nombre_completo, c.nombre AS Curso, d.anios_experiencia FROM docentes d JOIN cursos c ON d.id_docente = c.id_docente WHERE d.anios_experiencia > 5;

-- Obtener el promedio de calificaciones por curso (GROUP BY + AVG).

SELECT c.nombre, AVG(calificacion_final) AS promedio FROM inscripciones i JOIN cursos c ON i.id_curso = c.id_curso GROUP BY c.id_curso;

-- Mostrar los estudiantes que están inscritos en más de un curso (HAVING COUNT(*) > 1).

SELECT e.nombre_completo, COUNT(i.id_curso ) AS cantidad FROM estudiantes e JOIN inscripciones i ON e.id_estudiante = i.id_estudiante GROUP BY e.nombre_completo HAVING COUNT(i.id_curso) > 1;

-- Agregar una nueva columna estado_academico a la tabla estudiantes (ALTER TABLE).

ALTER TABLE estudiantes ADD COLUMN estado_academico VARCHAR(100);

-- Eliminar un docente y observar el efecto en la tabla cursos (uso de ON DELETE en FK).

DELETE FROM docente WHERE id_docente = 2;

-- Consultar los cursos en los que se han inscrito más de 2 estudiantes (GROUP BY + COUNT + HAVING).

SELECT c.nombre, COUNT(i.id_estudiante) as cantidad FROM cursos c JOIN inscripciones i ON c.id_curso = i.id_curso GROUP BY c.nombre HAVING COUNT(i.id_estudiante) > 1;

-- Obtener los estudiantes cuya calificación promedio es superior al promedio general (AVG() + subconsulta).

SELECT e.nombre_completo FROM estudiantes e JOIN inscripciones i ON e.id_estudiante = i.id_estudiante GROUP BY e.nombre_completo HAVING AVG(i.calificacion_final) > (SELECT AVG(calificacion_final) FROM inscripciones)

