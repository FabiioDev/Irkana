from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from core.erp.models import Category, Product


# Create your views here.

def myFirstView(request):
    data = {
        'name': 'Fito',
        'categories': Category.objects.all()
    }

    return render(request, 'index.html', data)

def mySecondView(request):
    data = {
        'name': 'Fito',
        'products': Product.objects.all()
    }

    return render(request, 'second.html', data)