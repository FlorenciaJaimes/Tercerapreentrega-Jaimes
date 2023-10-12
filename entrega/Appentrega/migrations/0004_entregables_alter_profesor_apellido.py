# Generated by Django 4.2.5 on 2023-10-12 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appentrega', '0003_curso_delete_curses'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entregables',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('FechaEntrega', models.DateField()),
                ('entregado', models.BooleanField()),
            ],
        ),
        migrations.AlterField(
            model_name='profesor',
            name='apellido',
            field=models.CharField(max_length=20),
        ),
    ]
