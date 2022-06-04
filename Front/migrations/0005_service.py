# Generated by Django 4.0.4 on 2022-06-04 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Front', '0004_alter_contact_latitude_alter_contact_longitude'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.URLField()),
                ('service_name', models.CharField(max_length=255)),
                ('service_description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('delete_at', models.DateTimeField(null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
