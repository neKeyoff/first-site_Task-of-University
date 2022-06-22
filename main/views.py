from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def product(request):
    return render(request, 'main/product.html')


def blog(request):
    return render(request, 'main/blog.html')


def contacts(request):
    return render(request, 'main/contacts.html')

