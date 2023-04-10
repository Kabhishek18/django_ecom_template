# Generated by Django 4.1.4 on 2023-04-10 10:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="products",
            name="bannerimage",
        ),
        migrations.AddField(
            model_name="products",
            name="image2",
            field=models.ImageField(default="default.png", upload_to="images/"),
        ),
        migrations.AddField(
            model_name="products",
            name="image3",
            field=models.ImageField(default="default.png", upload_to="images/"),
        ),
    ]
