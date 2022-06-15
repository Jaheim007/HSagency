# Generated by Django 4.0.4 on 2022-05-31 12:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0029_alter_infoagent_created_alter_user_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='infoagent',
            old_name='delete_at',
            new_name='deleted',
        ),
        migrations.RenameField(
            model_name='infoagent',
            old_name='updated_at',
            new_name='updated',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='created_at',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='delete_at',
            new_name='deleted',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='updated_at',
            new_name='updated',
        ),
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('AG', 'agent'), ('CL', 'client')], max_length=255),
        ),
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=1000)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('deleted', models.DateTimeField(blank=True, null=True)),
                ('updated', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]