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
        if request.POST.get('password') == 'teste123':
            print('Usuário {} entrou com sucesso!'.format(request.POST.get('email')))
            return redirect('/')
        else:
            print('Usuário {} digitou senha incorreta!'.format(request.POST.get('email')))
            return render(request, 'core/login.html', {'email': request.POST.get('email')})
