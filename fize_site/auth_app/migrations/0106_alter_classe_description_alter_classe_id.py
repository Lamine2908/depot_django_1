# Generated by Django 5.0.7 on 2024-10-04 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0105_remove_responsablefiliere_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classe',
            name='description',
            field=models.TextField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='classe',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
    ]
