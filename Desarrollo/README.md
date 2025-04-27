
# Proyecto: Fry - Plataforma de Bienestar Emocional y Académico para Estudiantes

# Bienvenido a Fry

Fry es una plataforma de bienestar emocional y académico que integra tecnología de IA, análisis de datos, microservicios escalables y modelos de comportamiento emocional.

## Propósito

- Apoyar a universidades y estudiantes en la detección temprana de niveles de estrés, ansiedad, deserciones y dificultades académicas.
- Brindar informes semanales personalizados y recomendaciones para mejorar el desempeño y la salud emocional.
- Analizar datos académicos y emocionales mediante inteligencia artificial para predecir riesgos de estrés elevado o deserción.

## Tecnologías Principales

- **Backend**: Python (Django), Django Rest Framework
- **Arquitectura**: Microservicios (AWS: API Gateway, Fargate, Aurora, DynamoDB, EventBridge)
- **Autenticación**: Microsoft Identity Platform (MSAL)
- **Base de datos**: RDS (PostgreSQL), DynamoDB, S3
- **IA**: Integración con Endpoint de IA (OpenAI o AWS SageMaker, Gemini API para análisis de datos y predicciones)
- **Monitoreo**: AWS CloudWatch, X-Ray

## Componentes Clave

- **Microservicios**: Separación de responsabilidades para perfiles, bienestar, calendario, estado de ánimo, notificaciones.
- **IA Predictiva**: Análisis de riesgo de deserción y predicción de estados emocionales basados en datos reales.
- **Múltiples Bases de Datos**: Especializadas por tipo de información (académica, emocional, comunicacional).
- **Población de datos de prueba**:
  - `populate_db_actualizado.py`: estudiantes, notas, tests de estrés, asistencias.
  - `populate_grades.py`: generación de promedios finales (`Grade`) por estudiante y curso.
- **Análisis de Datos**:
  - Subida de archivos académicos para análisis IA automático.
  - Generación de reportes de riesgo personalizados.

## Estructura del Proyecto

```plaintext
/ (root)
|- README.md
|- ARCHITECTURE.md
|- BACKLOG.md
|- populate_db/
|  |- populate_db_actualizado.py
|  |- populate_grades.py
|  |- README_populate.md
|  |- README_populate_grades.md
|- docs/
|  |- architecture_diagram.png
|  |- system_overview.md
|  |- microservices_description.md
|  |- user_stories.md
|  |- data_model_description.md
|  |- stress_profiles_definition.md
|  |- ai_analysis_description.md
|- src/ (código Django)
|- .github/
|  |- ISSUE_TEMPLATE.md
|  |- PULL_REQUEST_TEMPLATE.md
```

## Ejecución Local

```bash
# Clona el repositorio
$ git clone <repo-url>

# Instala dependencias
$ pip install -r requirements.txt

# Corre migraciones
$ python manage.py migrate

# Carga los datos de prueba (datos generales)
$ python manage.py shell
>>> exec(open('populate_db/populate_db_actualizado.py').read())

# Carga los promedios de notas (Grade)
$ python manage.py shell
>>> exec(open('populate_db/populate_grades.py').read())

# Corre el servidor
$ python manage.py runserver
```

## Análisis de Datos mediante IA

- Los administradores pueden subir archivos de datos de prueba.
- La IA analiza los datos para detectar riesgos de deserción y estrés elevado.
- Se generan recomendaciones y planes de acción sugeridos.

## Autenticación

- Se utiliza Microsoft Login (MSAL).
- Se requiere cuenta institucional o cuenta de prueba configurada.

## ¿Cómo contribuir?

Consulta el archivo `CONTRIBUTING.md` para lineamientos.

## Estado del Proyecto

- Fase de Prototipo de Validación
- Datos de prueba generados
- Arquitectura escalable definida
- Análisis predictivo basado en IA integrado
