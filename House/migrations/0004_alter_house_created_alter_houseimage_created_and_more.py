# Generated by Django 4.0.4 on 2022-05-21 12:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('House', '0003_alter_house_created_alter_houseimage_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 21, 12, 43, 59, 528775, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='houseimage',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 21, 12, 43, 59, 529769, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='housepaymentperiod',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 21, 12, 43, 59, 524803, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='housetype',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 21, 12, 43, 59, 523810, tzinfo=utc)),
        ),
    ]
