# Generated by Django 3.2 on 2021-05-18 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Attnd', '0003_rename_stu_name_student_stu_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentAttendence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=20)),
                ('student_roll', models.IntegerField()),
                ('student_present', models.CharField(choices=[('present', 'present'), ('absent', 'absent')], max_length=20)),
                ('attendance_date', models.DateField()),
            ],
        ),
    ]
