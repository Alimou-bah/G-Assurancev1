import email
from django.db import models
from django.forms import EmailField


class Controler(models.Model):
        nom = models.CharField(max_length=30, verbose_name='Nom')
        prenom = models.CharField(max_length=30, verbose_name='Prénom')
        email = models.EmailField(unique=True, verbose_name='Email' )

# Create your models here.
