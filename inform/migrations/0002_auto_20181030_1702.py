# Generated by Django 2.1.1 on 2018-10-30 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inform', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='url',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='shop',
            name='address_url',
            field=models.CharField(max_length=400),
        ),
    ]