# Generated by Django 3.2.8 on 2021-11-01 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_alter_product_condition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='condition',
            field=models.CharField(choices=[('2', 'ishlatilgan'), ('1', 'yangi'), ('3', 'bepul')], default='1', max_length=10),
        ),
    ]
