# Generated by Django 4.1.4 on 2023-04-11 03:47

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0005_discount_created_on_discount_updated_on"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="products",
            name="discount_percentage",
        ),
    ]