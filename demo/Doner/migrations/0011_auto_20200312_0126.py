# Generated by Django 3.0.2 on 2020-03-11 19:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Doner', '0010_auto_20200312_0119'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bloodbankinfo',
            old_name='cuntry',
            new_name='country',
        ),
        migrations.RenameField(
            model_name='donerinfo',
            old_name='cuntry',
            new_name='country',
        ),
        migrations.RenameField(
            model_name='reqdonerinfo',
            old_name='cuntry',
            new_name='country',
        ),
    ]
