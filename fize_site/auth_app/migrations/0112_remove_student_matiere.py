# Generated by Django 5.0.7 on 2024-10-04 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0111_alter_student_matricule'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='matiere',
        ),
    ]
