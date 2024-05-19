# Generated by Django 3.2.9 on 2024-05-18 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staffs', '0003_alter_staff_salary'),
        ('actions', '0004_rename_lef_at_staffleaving_left_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attandance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tracked_at', models.DateTimeField(auto_now_add=True, verbose_name='Qayd etilgan vaqt')),
                ('staff_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staffs.staff', verbose_name='Xodim')),
                ('ttj_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staffs.ttj')),
            ],
            options={
                'verbose_name': 'Davomat',
                'verbose_name_plural': 'Davomatlar',
            },
        ),
    ]