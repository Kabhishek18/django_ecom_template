# Generated by Django 4.1.4 on 2023-04-11 03:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0002_remove_products_bannerimage_products_image2_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="comment",
            name="postname",
        ),
        migrations.AddField(
            model_name="comment",
            name="proname",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="product_comments",
                to="products.products",
            ),
        ),
        migrations.AddField(
            model_name="products",
            name="cost_price",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="products",
            name="sell_price",
            field=models.IntegerField(default=0),
        ),
    ]
