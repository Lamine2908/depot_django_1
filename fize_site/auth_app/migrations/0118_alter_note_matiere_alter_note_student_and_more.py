# Generated by Django 5.0.7 on 2024-10-05 15:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0117_alter_pointage_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='matiere',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth_app.matiere'),
        ),
        migrations.AlterField(
            model_name='note',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth_app.student'),
        ),
        migrations.AlterField(
            model_name='note',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth_app.teacher'),
        ),
    ]
