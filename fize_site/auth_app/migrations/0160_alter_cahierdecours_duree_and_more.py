# Generated by Django 5.0.7 on 2024-10-11 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0159_alter_cahierdecours_horaire'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cahierdecours',
            name='duree',
            field=models.CharField(default='00:00-00:00', max_length=15),
        ),
        migrations.AlterField(
            model_name='cahierdecours',
            name='duree_stage',
            field=models.CharField(default='00:00-00:00', max_length=15),
        ),
        migrations.AlterField(
            model_name='cahierdecours',
            name='duree_td',
            field=models.CharField(default='00:00-00:00', max_length=15),
        ),
        migrations.AlterField(
            model_name='cahierdecours',
            name='duree_theorie',
            field=models.CharField(default='00:00-00:00', max_length=15),
        ),
        migrations.AlterField(
            model_name='cahierdecours',
            name='duree_tp',
            field=models.CharField(default='00:00-00:00', max_length=15),
        ),
        migrations.AlterField(
            model_name='cahierdecours',
            name='duree_tpa',
            field=models.CharField(default='00:00-00:00', max_length=15),
        ),
        migrations.AlterField(
            model_name='cahierdecours',
            name='horaire',
            field=models.CharField(default='00:00-00:00', max_length=15),
        ),
    ]
