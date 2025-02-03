# Generated by Django 5.1.4 on 2025-02-02 15:54

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ansade_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='basket',
            name='code',
            field=models.CharField(default='DEFAULT_CODE', max_length=45),
        ),
        migrations.AddField(
            model_name='basketproduct',
            name='date_from',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='basketproduct',
            name='date_to',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pointofsale',
            name='code',
            field=models.CharField(default=django.utils.timezone.now, max_length=45),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pointofsale',
            name='type',
            field=models.CharField(default='default', max_length=45),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='code',
            field=models.CharField(default='default', max_length=45),
            preserve_default=False,
        ),
    ]
