# Generated by Django 3.2.6 on 2023-04-10 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='image',
            field=models.TextField(null=True),
        ),
    ]