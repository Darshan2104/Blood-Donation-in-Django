from django.db import models
from django.forms import ModelForm


BG = (
    ('A+ve', 'A+ve'),
    ('B+ve', 'B+ve'),
    ('O+ve', 'O+ve'),
    ('AB+ve', 'AB+ve'),
    ('A-ve', 'A-ve'),
    ('B-ve', 'B-ve'),
    ('O+ve', 'O+ve'),
    ('AB-ve', 'AB-ve'),

)


class Donerinfo(models.Model):
    img = models.ImageField(upload_to='pics')
    name = models.CharField(max_length=20)
    email = models.EmailField()
    mobile = models.CharField(max_length=10)
    country = models.CharField(max_length=15)
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    pincode = models.CharField(max_length=6)
    address = models.TextField()
    bloodgrp = models.CharField(max_length=5, choices=BG)


class ReqDonerinfo(models.Model):
    patient_name = models.CharField(max_length=20)
    doctor_name = models.CharField(max_length=20)
    bloodgrp = models.CharField(max_length=5, choices=BG)
    country = models.CharField(max_length=15)
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    hospital_address = models.TextField()
    c_name = models.CharField(max_length=20)
    c_mobile = models.CharField(max_length=10)
    c_email = models.EmailField()


class BloodBankinfo(models.Model):
    img = models.ImageField(upload_to='pics')
    name = models.CharField(max_length=20)
    country = models.CharField(max_length=15)
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    bb_address = models.TextField()
    pincode = models.CharField(max_length=6)
    bb_mobile = models.CharField(max_length=10)
    bb_email = models.EmailField()
    about = models.TextField()


class Hospital(models.Model):
    img = models.ImageField(upload_to='pics')
    name = models.CharField(max_length=20)
    email = models.EmailField()
    mobile = models.CharField(max_length=10)
    country = models.CharField(max_length=15)
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    pincode = models.CharField(max_length=6)
    address = models.TextField()
