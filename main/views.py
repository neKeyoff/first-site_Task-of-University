from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "main/index.html"

    def get(self, request, *args, **kwargs):
        """
            Метод вызывается при загрузке страницы
            Тут обычно инициализируют динамические переменные класса
        """
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
            Метод вызывается при отправке запроса с типом метода 'POST'
         """
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        """
            Здесь инициализируются любые переменные для вывода на шаблон
            context - это словарь
        """
        context = super().get_context_data(**kwargs)
        return context


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

