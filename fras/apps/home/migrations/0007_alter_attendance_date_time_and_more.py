# Generated by Django 4.2.2 on 2023-06-20 11:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_registration_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='date_time',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='date_time',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
    ]
