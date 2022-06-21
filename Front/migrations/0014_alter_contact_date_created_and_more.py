# Generated by Django 4.0.4 on 2022-06-21 14:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Front', '0013_contact_localisation_map_alter_contact_date_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 21, 14, 1, 52, 781613, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='houseslide',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 21, 14, 1, 52, 781613, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='siteinfo',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 21, 14, 1, 52, 780614, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='siteservice',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 21, 14, 1, 52, 782613, tzinfo=utc)),
        ),
    ]
