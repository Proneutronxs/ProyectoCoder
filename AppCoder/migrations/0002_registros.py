# Generated by Django 4.0.5 on 2022-06-23 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sereno', models.CharField(max_length=50)),
                ('planta', models.IntegerField()),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('punto', models.IntegerField()),
            ],
        ),
    ]