# Generated by Django 3.0.2 on 2020-03-11 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doner', '0004_merge_20200312_0007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloodbankinfo',
            name='img',
            field=models.ImageField(upload_to='pics'),
        ),
        migrations.AlterField(
            model_name='donerinfo',
            name='img',
            field=models.ImageField(upload_to='pics'),
        ),
    ]