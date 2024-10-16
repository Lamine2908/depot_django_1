# Generated by Django 5.0.7 on 2024-10-11 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0165_teacher_classe_alter_classe_teacher_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classe',
            name='teacher',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='classe',
        ),
        migrations.AddField(
            model_name='classe',
            name='teacher',
            field=models.ManyToManyField(null=True, related_name='teachers', to='auth_app.teacher'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='classe',
            field=models.ManyToManyField(null=True, related_name='classes', to='auth_app.classe'),
        ),
    ]
