# Generated by Django 5.1.4 on 2024-12-24 06:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(code='invalid_mobile_number', message='Mobile number must be exactly 10 digits.', regex='^\\d{10}$')], verbose_name='Mobile Number')),
                ('email', models.EmailField(max_length=254)),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('guests', models.IntegerField()),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Book Table',
                'verbose_name_plural': 'Book Tables',
                'ordering': ['-created_at'],
            },
        ),
    ]
