# Generated by Django 3.0.3 on 2020-04-10 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_cart', '0014_auto_20200408_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='option_price',
            field=models.CharField(max_length=2),
        ),
    ]
