# Generated by Django 3.0.2 on 2020-03-26 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doner', '0014_auto_20200327_0145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donerinfo',
            name='img',
            field=models.ImageField(blank=True, upload_to='pics'),
        ),
    ]
