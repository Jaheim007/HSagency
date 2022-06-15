# Generated by Django 4.0.4 on 2022-05-27 14:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('House', '0011_realestatetype_remove_housetype_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 27, 14, 56, 54, 541374, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='houseimage',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 27, 14, 56, 54, 542374, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='housepaymentperiod',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 27, 14, 56, 54, 536707, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='realestatetype',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 27, 14, 56, 54, 535722, tzinfo=utc)),
        ),
    ]