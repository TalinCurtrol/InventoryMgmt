# Generated by Django 5.0.3 on 2024-03-07 10:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sku',
            name='order_code',
        ),
        migrations.AlterField(
            model_name='order',
            name='process_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 7, 21, 28, 16, 798063), verbose_name='Order date'),
        ),
        migrations.AlterField(
            model_name='sku',
            name='instock_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 7, 21, 28, 16, 797041), verbose_name='In-stock date'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='deal_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 7, 21, 28, 16, 797041)),
        ),
    ]
