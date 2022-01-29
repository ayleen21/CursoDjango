from django.shortcuts import render

from core.erp.models import Category, Product

def myfirstview(request): #Creando vista url
    data = {                                 #Creacion de diccionario
        'name': 'Ayleen' ,
        'categories': Category.objects.all()
    }
    return render(request, 'home.html',data)

def mysecondview(request):
    data = {                               
        'name': 'Ayleen' ,
        'categories': Category.objects.all(),
        'products': Product.objects.all()
    }
    return render(request,'second.html', data)
