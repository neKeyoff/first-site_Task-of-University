from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about-us', views.about),
    path('product', views.product),
    path('blog', views.blog),
    path('contacts', views.contacts)
]
