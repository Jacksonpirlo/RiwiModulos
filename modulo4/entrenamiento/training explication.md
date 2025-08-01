# TRAINING DOCUMENTATION.

### 1) 
`SELECT e.id_estudiante, e.nombre_completo, c.nombre AS nombre_curso, i.fecha_inscripcion FROM estudiantes e JOIN inscripciones i ON e.id_estudiante = i.id_estudiante JOIN cursos c ON i.id_inscripcion = c.id_curso;`

### 2)

