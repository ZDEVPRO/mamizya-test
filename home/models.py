from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class Product(models.Model):
    title = models.CharField(max_length=400)
    price = models.CharField(max_length=200)
    image = models.ImageField(upload_to='products/')
    content = RichTextField()
    additional_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class ImageItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='producs/')

    def __str__(self):
        return self.product.title
