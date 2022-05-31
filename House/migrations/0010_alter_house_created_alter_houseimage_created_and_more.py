# Generated by Django 4.0.4 on 2022-05-23 10:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('House', '0009_alter_house_created_alter_houseimage_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 23, 10, 54, 41, 291829, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='houseimage',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 23, 10, 54, 41, 292822, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='housepaymentperiod',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 23, 10, 54, 41, 287856, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='housetype',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 23, 10, 54, 41, 284875, tzinfo=utc)),
        ),
    ]
