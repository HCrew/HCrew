from django.shortcuts import render

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

def cursos(request):
    context = {
        "titulo": "Nossos cursos",
        "cursos": ['Análise e Desenvolvimento de Sistemas', 'Administração', 'Gestão de Tecnologia da Informação', 'Jogos Digitais', 'Redes de Computadores', 'Banco de Dados'],
        "siglas": ['ads', 'adm', 'gti', 'jd', 'rc', 'bd'],
        "descricao": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    }
    return render(request, 'cursos.html', context)

def contato(request):
    context = {
        "titulo": "Contato"
    }
    return render(request, 'contato.html', context)

def login(request):
    context = {
        "titulo": "Área restrita"
    }
    return render(request, 'login.html', context)

def disciplinaADS(request):
    context = {
        "titulo": "Análise e Desenvolvimento de Sistemas"
    }
    return render(request, 'disciplinaADS.html', context)

def novaDisciplina(request):
    context = {
        "titulo": "Nova disciplina"
    }
    return render(request, 'novaDisciplina.html', context)

def novoAluno(request):
    context = {
        "titulo": "Novo aluno"
    }
    return render(request, 'novoAluno.html', context)

def novoCurso(request):
    context = {
        "titulo": "Novo curso"
    }
    return render(request, 'novoCurso.html', context)

def matricula(request):
    context = {
        "titulo": "Matricula"
    }
    return render(request, 'matricula.html', context)