# Generated by Django 5.1 on 2025-03-06 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0002_alter_agent_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agent',
            name='type',
        ),
    ]
