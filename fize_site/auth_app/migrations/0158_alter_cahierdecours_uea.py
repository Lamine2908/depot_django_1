# Generated by Django 5.0.7 on 2024-10-11 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0157_alter_cahierdecours_horaire'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cahierdecours',
            name='uea',
            field=models.CharField(max_length=30),
        ),
    ]
