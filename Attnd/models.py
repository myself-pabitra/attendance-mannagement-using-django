from django.db import models

attendance = (('Present', 'PR'), ('Absent', 'AB'))
department = (('Bca', 'Bca'), ('Computer Science', 'Computer Science'),
              ('Mathematics', 'Mathematics'), ('Chemistry', 'Chemistry'), ('Physics', 'Physics'),
              ('Nutrition', 'Nutrition'))


class Student(models.Model):
    Stu_name = models.CharField(max_length=20)
    stu_roll = models.IntegerField()
    Stu_dept = models.CharField(max_length=15)
    Stu_group = models.CharField(max_length=1)


class StudentAttendence(models.Model):
    student_name = models.CharField(max_length=20)
    student_roll = models.IntegerField()
    student_present = models.CharField(max_length=20, choices=attendance)
    attendance_date = models.DateField(auto_now=True)
    student_department = models.CharField(max_length=55, choices=department)
    student_group = models.CharField(max_length=1, default='')
