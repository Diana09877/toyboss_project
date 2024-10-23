from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Категории продуктов'
        verbose_name = 'Категория продукта'

    def __str__(self):
        return self.name



class Product(models.Model):
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




