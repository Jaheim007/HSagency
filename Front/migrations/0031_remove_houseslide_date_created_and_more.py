# Generated by Django 4.0.4 on 2022-05-31 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Front', '0030_houseslide_date_created_houseslide_date_update_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='houseslide',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='houseslide',
            name='photo_house',
        ),
    ]
