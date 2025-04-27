import os
import sys
import csv
import django

# Add the project root directory to the Python path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(project_root)

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'collegedropouts.settings')
django.setup()

from wellbeingAI.models import StudentProfile, Scores, Grade, Course, Attendance, Class, TestResults

# Function to export a queryset to a CSV file
def export_to_csv(queryset, file_name, fields):
    with open(file_name, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(fields)  # Write header
        for obj in queryset:
            writer.writerow([getattr(obj, field) for field in fields])

# Export data from each model
export_to_csv(StudentProfile.objects.all(), 'student_profiles.csv', ['id', 'student_name', 'user_id'])
export_to_csv(Scores.objects.all(), 'scores.csv', ['id', 'score', 'student_profile_id', 'course_id'])
export_to_csv(Grade.objects.all(), 'grades.csv', ['id', 'grade', 'student_profile_id', 'course_id'])
export_to_csv(Course.objects.all(), 'courses.csv', ['id', 'course_name', 'course_code'])
export_to_csv(Attendance.objects.all(), 'attendance.csv', ['id', 'status', 'student_profile_id', 'course_id', 'class_instance_id'])
export_to_csv(Class.objects.all(), 'classes.csv', ['id', 'course_id', 'day', 'start_time', 'end_time', 'date'])
export_to_csv(TestResults.objects.all(), 'test_results.csv', ['id', 'mood', 'stress_level', 'student_profile_id', 'course_id'])

print("Data exported successfully!")