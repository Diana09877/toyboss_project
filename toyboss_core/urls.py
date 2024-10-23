"""
URL configuration for toyboss_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from toyboss_app.views import HomeView, ProductView, ProductInnerView, PublicationsView, RecipesInnerView, RecipesView, \
    PublicationsInnerView, AboutCompanyView
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings

from django.conf.urls.i18n import i18n_patterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),

]

urlpatterns += i18n_patterns(
    path('', HomeView.as_view(), name='home-url'),
    path('product/', ProductView.as_view(), name='product-url'),
    path('product/<int:pk>/', ProductInnerView.as_view(), name='product-inner-url'),
    path('publications/', PublicationsView.as_view(), name='publications-url'),
    path('publications/<int:pk>/', PublicationsInnerView.as_view(), name='publications-inner-url'),
    path('recipes/', RecipesView.as_view(), name='recipes-url'),
    path('recipes/int:pk/', RecipesInnerView.as_view(), name='recipes-inner-url'),
    path('about/', AboutCompanyView.as_view(), name='about-company-url'),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)