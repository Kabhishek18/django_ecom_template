# Generated by Django 4.1.4 on 2023-04-17 17:28

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("products", "0003_alter_products_mrp_alter_products_sell_price"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="ratings",
            unique_together={("username", "product_name")},
        ),
    ]
