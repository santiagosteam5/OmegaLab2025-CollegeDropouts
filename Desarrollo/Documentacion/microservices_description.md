
# Descripción de los Microservicios en Fry

### 1. Servicio de Autenticación y Gestión de Usuarios

- **Tecnología**: Django + Microsoft Identity Platform
- **Funcionalidad**: Maneja el registro, inicio de sesión y roles de usuarios (estudiantes, universidades, psicólogos).

### 2. Servicio de Perfil Académico

- **Tecnología**: Django + RDS PostgreSQL
- **Funcionalidad**: Gestiona los datos académicos del estudiante, incluyendo materias cursadas, horarios, asistencia, notas individuales (`Scores`) y promedios finales (`Grades`).

### 3. Servicio de Bienestar y Estado de Ánimo

- **Tecnología**: Django + RDS PostgreSQL
- **Funcionalidad**: Permite a los estudiantes registrar su estado de ánimo diario a través de una selección de emojis y genera reportes semanales de emociones.

### 4. Servicio de Calendario y Gestión de Eventos

- **Tecnología**: Django + RDS PostgreSQL
- **Funcionalidad**: Administra horarios de clases, fechas de parciales, entregas y citas psicológicas.

### 5. Servicio de Notificaciones

- **Tecnología**: Django + DynamoDB + Amazon SNS
- **Funcionalidad**: Envío de notificaciones push, recordatorios positivos, alertas de parciales y recomendaciones basadas en estados de ánimo y rendimiento.

### 6. Servicio de Dashboards y Análisis Académico

- **Tecnología**: Django + S3 + RDS PostgreSQL
- **Funcionalidad**: Genera dashboards para:
  - Estudiantes (rendimiento académico y bienestar emocional).
  - Universidades (análisis agregado de cohortes).
  - Psicólogos (detección de estudiantes en riesgo).
  - Análisis de estrés promedio por materia y desempeño académico general.

### 7. Servicio de Gestión de Asistencia

- **Tecnología**: Django + RDS PostgreSQL
- **Funcionalidad**: Almacena y procesa registros de asistencia por clase, vinculados a los análisis de estrés, rendimiento académico y predicciones de bienestar.

### 8. Servicio de Análisis Predictivo basado en IA

- **Tecnología**: Django + OpenAI API / AWS SageMaker / Gemini API
- **Funcionalidad**:
  - Analiza datos académicos y emocionales para detectar patrones.
  - Predice riesgos de estrés elevado, bajo rendimiento o deserción estudiantil.
  - Sugiere planes de acción preventivos personalizados para cada estudiante.
  - Genera resúmenes interpretativos para universidades y psicólogos.
