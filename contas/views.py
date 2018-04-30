from django.shortcuts import render, redirect
from contas.models import Aluno

def novoAluno(request):
    if request.POST:
        Aluno.objects.create(
            nome_aluno = request.POST.get('nome'),
            email_aluno = request.POST.get('email'),
            celular_aluno = request.POST.get('celular')
        )
        return redirect('/pesquisarAluno/')
    else:
        context = {
        "titulo": "Novo Aluno",
        "botao":"Salvar"
        }
        return render(request, 'dadosAluno.html', context)

def editarAluno(request, id):
    aluno = Aluno.objects.get(id_aluno = id)
    context = {
        "titulo":"Editar Aluno",
        "botao":"Atualizar",
        "aluno":aluno
    }
    return render(request, 'dadosAluno.html', context)


def excluirAluno(request):
    context = {
        "titulo":"Excluir Aluno",
        "botao":"Excluir"
    }
    return render(request, 'dadosAluno.html', context)


def pesquisarAluno(request):
    context = {
        "alunos": Aluno.objects.all(),
        "titulo" :"Alunos"
    }
    return render(request, 'listaAlunos.html', context)


