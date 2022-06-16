# Generated by Django 4.0.4 on 2022-06-16 13:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('House', '0004_alter_house_date_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 16, 13, 45, 49, 162533, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='houseimage',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='housepaymentperiod',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 16, 13, 45, 49, 157532, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='housetype',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 16, 13, 45, 49, 156532, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='latestnews',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 16, 13, 45, 49, 165532, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='realestatetype',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 16, 13, 45, 49, 155532, tzinfo=utc)),
        ),
    ]
