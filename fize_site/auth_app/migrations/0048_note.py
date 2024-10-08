# Generated by Django 5.0.7 on 2024-09-17 15:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0047_delete_note'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('competence', models.CharField(max_length=15)),
                ('evaluation_1', models.FloatField()),
                ('evaluation_2', models.FloatField()),
                ('note_evaluation', models.FloatField()),
                ('moyenne_semestrielle', models.FloatField()),
                ('moyenne_annuelle', models.FloatField()),
                ('Appreciation', models.TextField(max_length=10)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='auth_app.student')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='auth_app.teacher')),
            ],
        ),
    ]
