# Generated by Django 5.0.7 on 2024-09-17 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0040_note'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='id',
        ),
        migrations.AddField(
            model_name='note',
            name='competence',
            field=models.TextField(default='compt'),
        ),
        migrations.AlterField(
            model_name='note',
            name='code_note',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
