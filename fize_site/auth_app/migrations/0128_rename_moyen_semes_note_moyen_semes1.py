# Generated by Django 5.0.7 on 2024-10-06 00:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0127_alter_matiere_student_alter_student_matiere'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='moyen_semes',
            new_name='moyen_semes1',
        ),
    ]
