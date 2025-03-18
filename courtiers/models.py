
from django.db import models

# Create your models here.

class Courtier(models.Model):
    STATUT_CHOICES = [
        ('EN REGLE', 'EN REGLE'),
        ('SUSPENDU', 'SUSPENDU'),
        ('RETIRE', 'RETIRE'),
    ]
    nom = models.CharField(max_length=30, verbose_name='Nom')
    prenom = models.CharField(max_length=30, verbose_name='Prénom')
    photo_profil=models.ImageField(upload_to='images', verbose_name='Image')
    matricule=models.CharField(max_length=20, unique=True, verbose_name='Agrement')
    numero_carte=models.CharField(max_length=20, unique=True,verbose_name='Numero', null=True, blank=True)
    etablissement=models.CharField(max_length=50, verbose_name='Etablissement')
    date=models.DateField(auto_now=True, verbose_name='Date de Création')
    date_expire=models.DateField(verbose_name="Date d'Expiration")
    email = models.EmailField(unique=True, verbose_name='Email')
    phone=models.CharField(max_length=9,verbose_name='Telephone', null=True, blank=True)
    adresse=models.CharField(max_length=40, verbose_name='Adresse')
    statut=models.CharField(max_length=40, choices=STATUT_CHOICES, verbose_name='Statut')

    def __str__(self):
        return self.nom


    