# Generated by Django 5.0.7 on 2024-10-11 02:06

import datetime
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0147_alter_cahierdecours_duree_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cahierdecours',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='cahierdecours',
            name='duree',
            field=models.TimeField(default=datetime.time),
        ),
        migrations.AlterField(
            model_name='cahierdecours',
            name='duree_stage',
            field=models.TimeField(default=datetime.time),
        ),
        migrations.AlterField(
            model_name='cahierdecours',
            name='duree_td',
            field=models.TimeField(default=datetime.time),
        ),
        migrations.AlterField(
            model_name='cahierdecours',
            name='duree_theorie',
            field=models.TimeField(default=datetime.time),
        ),
        migrations.AlterField(
            model_name='cahierdecours',
            name='duree_tp',
            field=models.TimeField(default=datetime.time),
        ),
        migrations.AlterField(
            model_name='cahierdecours',
            name='duree_tpa',
            field=models.TimeField(default=datetime.time),
        ),
        migrations.AlterField(
            model_name='cahierdecours',
            name='horaire',
            field=models.TimeField(default=datetime.time),
        ),
    ]
