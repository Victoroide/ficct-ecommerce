# Generated by Django 5.2 on 2025-04-25 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_remove_order_payment_method_remove_order_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='discount_applied',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='order',
            name='discount_percentage',
            field=models.IntegerField(default=0),
        ),
    ]
