# Generated by Django 4.0.4 on 2022-06-15 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('House', '0001_initial'),
        ('Front', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='houseslide',
            name='house_slide',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='House.house'),
        ),
    ]