# Generated by Django 3.2 on 2021-05-18 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Attnd', '0007_alter_studentattendence_attendance_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentattendence',
            name='student_present',
            field=models.CharField(choices=[('Present', 'PR'), ('Absent', 'AB')], max_length=20),
        ),
    ]
