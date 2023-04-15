# Generated by Django 4.1.4 on 2023-04-11 03:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0003_remove_comment_postname_comment_proname_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Discount",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("code", models.CharField(max_length=10, unique=True)),
                ("percent_off", models.FloatField()),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name="products",
            name="discount_percentage",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="products",
            name="quantity",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="products",
            name="cost_price",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
        ),
        migrations.AlterField(
            model_name="products",
            name="sell_price",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AddField(
            model_name="products",
            name="discount",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="dis_pro",
                to="products.discount",
            ),
        ),
    ]
