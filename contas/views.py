from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404

from contas.models import Aluno, Professor, Mensagem, Coordenador



def novoAluno(request):
    if request.POST:
        Aluno.objects.create(
            login_aluno = request.POST.get('login'),
            senha_aluno = request.POST.get('senha'),
            nome_aluno = request.POST.get('nome'),
            email_aluno = request.POST.get('email'),
            celular_aluno = request.POST.get('celular'),
            ra_aluno = request.POST.get('ra')
        )
        return redirect('/pesquisarAluno/')
    else:
        novoRa = 0
        listRa =  Aluno.objects.values_list('ra_aluno', flat = True).order_by('ra_aluno')
        for ra in listRa:
            novoRa = ra
        novoRa += 1
        if novoRa == 1:
            novoRa = 1800000
        context = {
        "titulo": "Novo Aluno",
        "botao":"Salvar",
        "ra": novoRa
        }
        return render(request, 'contas/dadosAluno.html', context)


def editarAluno(request, id):
    if request.POST:
        aluno = Aluno.objects.get(id_aluno = id)

        aluno.login_aluno = request.POST.get('login')
        aluno.senha_aluno = request.POST.get('senha')
        aluno.nome_aluno = request.POST.get('nome')
        aluno.email_aluno = request.POST.get('email')
        aluno.celular_aluno = request.POST.get('celular')
        aluno.ra_aluno = request.POST.get('ra')

        aluno.save()

        return redirect('/pesquisarAluno/')
    else:
        aluno = Aluno.objects.get(id_aluno = id)
        context = {
            "titulo":"Editar Aluno",
            "botao":"Atualizar",
            "aluno":aluno,
            "ra": aluno.ra_aluno
        }
        return render(request, 'contas/dadosAluno.html', context)


def excluirAluno(request, id):
    if request.POST:
        aluno = Aluno.objects.get(id_aluno = id)
        aluno.delete()
        return redirect('/pesquisarAluno/')
    else:
        aluno = Aluno.objects.get(id_aluno = id)
        context = {
            "titulo":"Excluir Aluno",
            "botao":"Excluir",
            "aluno": aluno,
            "ra": aluno.ra_aluno
        }
        return render(request, 'contas/dadosAluno.html', context)


def pesquisarAluno(request):
    context = {
        "alunos": Aluno.objects.all(),
        "titulo" :"Alunos"
    }
    return render(request, 'contas/listaAlunos.html', context)





def message_create(request):
    if request.method == 'POST':
        professor = request.POST.get('professor')
        aluno = request.POST.get('aluno')
        assunto = request.POST.get('assunto')
        referencia = request.POST.get('referencia')
        conteudo = request.POST.get('conteudo')

        Mensagem.objects.create(id_professor_mensagem_id=professor,
                                id_aluno_mensagem_id=aluno,
                                assunto_mensagem=assunto,
                                referencia_mensagem=referencia,
                                conteudo_mensagem=conteudo,
                                status_mensagem='')
        return redirect(reverse('message_list'))

    alunos = Aluno.objects.all()
    professores = Professor.objects.all()
    return render(request, 'contas/message_edit.html',
                  {'professors': professores, 'students': alunos})


def message_list(request):
    ms = Mensagem.objects.all()
    return render(request, 'contas/message_list.html', {'messages': ms})


def message_edit(request, pk):
    message = get_object_or_404(Mensagem, pk=pk)

    if request.method == 'POST':
        professor = request.POST.get('professor')
        aluno = request.POST.get('aluno')
        assunto = request.POST.get('assunto')
        referencia = request.POST.get('referencia')
        conteudo = request.POST.get('conteudo')

        message.__dict__.update({'id_professor_mensagem_id': professor,
                                 'id_aluno_mensagem_id': aluno,
                                 'assunto_mensagem': assunto,
                                 'referencia_mensagem': referencia,
                                 'conteudo_mensagem': conteudo})
        message.save()
        return redirect(reverse('message_list'))

    alunos = Aluno.objects.all()
    professores = Professor.objects.all()
    return render(
        request, 'contas/message_edit.html',
        {'message': message, 'professors': professores, 'students': alunos})


def message_delete(request):
    if request.method != 'POST':
        return None

    m = get_object_or_404(Mensagem, pk=request.POST.get('pk'))
    m.delete()
    return redirect(reverse('message_list'))





def novoProfessor (request):
    if request.POST:
        Professor.objects.create(
            nome_professor = request.POST.get('nome'),
            email_professor = request.POST.get('email'),
            celular_professor = request.POST.get('celular'),
            login_professor = request.POST.get('login'),
            senha_professor = request.POST.get('senha'),
            apelido_professor = request.POST.get('apelido')
        )
        return redirect ('/pesquisarProfessor/')
    else:
        context = {
            "titulo": "Novo Professor",
            "botao": "Salvar"

        }
        return render(request, 'contas/dadosProfessor.html', context)


def editarProfessor (request, id):
    if request.POST:
        professor = Professor.objects.get(id_professor = id)

        professor.login_professor = request.POST.get('login')
        professor.senha_professor = request.POST.get('senha')
        professor.nome_professor = request.POST.get('nome')
        professor.email_professor = request.POST.get('email')
        professor.celular_professor = request.POST.get('celular')

        professor.save()

        return redirect('/pesquisarProfessor/')
    else:
        professor = Professor.objects.get(id_professor = id)
        context = {
            "titulo": "Editar Professor",
            "botao": "Atualizar",
            "professor": professor
        }
        return render(request, 'contas/dadosProfessor.html', context)


def excluirProfessor (request, id):
    professor = Professor.objects.get(id_professor = id)
    if request.POST:
        professor.delete()
        return redirect('/pesquisarAluno/')
    else:
        context = {
            "titulo": "Excluir Professor",
            "botao": "Excluir",
            "professor": professor
        }
        return render(request, 'contas/dadosProfessor.html', context)


def pesquisarProfessor (request):
    context = {
        "professores": Professor.objects.all(),
        "titulo": "Professor"
    }
    return render(request, 'contas/listaProfessor.html', context)


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

        Coordenador.objects.create(
        login_coordenador = login,
        senha_coordenador = senha,
        nome_coordenador = nome,
        email_coordenador = email,
        celular_coordenador = celular
        )
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
