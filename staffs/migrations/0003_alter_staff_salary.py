# Generated by Django 4.2.13 on 2024-05-18 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staffs', '0002_staff_ttj_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='salary',
            field=models.DecimalField(decimal_places=2, default=0, help_text='UZS da kiritilsin', max_digits=15, verbose_name='Maosh'),
        ),
    ]
