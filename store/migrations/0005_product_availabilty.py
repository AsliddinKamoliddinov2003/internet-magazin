# Generated by Django 3.2.8 on 2021-10-22 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_product_color_product_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='availabilty',
            field=models.BooleanField(default=True),
        ),
    ]
