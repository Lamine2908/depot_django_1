# Generated by Django 5.0.7 on 2024-10-05 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0118_alter_note_matiere_alter_note_student_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Note',
        ),
    ]
