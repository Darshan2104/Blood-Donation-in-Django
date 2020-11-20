# Generated by Django 3.0.2 on 2020-03-08 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BloodBankinfo',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('bb_name', models.CharField(max_length=20)),
                ('cuntry', models.CharField(max_length=15)),
                ('state', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('bb_address', models.TextField()),
                ('pincode', models.CharField(max_length=6)),
                ('bb_mobile', models.CharField(max_length=10)),
                ('bb_email', models.EmailField(max_length=254)),
                ('about', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Doner',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.CharField(max_length=10)),
                ('cuntry', models.CharField(max_length=15)),
                ('state', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('pincode', models.CharField(max_length=6)),
                ('address', models.TextField()),
                ('bloodgrp', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ReqDoner',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=20)),
                ('doctor_name', models.CharField(max_length=20)),
                ('bloodgrp', models.CharField(max_length=10)),
                ('cuntry', models.CharField(max_length=15)),
                ('state', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('hospital_address', models.TextField()),
                ('c_name', models.CharField(max_length=20)),
                ('c_mobile', models.CharField(max_length=10)),
                ('c_email', models.EmailField(max_length=254)),
            ],
        ),
    ]
