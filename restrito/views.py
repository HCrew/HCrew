from django.shortcuts import render, redirect
from restrito.models import Atividade
from contas.models import Professor


# Create your views here.

def pesquisarAtividades(request):
    context = {
    "atividades": Atividade.objects.all(),
    "titulo": "Lista Atividades"
    }
    return render(request, 'restrito/listaAtividades.html', context)

def novaAtividade(request):
    if request.POST:
        Atividade.objects.create(
        titulo_atividade = request.POST.get('titulo'),
        descricao_atividade= request.POST.get('descricao'),
        conteudo_atividade= request.POST.get('conteudo'),
        tipo_atividade= request.POST.get('tipo'),
        extras_atividade= request.POST.get('extras'),
        id_professor_atividade= request.POST.get('nome_professor'),
        )
        return render(request,'/pesquisarAtividades/', context)
    else:
        context = {
        "titulo": "Nova Atividade",
        "botao": "Salvar"
        }
        return render(request, 'restrito/dadosAtividade.html', context)

def editarAtividade(request, id):
    if request.POST:
        avitidade = Atividade.objects.get(id_atividade=id)
        atividade.titulo_atividade = request.POST.get('titulo')
        atividade.descricao_atividade= request.POST.get('descricao')
        atividade.conteudo_atividade= request.POST.get('conteudo')
        atividade.tipo_atividade= request.POST.get('tipo')
        atividade.extras_atividade= request.POST.get('extras')
        atividade.id_professor_atividade= request.POST.get('nome_professor')
        atividade.save()
        return redirect('/pesquisarAtividades/')

    else:
        atividade = Atividade.objects.get(id_atividade=id)
        context = {
        "titulo": "Editar Atividade",
        "botao": "Salvar",
        "atividade": atividade
        }
        return render(request, 'restrito/dadosAtividade.html', context)


def excluirAtividade(request, id):
    if request.POST:
        avitidade = Atividade.objects.get(id_atividade=id)
        atividade.delete()
        return redirect('/pesquisarAtividades/')

    else:
        atividade = Atividade.objects.get(id_atividade=id)
        context = {
        "titulo": "Excluir Atividade",
        "botao": "Excluir",
        "atividade": atividade
        }
        return render(request, 'restrito/dadosAtividade.html', context)
