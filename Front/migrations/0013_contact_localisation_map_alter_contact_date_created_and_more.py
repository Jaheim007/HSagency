# Generated by Django 4.0.4 on 2022-06-21 12:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Front', '0012_alter_contact_date_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='localisation_map',
            field=models.URLField(default='https://www.google.com/maps/d/u/0/edit?mid=1b-CX92nNskrUMaStwhMyvRWPrsMQLNA&usp=sharing'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 21, 12, 32, 50, 212411, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='houseslide',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 21, 12, 32, 50, 213415, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='siteinfo',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 21, 12, 32, 50, 210410, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='siteservice',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 21, 12, 32, 50, 214376, tzinfo=utc)),
        ),
    ]