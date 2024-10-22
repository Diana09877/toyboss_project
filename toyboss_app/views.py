from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class HomeView(TemplateView):
    template_name = 'index.html'


class ProductView(TemplateView):
    template_name = 'product.html'
