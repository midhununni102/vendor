# Generated by Django 4.0.6 on 2023-11-20 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_purchaseorder_actual_delivery_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseorder',
            name='fulfillment_rate',
            field=models.FloatField(default=0.0),
        ),
    ]