# Generated by Django 3.0.2 on 2020-03-13 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doner', '0011_auto_20200312_0126'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='pics')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.CharField(max_length=10)),
                ('country', models.CharField(max_length=15)),
                ('state', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('pincode', models.CharField(max_length=6)),
                ('address', models.TextField()),
                ('bloodgrp', models.CharField(choices=[('A', 'A+ve'), ('B', 'B+ve'), ('AB', 'AB+ve'), ('a', 'A-ve'), ('b', 'B-ve'), ('ab', 'AB-ve')], max_length=5)),
            ],
        ),
    ]
