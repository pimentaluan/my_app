from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def welcome(request):
    return HttpResponse('Bem-vindo ao meu blog!')

def eco(request, mensagem):
    return HttpResponse(f'Você digitou: {mensagem}')

def info(request):
    info = {"disciplina": "RAD", "framework": "Django", "semestre": "2025.2"}
    return JsonResponse(info)