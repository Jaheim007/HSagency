# Generated by Django 4.0.4 on 2022-06-21 14:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('House', '0011_alter_house_date_created_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactSite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=150)),
                ('message', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AlterField(
            model_name='house',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 21, 14, 1, 52, 772613, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='housepaymentperiod',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 21, 14, 1, 52, 767613, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='housetype',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 21, 14, 1, 52, 767613, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='latestnews',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 21, 14, 1, 52, 776613, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='realestatetype',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 21, 14, 1, 52, 766613, tzinfo=utc)),
        ),
    ]