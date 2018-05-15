from django.shortcuts import render, redirect
from restrito.models import Atividade
from contas.models import Professor


def pesquisar_atividades(request):
    context = {
        "atividades": Atividade.objects.all(),
        "titulo": "Lista Atividades"
    }
    return render(request, 'restrito/listaAtividades.html', context)


def nova_atividade(request):
    if request.POST:
        professor = Professor.objects.get(id=request.POST.get('id_professor'))
        Atividade.objects.create(
            titulo_atividade=request.POST.get('titulo'),
            descricao_atividade=request.POST.get('descricao'),
            conteudo_atividade=request.POST.get('conteudo'),
            tipo_atividade=request.POST.get('tipo'),
            extras_atividade=request.POST.get('extras'),
            id_professor_atividade=professor
        )
        return redirect('/pesquisarAtividades/')
    else:
        context = {
            "titulo": "Nova Atividade",
            "botao": "Salvar",
            "professores": Professor.objects.all()
        }
        return render(request, 'restrito/dadosAtividade.html', context)


def editar_atividade(request, id):
    if request.POST:
        professor = Professor.objects.get(id=request.POST.get('id_professor'))
        atividade = Atividade.objects.get(id_atividade=id)
        atividade.titulo_atividade = request.POST.get('titulo')
        atividade.descricao_atividade = request.POST.get('descricao')
        atividade.conteudo_atividade = request.POST.get('conteudo')
        atividade.tipo_atividade = request.POST.get('tipo')
        atividade.extras_atividade = request.POST.get('extras')
        atividade.id_professor_atividade = professor
        atividade.save()
        return redirect('/pesquisarAtividades/')

    else:
        atividade = Atividade.objects.get(id_atividade=id)
        professor = Professor.objects.all()
        context = {
            "titulo": "Editar Atividade",
            "botao": "Salvar",
            "atividade": atividade,
            "professores": professor
        }
        return render(request, 'restrito/dadosAtividade.html', context)


def excluir_atividade(request, id):
    if request.POST:
        atividade = Atividade.objects.get(id_atividade=id)
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
