# Generated by Django 3.0.2 on 2020-03-11 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doner', '0009_bloodbankinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donerinfo',
            name='bloodgrp',
            field=models.CharField(choices=[('A', 'A+ve'), ('B', 'B+ve'), ('AB', 'AB+ve'), ('a', 'A-ve'), ('b', 'B-ve'), ('ab', 'AB-ve')], max_length=5),
        ),
        migrations.AlterField(
            model_name='reqdonerinfo',
            name='bloodgrp',
            field=models.CharField(choices=[('A', 'A+ve'), ('B', 'B+ve'), ('AB', 'AB+ve'), ('a', 'A-ve'), ('b', 'B-ve'), ('ab', 'AB-ve')], max_length=5),
        ),
    ]
