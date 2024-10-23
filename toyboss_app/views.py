from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import TemplateView, View

from toyboss_app.models import Product


class HomeView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        products = Product.objects.filter(is_active=True)
        paginator = Paginator(products, 3)
        page_number = self.request.GET.get('page', 1)
        pages = paginator.get_page(page_number)
        context = {
            'pages': pages


        }
        return context


class ProductView(TemplateView):
    template_name = 'product.html'
    def get_context_data(self, **kwargs):
        context = {
            'products': Product.objects.filter(is_active=True)

        }
        return context


class ProductInnerView(TemplateView):
    template_name = 'product-inner.html'
    def get_context_data(self, **kwargs):
        product_pk = self.kwargs['pk']

        context = {
            'product': Product.objects.get(id=product_pk)

        }
        return context

class PublicationsView(TemplateView):
    template_name = 'publications.html'

class PublicationsInnerView(TemplateView):
    template_name = 'publications-inner.html'

class RecipesView(TemplateView):
    template_name = 'recipes.html'
    def get_context_data(self, **kwargs):
        products = Product.objects.filter(is_active=True)
        paginator = Paginator(products, 3)
        page_number = self.request.GET.get('page', 1)
        pages = paginator.get_page(page_number)
        context = {
            'pages': pages


        }
        return context

class RecipesInnerView(TemplateView):
    template_name = 'recipes-inner.html'

class AboutCompanyView(TemplateView):
    template_name = 'about-company.html'
