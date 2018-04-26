from django.shortcuts import render

# Create your views here.

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

def novaDisciplina(request):
    context = {
        "titulo": "Nova disciplina"
    }
    return render(request, 'novaDisciplina.html', context)
