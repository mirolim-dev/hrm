# Generated by Django 4.2.13 on 2024-05-18 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actions', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staffleaving',
            old_name='saff_id',
            new_name='staff_id',
        ),
    ]
