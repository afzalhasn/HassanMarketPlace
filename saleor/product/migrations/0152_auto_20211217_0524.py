# Generated by Django 3.2.6 on 2021-12-17 11:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tax", "0001_initial"),
        ("product", "0151_productchannellisting_product_pro_discoun_3145f3_btree"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="tax_group",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="tax.taxgroup",
            ),
        ),
        migrations.AddField(
            model_name="producttype",
            name="tax_group",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="tax.taxgroup",
            ),
        ),
    ]