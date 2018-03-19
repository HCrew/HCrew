from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader


# Create your views here.

# Função para retornar view de index.html
def index(request):
    return render(request, 'core/index.html')


# Função para retornar view de contato.html
def contato(request):
    if request.method == 'GET':
        return render(request, 'core/contato.html')
    elif request.method == 'POST':
        print(request.POST)
        return redirect('/contato')


# Função para retornar view de login.html
def login(request):
    if request.method == 'GET':
        return render(request, 'core/login.html')
    elif request.method == 'POST':
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        print(request.POST)
        if email == 'herbalist@gmail.com' and password == '1234':
            return redirect('/')
        else:
            return render(request, 'core/login.html')
