from django.shortcuts import render
from django.http import HttpResponse

from .models import Sales


def index(request):
    sales = Sales.objects.order_by('-created_at')
    context = {'adv': sales, 'title': 'Список объявлений'}
    return render(request, 'sales/index.html', context=context)
