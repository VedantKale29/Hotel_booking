# Generated by Django 4.2.5 on 2023-11-06 03:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0014_hotelimages'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hotelimages',
            old_name='images',
            new_name='image',
        ),
    ]
