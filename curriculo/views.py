from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404

from contas.models import Curso


def novoCurso(request):
    if request.POST:
        Curso.objects.create(
            Id_Curso = request.POST.get('Id'),
            nome_Curso = request.POST.get('nome')
        )
        return redirect('/pesquisarCurso/')
    else:
        ############################
        context = {
        "titulo": "Novo Curso",
        "botao":"Salvar",
        "Id": novoId
        }
        return render(request, 'contas/dadosCurso.html', context)
    ####################################


def editarCurso(request, Id):
    if request.POST:
        Curso = Curso.objects.get(Id_Curso = Id)
        
        Curso.Id_Curso = request.POST.get('Id')
        Curso.nome_Curso = request.POST.get('nome')
        
        Curso.save()
        
        return redirect('/pesquisarCurso/')
    else:

        #######################
        Curso = Curso.objects.get(Id_Curso = Id)
        context = {
            "titulo":"Editar Curso",
            "botao":"Atualizar",
            "Curso":Curso,
            "Id": Curso.Id_Curso
        }
        return render(request, 'contas/dadosCurso.html', context)
        ###########################

def excluirCurso(request, Id):
    if request.POST:
        Curso = Curso.objects.get(Id_Curso = Id)
        Curso.delete()
        return redirect('/pesquisarCurso/')
    else:
        Curso = Curso.objects.get(Id_Curso = Id)
        context = {
            "titulo":"Excluir Curso",
            "botao":"Excluir",
            "Curso": Curso,
            "Id": Curso.Id_Curso
        }
        return render(request, 'contas/dadosCurso.html', context)


def pesquisarCurso(request):
    context = {
        "Cursos": Curso.objects.all(),
        "titulo" :"Cursos"
    }
    return render(request, 'contas/listaCursos.html', context)

