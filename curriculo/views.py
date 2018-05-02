from django.shortcuts import render, redirect

from .models import Curso


def novoCurso(request):
    if request.POST:
        Curso.objects.create(
            nome_curso = request.POST.get('nome')
        )
        return redirect('/pesquisarCurso/')
    else:
        ############################
        context = {
        "titulo": "Novo Curso",
        "botao":"Salvar"
        }
        return render(request, 'dadosCurso.html', context)
    ####################################


def editarCurso(request, id):
    if request.POST:
        curso = Curso.objects.get(id_curso = id)
        
        curso.id_curso = request.POST.get('Id')
        curso.nome_curso = request.POST.get('nome')
        
        curso.save()
        
        return redirect('/pesquisarCurso/')
    else:

        #######################
        curso = Curso.objects.get(id_curso = id)
        context = {
            "titulo":"Editar Curso",
            "botao":"Atualizar",
            "Curso":Curso,
            "curso": curso
        }
        return render(request, 'dadosCurso.html', context)
        ###########################

def excluirCurso(request, id):
    if request.POST:
        curso = Curso.objects.get(id_curso = id)
        curso.delete()
        return redirect('/pesquisarCurso/')
    else:
        curso = Curso.objects.get(id_curso = id)
        context = {
            "titulo":"Excluir Curso",
            "botao":"Excluir",
            "curso": curso,
        }
        return render(request, 'dadosCurso.html', context)


def pesquisarCurso(request):
    context = {
        "Cursos": Curso.objects.all(),
        "titulo" :"Cursos"
    }
    return render(request, 'listaCursos.html', context)
