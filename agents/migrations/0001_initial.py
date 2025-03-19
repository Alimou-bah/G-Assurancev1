# Generated by Django 5.1 on 2025-03-19 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom', models.CharField(max_length=30, verbose_name='Nom')),
                ('Prenom', models.CharField(max_length=30, verbose_name='Prénom')),
                ('photo_profil', models.ImageField(upload_to='images', verbose_name='Logo')),
                ('matricule', models.CharField(max_length=20, unique=True, verbose_name='Agrement')),
                ('numero_carte', models.CharField(blank=True, max_length=20, null=True, unique=True, verbose_name='Numero')),
                ('etablissement', models.CharField(max_length=50, verbose_name='Etablissement')),
                ('date', models.DateField(auto_now=True, verbose_name='Date de Création')),
                ('date_expire', models.DateField(verbose_name="Date d'Expiration")),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('phone', models.CharField(blank=True, max_length=9, null=True, verbose_name='Telephone')),
                ('adresse', models.CharField(max_length=40, verbose_name='Adresse')),
                ('statut', models.CharField(choices=[('EN REGLE', 'EN REGLE'), ('SUSPENDU', 'SUSPENDU'), ('RETIRE', 'RETIRE')], max_length=40, verbose_name='Statut')),
            ],
        ),
    ]
