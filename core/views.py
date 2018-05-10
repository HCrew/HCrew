from django.urls import reverse
from django.db import connection
from django.shortcuts import render, redirect


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

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember = request.POST.get('remember')

        with connection.cursor() as c:
            c.execute(
                'SELECT id_aluno FROM tbl_aluno WHERE '
                'login_aluno = %s AND senha_aluno = %s',
                [username, password])
            student = c.fetchone()

        if student is not None:
            request.session.cycle_key()
            request.session['user'] = student[0]

            if not remember:
                request.session.set_expiry(0)

            return redirect(reverse('index'))

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
