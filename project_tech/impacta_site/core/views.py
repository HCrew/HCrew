from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader



# Create your views here.

# Função para retornar view de index.html

def index(request):
    template = loader.get_template('core/index.html')
    context = {}
    return HttpResponse(template.render(context, request))


# Função para retornar view de contato.html

def contato(request):
    template = loader.get_template('core/contato.html')
    context = {}
    return HttpResponse(template.render(context, request))

# Função para retornar view de login.html

def login(request):
    template = loader.get_template('core/login.html')
    context = {}
    return HttpResponse(template.render(context, request))
