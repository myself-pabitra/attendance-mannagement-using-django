# Generated by Django 3.2 on 2021-05-19 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Attnd', '0008_alter_studentattendence_student_present'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentattendence',
            name='Student_dept',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AddField(
            model_name='studentattendence',
            name='Student_group',
            field=models.CharField(default='', max_length=1),
        ),
    ]
