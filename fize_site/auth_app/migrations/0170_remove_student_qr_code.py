# Generated by Django 5.0.7 on 2024-10-13 01:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0169_alter_student_qr_code_alter_teacher_qr_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='qr_code',
        ),
    ]
