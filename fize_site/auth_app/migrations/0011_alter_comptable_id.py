# Generated by Django 5.0.7 on 2024-09-09 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0010_rename_formateur_planning_activity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comptable',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
