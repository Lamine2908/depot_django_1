# Generated by Django 5.0.7 on 2024-10-06 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0129_rename_moyen_annuel_note_moyen_semes_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='responsablefiliere',
            name='matricule',
            field=models.CharField(default='modifier', max_length=20),
        ),
        migrations.AddField(
            model_name='teacher',
            name='matricule',
            field=models.CharField(default='modifier', max_length=20),
        ),
    ]
