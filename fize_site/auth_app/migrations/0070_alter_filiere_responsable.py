# Generated by Django 5.0.7 on 2024-09-28 18:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0069_alter_filiere_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filiere',
            name='responsable',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth_app.responsablefiliere'),
        ),
    ]
