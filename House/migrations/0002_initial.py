# Generated by Django 4.0.4 on 2022-06-15 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
        ('House', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='latestnews',
            name='info_agent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.infoagent'),
        ),
        migrations.AddField(
            model_name='houseimage',
            name='house',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='House.house'),
        ),
        migrations.AddField(
            model_name='house',
            name='house_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='House.housetype'),
        ),
        migrations.AddField(
            model_name='house',
            name='info_agent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.infoagent'),
        ),
        migrations.AddField(
            model_name='house',
            name='real_estate_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='House.realestatetype'),
        ),
    ]
