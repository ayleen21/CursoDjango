from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

def myfirstview(request): #Creando vista url
    data = {  #Creacion de diccionario
        'name': 'Ayleen' 
    }
    return JsonResponse(data)
