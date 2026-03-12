from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from datetime import date

def welcome(request):
    nome = "Luan"
    data = date.today()
    is_logged_in = True
    role = 'admin'
    produtos = [
        {"nome": "Iphone", "preço": 10000},
        {"nome": "Macbook", "preço": 12000},
        {"nome": "Dolphin Mini", "preço": 120000},
    ]
    
    numero = 988888888

    context={
        "nome": nome,
        "data": data,
        "is_logged_in":is_logged_in,
        "role": role,
        "produtos": produtos,
        "numero": numero
    }
    return render(request, "blog/welcome.html", context)

def eco(request, mensagem):
    return HttpResponse(f'Você digitou: {mensagem}')

def info(request):
    info = {"disciplina": "RAD", "framework": "Django", "semestre": "2025.2"}
    return JsonResponse(info)

def home(request):
    return render(request, "blog/home.html")

def contato(request, numero):
    context = {
        "numero": numero,
    }
    return render(request, "blog/contato.html", context)