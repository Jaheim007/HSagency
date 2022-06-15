# Generated by Django 4.0.4 on 2022-05-27 15:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Front', '0020_alter_contact_created_alter_houseslide_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 27, 15, 32, 1, 462001, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='houseslide',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 27, 15, 32, 1, 463001, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='siteinfo',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 27, 15, 32, 1, 438001, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='siteservice',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 27, 15, 32, 1, 464001, tzinfo=utc)),
        ),
    ]