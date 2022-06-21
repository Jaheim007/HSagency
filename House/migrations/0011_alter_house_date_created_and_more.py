# Generated by Django 4.0.4 on 2022-06-21 12:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('House', '0010_house_city_alter_house_date_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 21, 12, 32, 50, 206376, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='housepaymentperiod',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 21, 12, 32, 50, 201412, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='housetype',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 21, 12, 32, 50, 200410, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='latestnews',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 21, 12, 32, 50, 209412, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='realestatetype',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 21, 12, 32, 50, 199410, tzinfo=utc)),
        ),
    ]