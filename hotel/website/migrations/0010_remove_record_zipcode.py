# Generated by Django 4.2.5 on 2023-10-11 23:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_alter_hotel_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='zipcode',
        ),
    ]