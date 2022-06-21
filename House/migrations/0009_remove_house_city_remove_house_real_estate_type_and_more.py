# Generated by Django 4.0.4 on 2022-06-20 12:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('House', '0008_messageagent_alter_house_date_created_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='house',
            name='city',
        ),
        migrations.RemoveField(
            model_name='house',
            name='real_estate_type',
        ),
        migrations.AlterField(
            model_name='house',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 20, 12, 24, 11, 434853, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='housepaymentperiod',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 20, 12, 24, 11, 429853, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='housetype',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 20, 12, 24, 11, 428854, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='latestnews',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 20, 12, 24, 11, 436853, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='realestatetype',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 20, 12, 24, 11, 427853, tzinfo=utc)),
        ),
    ]