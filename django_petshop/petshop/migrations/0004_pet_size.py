# Generated by Django 3.2.4 on 2021-06-24 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("petshop", "0003_rename_identity_customer_document"),
    ]

    operations = [
        migrations.AddField(
            model_name="pet",
            name="size",
            field=models.CharField(default="UNSELECTED", max_length=10),
        ),
    ]