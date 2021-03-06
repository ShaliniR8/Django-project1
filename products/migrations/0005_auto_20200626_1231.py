# Generated by Django 3.0.7 on 2020-06-26 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20200626_0151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='ratings',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=100),
        ),
    ]
