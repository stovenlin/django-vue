# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-08 19:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InventoryUpdate',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('Name', models.CharField(db_column='Name', max_length=400)),
                ('ManufacturerPartNumber', models.CharField(db_column='ManufacturerPartNumber', max_length=400)),
                ('ManageInventoryMethodId', models.IntegerField(db_column='ManageInventoryMethodId', default=0)),
                ('StockQuantity', models.IntegerField(db_column='StockQuantity', default=1000)),
                ('UnitPrice', models.DecimalField(db_column='UnitPrice', decimal_places=4, max_digits=18)),
                ('VendorPrice', models.DecimalField(db_column='VendorPrice', decimal_places=4, max_digits=18)),
                ('UnitsPerCase', models.DecimalField(db_column='UnitsPerCase', decimal_places=4, default=20, max_digits=18)),
                ('PriceMeasure', models.CharField(db_column='PriceMeasure', default='kg', max_length=400)),
                ('VendorId', models.IntegerField(db_column='VendorId', default=103)),
                ('GCGBatchId', models.IntegerField(db_column='GCGBatchId', default=91)),
                ('published', models.BooleanField(db_column='Published', default=True)),
            ],
            options={
                'db_table': 'Inventory_update',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=100)),
                ('languageculture', models.CharField(db_column='LanguageCulture', max_length=20)),
                ('uniqueseocode', models.CharField(blank=True, db_column='UniqueSeoCode', max_length=2, null=True)),
                ('flagimagefilename', models.CharField(blank=True, db_column='FlagImageFileName', max_length=50, null=True)),
                ('rtl', models.BooleanField(db_column='Rtl')),
                ('limitedtostores', models.BooleanField(db_column='LimitedToStores')),
                ('defaultcurrencyid', models.IntegerField(db_column='DefaultCurrencyId')),
                ('published', models.BooleanField(db_column='Published')),
                ('displayorder', models.IntegerField(db_column='DisplayOrder')),
            ],
            options={
                'db_table': 'Language',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Localestringresource',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('resourcename', models.CharField(db_column='ResourceName', max_length=200)),
                ('resourcevalue', models.TextField(db_column='ResourceValue')),
            ],
            options={
                'db_table': 'LocaleStringResource',
                'managed': False,
            },
        ),
    ]