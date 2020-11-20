# Generated by Django 3.0.2 on 2020-03-26 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doner', '0017_auto_20200327_0345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donerinfo',
            name='bloodgrp',
            field=models.CharField(choices=[('A+ve', 'A+ve'), ('B+ve', 'B+ve'), ('O+ve', 'O+ve'), ('AB+ve', 'AB+ve'), ('A-ve', 'A-ve'), ('B-ve', 'B-ve'), ('O+ve', 'O+ve'), ('AB-ve', 'AB-ve')], max_length=5),
        ),
        migrations.AlterField(
            model_name='reqdonerinfo',
            name='bloodgrp',
            field=models.CharField(choices=[('A+ve', 'A+ve'), ('B+ve', 'B+ve'), ('O+ve', 'O+ve'), ('AB+ve', 'AB+ve'), ('A-ve', 'A-ve'), ('B-ve', 'B-ve'), ('O+ve', 'O+ve'), ('AB-ve', 'AB-ve')], max_length=5),
        ),
    ]