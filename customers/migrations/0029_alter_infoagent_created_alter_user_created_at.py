# Generated by Django 4.0.4 on 2022-05-27 16:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0028_alter_infoagent_created_alter_user_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infoagent',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]