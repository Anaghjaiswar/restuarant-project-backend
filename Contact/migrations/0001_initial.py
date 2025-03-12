# Generated by Django 5.1.4 on 2025-02-13 16:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Full Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email Address')),
                ('number', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(code='invalid_mobile_number', message='Mobile number must be exactly 10 digits.', regex='^\\d{10}$')], verbose_name='Mobile Number')),
                ('message', models.TextField(verbose_name='Message')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
