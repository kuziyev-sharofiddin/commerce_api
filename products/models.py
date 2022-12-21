from django.db import models
from django.utils.text import slugify
# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=200, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.category_name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.category_name


class QuantityVariant(models.Model):
    variant_name = models.CharField(max_length=200)

    def __str__(self):
        return self.variant_name


class ColorVarinat(models.Model):
    color_name = models.CharField(max_length=200)
    color_code = models.CharField(max_length=200)

    def __str__(self):
        return self.color_name


class SizeVariant(models.Model):
    size_name = models.CharField(max_length=200)

    def __str__(self):
        return self.size_name


class Product(models.Model):
    product_name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/products')
    price = models.FloatField()
    description = models.TextField()
    stock = models.IntegerField(default=100)

    quantity_type = models.ForeignKey(
        QuantityVariant, blank=True, null=True, on_delete=models.PROTECT)
    color_type = models.ForeignKey(
        ColorVarinat, blank=True, null=True, on_delete=models.PROTECT)
    size_type = models.ForeignKey(
        SizeVariant, blank=True, null=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.product_name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='static/products')

    def __str__(self):
        return self.product.name
