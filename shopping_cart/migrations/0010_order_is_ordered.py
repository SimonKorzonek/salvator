# Generated by Django 3.0.3 on 2020-04-07 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_cart', '0009_remove_order_is_ordered'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_ordered',
            field=models.BooleanField(default=False),
        ),
    ]