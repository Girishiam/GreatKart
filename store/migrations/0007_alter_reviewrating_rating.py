# Generated by Django 3.2.4 on 2021-08-20 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_reviewrating_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewrating',
            name='rating',
            field=models.FloatField(null=True),
        ),
    ]
