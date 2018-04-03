from django.shortcuts import render, redirect


# Função para retornar view de index.html
def index(request):
    return render(request, 'core/index.html')


# Função para retornar view de contato.html
def contato(request):
    if request.method == 'GET':
        return render(request, 'core/contato.html')
    elif request.method == 'POST':
        print(('Nome completo: {0[Username]}\n'
               'E-mail:        {0[email]}\n'
               'Assunto:       {0[option]}\n'
               'Mensagem:      {0[message]}').format(request.POST))
        return redirect('/contato')


# Função para retornar view de login.html
def login(request):
    if request.method == 'GET':
        if not request.session.get('logged-in'):
            return render(request, 'core/login.html')

        else:
            return redirect('core:index')

    elif request.method == 'POST':
        if request.POST.get('password') == 'teste123':
            print('Usuário {} entrou com sucesso!'.format(request.POST.get('email')))
            request.session.cycle_key()
            request.session['logged-in'] = True
            not request.POST.get('rememberme') and request.session.set_expiry(0)
            return redirect('core:index')

        else:
            print('Usuário {} digitou senha incorreta!'.format(request.POST.get('email')))
            return render(request, 'core/login.html', {'email': request.POST.get('email')})


def logout(request):
    request.session.flush()
    return redirect('core:index')


def cursos(request):
    return render(request, 'core/cursos.html')


def detalhesCurso(request):
    return render(request, 'core/detalhes_curso.html')


def form_novo_curso(request):
    return render(request, 'core/form_novo_curso.html')


def disciplina_cursos(request):
    return render(request, 'core/disciplina_cursos.html')


def aImpacta(request):
    return render(request, 'core/aImpacta.html')
