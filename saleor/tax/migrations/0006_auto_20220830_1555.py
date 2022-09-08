# Generated by Django 3.2.14 on 2022-08-30 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tax", "0005_migrate_vatlayer"),
    ]

    operations = [
        migrations.AddField(
            model_name="taxconfiguration",
            name="tax_calculation_strategy",
            field=models.CharField(
                blank=True,
                choices=[("FLAT_RATES", "Flat rates"), ("TAX_APP", "Tax app")],
                max_length=20,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="taxconfigurationpercountry",
            name="tax_calculation_strategy",
            field=models.CharField(
                blank=True,
                choices=[("FLAT_RATES", "Flat rates"), ("TAX_APP", "Tax app")],
                max_length=20,
                null=True,
            ),
        ),
    ]