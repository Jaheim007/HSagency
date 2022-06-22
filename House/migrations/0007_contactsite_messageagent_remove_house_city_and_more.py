# Generated by Django 4.0.4 on 2022-06-22 11:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('House', '0006_city_alter_house_date_created_and_more'),
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
        migrations.CreateModel(
            name='MessageAgent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField(max_length=1000)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
                ('date_deleted', models.DateTimeField(auto_now=True)),
            ],
        ),
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
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 22, 11, 39, 26, 183003, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='housepaymentperiod',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 22, 11, 39, 26, 105648, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='housetype',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 22, 11, 39, 26, 105183, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='latestnews',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 22, 11, 39, 26, 184313, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='realestatetype',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 22, 11, 39, 26, 104326, tzinfo=utc)),
        ),
    ]