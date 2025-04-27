from django.db import models
from django.contrib.auth.models import User

class StudentProfile(models.Model):
    student_name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.student_name

class Scores(models.Model):
    score = models.IntegerField()
    student_profile = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student_profile} - {self.course} - {self.score}"

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=10)

    def __str__(self):
        return self.course_name

class Attendance(models.Model):
    PRESENT = 'Present'
    ABSENT = 'Absent'
    STATUS_CHOICES = [
        (PRESENT, 'Present'),
        (ABSENT, 'Absent'),
    ]

    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    student_profile = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    class_instance = models.ForeignKey('Class', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student_profile} - {self.date} - {self.status}"

class Class(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    day = models.CharField(max_length=10)  # e.g., 'Monday', 'Tuesday'
    start_time = models.TimeField()
    end_time = models.TimeField()
    date = models.DateField()  # If this represents a specific class date

    def __str__(self):
        return f"{self.course} - {self.day} - {self.date}"

class TestResults(models.Model):
    mood = models.CharField(max_length=100)  # e.g., 'Happy', 'Sad', 'Stressed'
    stress_level = models.IntegerField()  # e.g., 1-10 scale
    student_profile = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)  # Optional

    def __str__(self):
        return f"{self.student_profile} - {self.mood} - {self.stress_level}"