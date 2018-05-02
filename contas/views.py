from django.shortcuts import render, redirect
from contas.models import Aluno, Coordenador

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




































































#-------COORDENADOR---------#

def pesquisarCoordenador(request):
    context = {
    'coordenador': Coordenador.objects.all(),
    'titulo': 'Coordenador'
    }
    return render(request, 'listaCoordenador.html', context)

def novoCoordenador(request):
    if request.POST:
        login = request.POST.get('login')
        senha = request.POST.get('senha')
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        celular = request.POST.get('celular')
        data = request.POST.get('data')

        Coordenador.objects.create(
        login_coordenador = login,
        senha_coordenador = senha,
        nome_coordenador = nome,
        email_coordenador = email,
        celular_coordenador = celular,
        dt_expiracao_coordenador = data)
        return redirect('/pesquisarCoordenador/')
    else:
        context = {
        "titulo": "Novo Coordenador",
        "botao":"Salvar"
        }
        return render(request, 'dadosCoordenador.html', context)


def editarCoordenador(request, id):
    coordenador = Coordenador.objects.get(id_coordenador = id)
    if request.POST:
        coordenador.login_coordenador = request.POST.get("login")
        coordenador.senha_coordenador = request.POST.get("senha")
        coordenador.nome_coordenador = request.POST.get("nome")
        coordenador.email_coordenador = request.POST.get("email")
        coordenador.celular_coordenador = request.POST.get("celular")
        coordenador.dt_expiracao_coordenador = request.POST.get("data")
        coordenador.save()
        return redirect('/pesquisarCoordenador/')
    else:
        coordenador = Coordenador.objects.get(id_coordenador = id)
        context = {
        "coordenador": coordenador
        }
        return render(request, 'editar_dadosCoordenador.html', context)
