# Generated by Django 3.0.3 on 2020-03-24 18:24

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('category', multiselectfield.db.fields.MultiSelectField(choices=[(1, 'kawy'), (2, 'fartuchy'), (3, 'akcesoria'), (5, 'inne')], default=1, max_length=7)),
                ('short_description', models.TextField(default='product list description')),
                ('long_description', models.TextField(default='product detail description')),
                ('availability', models.BooleanField()),
                ('discount', models.FloatField(default='0')),
                ('quantity_available', models.IntegerField()),
                ('price', models.IntegerField(default='0')),
                ('image', models.ImageField(default='default.jpg', upload_to='product_pics')),
            ],
        ),
    ]