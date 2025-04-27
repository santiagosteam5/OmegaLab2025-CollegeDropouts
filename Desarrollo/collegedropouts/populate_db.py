
from datetime import datetime, timedelta, time
from random import uniform, randint, choice
from wellbeingAI.models import StudentProfile, Scores, Course, Attendance, Class, TestResults
from django.contrib.auth.models import User

# Datos base
course_names = [
    ("Mathematics", "MATH101"),
    ("History", "HIST202"),
    ("Physics", "PHYS303"),
    ("Literature", "LIT404"),
    ("Biology", "BIO505"),
    ("Economy", "ECO606"),
]

week_days = ["Monday", "Wednesday", "Friday"]
start_times = [time(8, 0), time(10, 0), time(13, 0)]
end_times = [time(9, 30), time(11, 30), time(14, 30)]

# Crear Cursos
courses = []
for name, code in course_names:
    course = Course.objects.create(course_name=name, course_code=code)
    courses.append(course)

# Crear Clases para cada Curso (3 clases por semana * 12 semanas)
classes = []
start_date = datetime(2024, 1, 20)  # Primer lunes de mayo
for course in courses:
    for i, day in enumerate(week_days):
        for week in range(12):
            class_date = start_date + timedelta(days=(week * 7) + i)
            class_instance = Class.objects.create(
                course=course,
                day=day,
                start_time=start_times[i],
                end_time=end_times[i],
                date=class_date.date()
            )
            classes.append(class_instance)

# Crear Usuarios y Estudiantes
profiles = []
stress_profiles = ["Estrés Presente", "Estrés Presente", "Indicios de Estrés", "Indicios de Estrés", "Sin Presencia de Estrés"]
for i in range(5):
    user = User.objects.create_user(username=f'student{i+1}', password='password123')
    profile = StudentProfile.objects.create(student_name=f"Student {i+1}", user=user)
    profiles.append(profile)

# Crear Test de Estrés tipo SISCO
def generate_sisco_results(profile_type):
    if profile_type == "Estrés Presente":
        return randint(7, 10), "Alto", "Alto", "Alto"
    elif profile_type == "Indicios de Estrés":
        return randint(4, 6), "Moderado", "Moderado", "Moderado"
    else:
        return randint(1, 3), "Bajo", "Bajo", "Bajo"

for i, student in enumerate(profiles):
    stress_level, emo, fis, cond = generate_sisco_results(stress_profiles[i])
    TestResults.objects.create(
        mood=f"Test SISCO - Nivel {stress_level}",
        stress_level=stress_level,
        student_profile=student,
    )

# Crear Scores (Notas)
for i, student in enumerate(profiles):
    for course in courses:
        if stress_profiles[i] == "Estrés Presente":
            nota = round(uniform(1.5, 2.8), 1)
        elif stress_profiles[i] == "Indicios de Estrés":
            nota = round(uniform(3.0, 3.6), 1)
        else:
            nota = round(uniform(3.7, 5.0), 1)
        
        for _ in range(randint(2, 4)):
            Scores.objects.create(
                score=nota,
                student_profile=student,
                course=course
            )

# Generar Asistencias
attendance_statuses = ["Present", "Absent"]

for student in profiles:
    for course in courses:
        course_classes = Class.objects.filter(course=course)
        for class_instance in course_classes:
            status = choice(attendance_statuses)
            Attendance.objects.create(
                status=status,
                student_profile=student,
                course=course,
                class_instance=class_instance
            )
