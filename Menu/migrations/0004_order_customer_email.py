# Generated by Django 5.1.4 on 2024-12-28 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Menu', '0003_order_is_paid_order_razorpay_order_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='customer_email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]
