# Generated by Django 5.0.7 on 2024-07-16 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("insights", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="txn",
            name="user_category",
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name="txn",
            name="user_subcategory",
            field=models.CharField(default=None, max_length=200),
        ),
    ]
