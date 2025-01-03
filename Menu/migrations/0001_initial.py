# Generated by Django 5.1.4 on 2024-12-22 17:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(choices=[('veg', 'Veg Menu'), ('non_veg', 'Non-Veg Menu'), ('dessert', 'Desserts Menu'), ('beverage', 'Beverages Menu')], max_length=20, unique=True, verbose_name='Menu Category')),
            ],
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Dish Name')),
                ('description', models.TextField(verbose_name='Dish Description')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Price (₹)')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dishes', to='Menu.menu')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
