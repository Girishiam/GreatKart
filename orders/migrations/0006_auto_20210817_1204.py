# Generated by Django 3.2.4 on 2021-08-17 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_alter_orderproduct_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderproduct',
            name='product_price',
            field=models.IntegerField(max_length=10000000000),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]
