# Generated by Django 2.2.2 on 2019-07-01 15:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('faucet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faucet',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
