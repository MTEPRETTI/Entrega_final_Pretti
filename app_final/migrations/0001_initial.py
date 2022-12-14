# Generated by Django 4.0.6 on 2022-08-15 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sucuarsales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zona', models.CharField(max_length=40)),
                ('rsoc', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Tecnicos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('turno', models.CharField(max_length=40)),
                ('fecha_ingreso', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=40)),
                ('modelo', models.CharField(max_length=40)),
            ],
        ),
    ]
