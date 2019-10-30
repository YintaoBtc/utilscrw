# Generated by Django 2.2.5 on 2019-09-27 11:50

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Date of created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Date of edition')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True, verbose_name='Título')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Contenido')),
                ('image', models.FileField(upload_to='')),
                ('addr_shop', models.CharField(max_length=100)),
                ('addr_donate', models.CharField(blank=True, max_length=100, null=True)),
                ('amount_goal', models.FloatField()),
                ('amount_donate', models.FloatField(blank=True, null=True)),
                ('progress', models.CharField(blank=True, max_length=100, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('completed', models.BooleanField(default=False, verbose_name='Completo')),
                ('categories', models.ManyToManyField(related_name='get_projects', to='projects.Category', verbose_name='Categories')),
            ],
            options={
                'verbose_name': 'proyecto',
                'verbose_name_plural': 'proyectos',
                'ordering': ['title'],
            },
        ),
    ]
