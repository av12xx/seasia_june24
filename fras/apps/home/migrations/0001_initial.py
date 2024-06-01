# Generated by Django 3.2.6 on 2023-04-06 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='registration',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=191)),
                ('department', models.CharField(max_length=191)),
                ('date', models.DateField(auto_now_add=True)),
                ('time', models.TimeField(auto_now_add=True)),
                ('image', models.TextField(null=True)),
            ],
            options={
                'db_table': 'registration',
            },
        ),
        migrations.CreateModel(
            name='attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=191)),
                ('date', models.DateField(auto_now_add=True)),
                ('time', models.TimeField(auto_now_add=True)),
                ('emp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.registration')),
            ],
            options={
                'db_table': 'attendance',
            },
        ),
    ]