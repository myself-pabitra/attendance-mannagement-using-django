# Generated by Django 3.2 on 2021-05-19 03:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Attnd', '0010_auto_20210519_0904'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentattendence',
            old_name='student_dept',
            new_name='student_department',
        ),
    ]
