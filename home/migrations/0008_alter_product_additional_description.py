# Generated by Django 4.1.4 on 2023-01-03 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_product_additional_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='additional_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
