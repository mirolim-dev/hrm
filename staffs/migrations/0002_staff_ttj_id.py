# Generated by Django 4.2.13 on 2024-05-18 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staffs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='ttj_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='staffs.ttj', verbose_name='TTJ'),
        ),
    ]
