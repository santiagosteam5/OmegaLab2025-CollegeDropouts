
# Visión General del Sistema

### Propósito General

Fry es una plataforma desarrollada para apoyar el bienestar emocional, académico y personal de estudiantes universitarios, integrando análisis de datos académicos, evaluaciones emocionales diarias, cálculos de promedios académicos y recomendaciones personalizadas basadas en IA.

### Actores Principales

- **Estudiantes**: Usuarios que registran su estado de ánimo, reciben recomendaciones, visualizan su rendimiento académico y pueden agendar citas de apoyo psicológico.
- **Universidades**: Instituciones que gestionan perfiles de estudiantes, supervisan tendencias de bienestar y rendimiento, y reciben análisis predictivos de riesgo.
- **Psicólogos**: Profesionales que acceden a dashboards para identificar estudiantes en riesgo emocional o académico y gestionar intervenciones.

### Flujos de Información

1. **Autenticación**:
   - Los usuarios se registran o inician sesión utilizando Microsoft Identity Platform.

2. **Registro de Datos**:
   - Estudiantes ingresan su estado de ánimo diario.
   - Se reciben y almacenan datos académicos: notas individuales (`Scores`), promedios finales (`Grades`), asistencia y horarios.
   - Resultados de tests de bienestar (como SISCO) son capturados.

3. **Procesamiento Inicial**:
   - Microservicios consolidan información académica y emocional.
   - Datos son almacenados en bases especializadas (RDS, DynamoDB, S3).

4. **Análisis Predictivo mediante IA**:
   - Administradores pueden subir archivos o seleccionar datos para análisis.
   - La IA analiza comportamientos académicos y emocionales.
   - Se detectan riesgos de estrés alto, bajo rendimiento o probabilidad de deserción.
   - Se generan recomendaciones de intervención personalizadas.

5. **Visualización**:
   - Dashboards individuales para estudiantes (rendimiento y bienestar).
   - Dashboards agregados para universidades y psicólogos.
   - Reportes interpretativos generados automáticamente por la IA.

6. **Intervención y Seguimiento**:
   - El sistema sugiere acciones correctivas.
   - Los estudiantes pueden agendar citas psicológicas.
   - Se disparan notificaciones personalizadas de apoyo y motivación.

### Componentes Clave en el Ecosistema

- Microservicios específicos por dominio funcional (académico, bienestar, IA, notificaciones).
- Integración de servicios de IA para predicción temprana de riesgos.
- Bases de datos diferenciadas para almacenamiento eficiente y seguro.
- Monitoreo integral del sistema y del bienestar de la comunidad estudiantil.
