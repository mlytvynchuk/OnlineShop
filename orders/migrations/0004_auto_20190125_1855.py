# Generated by Django 2.1.5 on 2019-01-25 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20190125_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimages',
            name='images',
            field=models.ManyToManyField(related_name='images', to='orders.Image'),
        ),
    ]
