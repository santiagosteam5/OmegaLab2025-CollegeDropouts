
from random import uniform
from wellbeingAI.models import StudentProfile, Course, Grade

# Simulación de perfiles de estrés
stress_profiles = {
    "Student 1": "Estrés Presente",
    "Student 2": "Estrés Presente",
    "Student 3": "Indicios de Estrés",
    "Student 4": "Indicios de Estrés",
    "Student 5": "Sin Presencia de Estrés"
}

# Recuperar estudiantes y cursos
students = StudentProfile.objects.all()
courses = Course.objects.all()

# Crear Grades
for student in students:
    profile_type = stress_profiles.get(student.student_name, "Sin Presencia de Estrés")
    for course in courses:
        if profile_type == "Estrés Presente":
            grade_value = round(uniform(1.5, 2.8), 2)
        elif profile_type == "Indicios de Estrés":
            grade_value = round(uniform(3.0, 3.6), 2)
        else:  # Sin Presencia de Estrés
            grade_value = round(uniform(3.7, 5.0), 2)

        Grade.objects.create(
            grade=grade_value,
            student_profile=student,
            course=course
        )

print("¡Promedios de notas creados exitosamente!")
