from email.mime import image
from django.utils.text import slugify

from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100,unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name_plural = "Categories"
        verbose_name = "Category"

class Size(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "Sizes"
        verbose_name = "Size"

    def __str__(self):
        return self.name

class ProductSize(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE,related_name='product_size')
    size = models.ForeignKey(Size, on_delete=models.CASCADE,related_name='product_size')
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.size.name} ({self.stock} in stock) for {self.product.name}"


class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=100,unique=True)
    main_image = models.ImageField(upload_to='products/main/')
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Products"
        verbose_name = "Product"


    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='product_image')
    image = models.ImageField(upload_to='products/extra/')

    class Meta:
        verbose_name_plural = "ProductImages"
        verbose_name = "ProductImage"
