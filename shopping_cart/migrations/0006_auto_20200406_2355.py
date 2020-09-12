# Generated by Django 3.0.3 on 2020-04-06 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_cart', '0005_auto_20200406_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(default=None, max_length=120),
        ),
        migrations.AlterField(
            model_name='order',
            name='city',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_option',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AlterField(
            model_name='order',
            name='is_ordered',
            field=models.BooleanField(default=None),
        ),
        migrations.AlterField(
            model_name='order',
            name='is_payed',
            field=models.BooleanField(default=None),
        ),
        migrations.AlterField(
            model_name='order',
            name='is_sent',
            field=models.BooleanField(default=None),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone_number',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='postcode',
            field=models.CharField(default=None, max_length=6),
        ),
    ]