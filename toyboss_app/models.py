from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Категории товаров'
        verbose_name = 'Категория товара'

    def __str__(self):
        return self.name



class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=255, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    recipes = models.TextField(verbose_name='рецепты')
    image = models.ImageField(upload_to='products_images/')

    class Meta:
        verbose_name_plural = 'Продукты'
        verbose_name = 'Продукт'

        def __str__(self):
            return self.name



