# Generated by Django 4.0.6 on 2023-11-18 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_code', models.CharField(max_length=200, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('contact', models.CharField(max_length=20)),
                ('details', models.TextField(blank=True, null=True)),
                ('address', models.TextField()),
            ],
        ),
    ]