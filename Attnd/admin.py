from django.contrib import admin
from .models import Student, StudentAttendence


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'Stu_name', 'stu_roll', 'Stu_dept', 'Stu_group')


# admin.site.register(StudentAttendence)

@admin.register(StudentAttendence)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'student_name', 'student_roll',
                    'student_present', 'attendance_date' , 'student_department','student_group')
