# Generated by Django 4.2.5 on 2023-10-11 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appentrega', '0002_rename_curso_curses_rename_estudiante_students'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('camada', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Curses',
        ),
    ]