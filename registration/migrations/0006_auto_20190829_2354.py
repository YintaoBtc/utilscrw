# Generated by Django 2.2.3 on 2019-08-29 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0005_profile_balance_faucet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.FileField(upload_to=''),
        ),
    ]
