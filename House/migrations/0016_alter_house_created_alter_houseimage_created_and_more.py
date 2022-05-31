# Generated by Django 4.0.4 on 2022-05-27 15:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('House', '0015_alter_house_created_alter_houseimage_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 27, 15, 59, 42, 823940, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='houseimage',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 27, 15, 59, 42, 824940, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='housepaymentperiod',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 27, 15, 59, 42, 818939, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='latestnews',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 27, 15, 59, 42, 825940, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='realestatetype',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 27, 15, 59, 42, 817939, tzinfo=utc)),
        ),
    ]
