# Generated by Django 4.1.4 on 2023-01-02 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_imageitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='image.png', upload_to='products/'),
            preserve_default=False,
        ),
    ]
