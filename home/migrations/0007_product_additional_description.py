# Generated by Django 4.1.4 on 2023-01-03 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_product_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='additional_description',
            field=models.TextField(default='text'),
            preserve_default=False,
        ),
    ]
