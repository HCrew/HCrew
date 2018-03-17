from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django import forms


# Create your views here.

# Função para retornar view de index.html
def index(request):
    return render(request, 'core/index.html')


# Função para retornar view de contato.html
def contato(request):
    return render(request, 'core/contato.html')


# Função para retornar view de login.html
def login(request):
    return render(request, 'core/login.html')
