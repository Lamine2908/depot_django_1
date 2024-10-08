# Generated by Django 5.0.7 on 2024-09-09 01:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AdjointClasse',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Administrateur',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bulletin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ctabd', models.CharField(max_length=10)),
                ('uea', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=20)),
                ('nom', models.CharField(max_length=100)),
                ('elements_constitutifs', models.FloatField()),
                ('integration', models.FloatField()),
                ('moyenne', models.FloatField()),
                ('valide', models.BooleanField()),
                ('credit', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CahierDeCours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('horaire', models.TimeField()),
                ('duree', models.CharField(max_length=100)),
                ('competence', models.CharField(max_length=200)),
                ('uea', models.CharField(max_length=200)),
                ('elements_constituifs', models.TextField()),
                ('professeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('professeur', 'date', 'horaire')},
            },
        ),
        migrations.CreateModel(
            name='Classe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comptable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Enseigner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth_app.classe')),
            ],
        ),
        migrations.CreateModel(
            name='Filiere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, unique=True)),
                ('nom', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Matiere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_matiere', models.CharField(max_length=20, unique=True)),
                ('nom_matiere', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Paiement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montant', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_paiement', models.DateTimeField(auto_now_add=True)),
                ('moyen_paiement', models.CharField(choices=[('CB', 'Carte Bancaire'), ('PP', 'Paypal'), ('BT', 'Virement Bancaire')], default='CB', max_length=2)),
                ('est_paye', models.BooleanField(default=False)),
                ('comptable', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth_app.comptable')),
            ],
        ),
        migrations.CreateModel(
            name='Planifier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Planning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metier', models.CharField(max_length=100)),
                ('jour', models.CharField(choices=[('Lundi', 'Lundi'), ('Mardi', 'Mardi'), ('Mercredi', 'Mercredi'), ('Jeudi', 'Jeudi'), ('Vendredi', 'Vendredi'), ('Samedi', 'Samedi')], max_length=10)),
                ('heure_debut', models.TimeField()),
                ('heure_fin', models.TimeField()),
                ('activite', models.CharField(max_length=200)),
                ('salle', models.CharField(max_length=50)),
                ('formateur', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Programme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_programme', models.CharField(max_length=50)),
                ('niveau', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ResponsableClasse',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ResponsableFiliere',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('profession', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Salle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('metier', models.CharField(blank=True, max_length=100, null=True)),
                ('qr_code', models.ImageField(blank=True, null=True, upload_to='qr_codes/')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('profession', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Utilisateur',
        ),
        migrations.AddField(
            model_name='enseigner',
            name='matiere',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth_app.matiere'),
        ),
        migrations.AddField(
            model_name='planifier',
            name='programme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth_app.programme'),
        ),
        migrations.AddField(
            model_name='programme',
            name='responsablefiliere',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth_app.responsablefiliere'),
        ),
        migrations.AddField(
            model_name='planifier',
            name='filiere',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth_app.responsablefiliere'),
        ),
        migrations.AddField(
            model_name='filiere',
            name='responsable',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='filieres', to='auth_app.responsablefiliere'),
        ),
        migrations.AddField(
            model_name='enseigner',
            name='salle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth_app.salle'),
        ),
        migrations.AddField(
            model_name='classe',
            name='salle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth_app.salle'),
        ),
        migrations.AddField(
            model_name='student',
            name='filiere',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth_app.filiere'),
        ),
        migrations.AddField(
            model_name='paiement',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth_app.student'),
        ),
        migrations.AddField(
            model_name='classe',
            name='students',
            field=models.ManyToManyField(related_name='matiere', to='auth_app.student'),
        ),
        migrations.AddField(
            model_name='paiement',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth_app.teacher'),
        ),
        migrations.AddField(
            model_name='enseigner',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth_app.teacher'),
        ),
        migrations.AddField(
            model_name='classe',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth_app.teacher'),
        ),
        migrations.AlterUniqueTogether(
            name='enseigner',
            unique_together={('teacher', 'matiere', 'classe', 'salle')},
        ),
    ]
