from modeltranslation.translator import register, TranslationOptions
from .models import Product, ProductCategory, Recipe, About, Publication


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'ingredients')

@register(ProductCategory)
class ProductCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Publication)
class PublicationTranslationOptions(TranslationOptions):
    fields = ('name', 'description')

@register(Recipe)
class RecipeTranslationOptions(TranslationOptions):
    fields = ('name', 'description')

@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ('description',)


