# Generated by Django 5.0.7 on 2024-10-04 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0103_alter_student_classe'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='matricule',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
    ]
