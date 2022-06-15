# Generated by Django 4.0.4 on 2022-06-15 16:42

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
from django.utils.timezone import utc
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contry', django_countries.fields.CountryField(max_length=2)),
                ('city', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('beds', models.PositiveIntegerField(default=3, validators=[django.core.validators.MinValueValidator(1)])),
                ('price', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(1000000000)])),
                ('area', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(1000000000)])),
                ('garage_number', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(1000000000)])),
                ('rooms_number', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(1000000000)])),
                ('toillete_number', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(1000000000)])),
                ('latest_news_bool', models.BooleanField(default=False)),
                ('latitude', models.DecimalField(decimal_places=2, max_digits=5)),
                ('longitude', models.DecimalField(decimal_places=2, max_digits=5)),
                ('main_image', models.ImageField(upload_to='')),
                ('date_created', models.DateTimeField(default=datetime.datetime(2022, 6, 15, 16, 42, 58, 611616, tzinfo=utc))),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('date_deleted', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='HouseImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.URLField()),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('delete_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HousePaymentPeriod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('isactive', models.BooleanField(default=True)),
                ('description', models.TextField(null=True)),
                ('symbol', models.CharField(max_length=2)),
                ('date_created', models.DateTimeField(default=datetime.datetime(2022, 6, 15, 16, 42, 58, 606949, tzinfo=utc))),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('date_deleted', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='HouseType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_category', models.CharField(max_length=225)),
                ('date_created', models.DateTimeField(default=datetime.datetime(2022, 6, 15, 16, 42, 58, 605949, tzinfo=utc))),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('date_deleted', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='RealEstateType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('isactive', models.BooleanField(default=True)),
                ('description', models.TextField()),
                ('date_created', models.DateTimeField(default=datetime.datetime(2022, 6, 15, 16, 42, 58, 604949, tzinfo=utc))),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('date_deleted', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='LatestNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=50)),
                ('available_date', models.DateTimeField()),
                ('date_created', models.DateTimeField(default=datetime.datetime(2022, 6, 15, 16, 42, 58, 613616, tzinfo=utc))),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('date_deleted', models.DateTimeField(auto_now=True)),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='House.house')),
            ],
        ),
    ]
