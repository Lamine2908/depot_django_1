# Generated by Django 5.0.7 on 2024-10-03 08:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0093_planning_premiere_heure_planning_student_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planning',
            name='student',
        ),
    ]
