from django.urls import path
from . import views

# Почитай про это
# app_name = "main"

urlpatterns = [
    # path('', IndexView.as_view(), name="index"),  # Так определяются урлы для вьюх на классах
    path('', views.index),
    path('about-us', views.about),
    path('product', views.product),
    path('blog', views.blog),
    path('contacts', views.contacts)
]
