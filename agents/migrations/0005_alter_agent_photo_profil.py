# Generated by Django 5.1 on 2025-03-10 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0004_alter_agent_statut'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='photo_profil',
            field=models.ImageField(upload_to='images', verbose_name='Logo'),
        ),
    ]
