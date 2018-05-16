from django.urls import reverse
from django.shortcuts import render, redirect

from contas.models.login import Login
from contas.models.aluno import Aluno
from contas.models.professor import Professor
from contas.models.coordenador import Coordenador


def index(request):
    context = {
        "titulo": "Faculdade Impacta de Tecnologia"
    }
    return render(request, 'index.html', context)


def sobre(request):
    context = {
        "titulo": "Sobre nós"
    }
    return render(request, 'sobre.html', context)


def contato(request):
    context = {
        "titulo": "Contato"
    }
    return render(request, 'contato.html', context)


def login(request):
    context = {
        "titulo": "Área restrita"
    }
    print(request.session['user'])
    print(request.session['user_type'])

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember = request.POST.get('remember')

        try:
            login_ = Login.objects.get(login=username, senha=password)

            user = (
                Aluno.objects.filter(id_login=login_).first() or
                Professor.objects.filter(id_login=login_).first() or
                Coordenador.objects.filter(id_login=login_).first()
            )

            request.session.cycle_key()
            request.session['user'] = user.pk
            request.session['user_type'] = user.__class__.__name__.lower()

            if not remember:
                request.session.set_expiry(0)

            return redirect(reverse('index'))

        except Login.DoesNotExist:
            pass  # continua abaixo

        context['username'] = username
        context['error_message'] = 'Nome de usuário ou senha inválida. Por favor tente novamente.'

    return render(request, 'login.html', context)


def logout(request):
    request.session.flush()
    return redirect(reverse('index'))


def matricula(request):
    context = {
        "titulo": "Matricula"
    }
    return render(request, 'matricula.html', context)
