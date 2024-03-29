# Generated by Django 2.2.2 on 2019-07-01 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faucet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('ip_user', models.CharField(max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('completed', models.BooleanField(default=False, verbose_name='Completo')),
            ],
            options={
                'verbose_name': 'faucet',
                'verbose_name_plural': 'faucets',
                'ordering': ['username'],
            },
        ),
    ]
