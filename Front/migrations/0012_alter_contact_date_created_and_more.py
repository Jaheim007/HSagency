# Generated by Django 4.0.4 on 2022-06-20 12:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Front', '0011_alter_contact_date_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 20, 12, 25, 5, 788701, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='houseslide',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 20, 12, 25, 5, 789701, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='siteinfo',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 20, 12, 25, 5, 784700, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='siteservice',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 20, 12, 25, 5, 790700, tzinfo=utc)),
        ),
    ]