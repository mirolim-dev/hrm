# Generated by Django 4.2.13 on 2024-05-18 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('staffs', '0001_initial'),
        ('actions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffleaving',
            name='saff_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staffs.staff', verbose_name='Xodim'),
        ),
    ]