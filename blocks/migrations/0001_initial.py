# Generated by Django 2.2.5 on 2019-09-27 11:49

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Título')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Contenido')),
                ('order', models.SmallIntegerField(default=0, verbose_name='Orden')),
                ('height', models.SmallIntegerField(verbose_name='Peso')),
                ('size', models.FloatField(verbose_name='Tamaño')),
                ('difficulty', models.FloatField(verbose_name='Dificultad')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'block',
                'verbose_name_plural': 'blocks',
                'ordering': ['order', 'title'],
            },
        ),
    ]
