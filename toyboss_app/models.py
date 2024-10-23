from django.db import models
from ckeditor.fields import RichTextField

class ProductCategory(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Категории продуктов'
        verbose_name = 'Категория продукта'

    def __str__(self):
        return self.name



class Product(models.Model):
    recipes = models.ManyToManyField('Recipe', related_name='products')
    product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=255, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    ingredients = models.TextField(verbose_name='состав')
    image = models.ImageField(upload_to='products_images/')
    is_active = models.BooleanField()

    class Meta:
        verbose_name_plural = 'Продукты'
        verbose_name = 'Продукт'

        def __str__(self):
            return self.name

class Publication(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='publications/')

    def __str__(self):
        return self.title

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.name


class Contact(models.Model):
    phone_number = models.CharField(max_length=15)
    facebook_link = models.URLField(blank=True)
    instagram_link = models.URLField(blank=True)


class About(models.Model):
    description = RichTextField()


