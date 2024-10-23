from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from toyboss_app.models import ProductCategory, Product, Publication, Recipe, Contact


@admin.register(ProductCategory)
class ProductCategoryAdmin(TranslationAdmin):
    list_display = ['id', 'name']


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    list_display = ['id', 'name']

@admin.register(Publication)
class PublicationAdmin(TranslationAdmin):
    list_display = ['id', 'name']

@admin.register(Recipe)
class RecipeAdmin(TranslationAdmin):
    list_display = ['id', 'name']


