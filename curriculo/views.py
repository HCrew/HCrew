from django.shortcuts import render, redirect

from curriculo.models import Disciplina
from .models import Curso

# Create your views here.

def pesquisarDisciplinas(request):
    context = {
        "disciplina" : Disciplina.objects.all(),
        "titulo": "Lista de Disciplinas"
        }
    return render(request, 'curriculo/listaDisciplinas.html', context)


def novaDisciplina(request):
    if request.POST:
        nome = request.POST.get('nome')
        data = request.POST.get('data')
        status = request.POST.get('status')
        plano = request.POST.get('plano')
        carga = request.POST.get('carga')
        competencias = request.POST.get('competencias')
        habilidades = request.POST.get('habilidades')
        ementa = request.POST.get('ementa')
        conteudo = request.POST.get('conteudo')
        bibliografia_basica = request.POST.get('bibliografia_basica')
        bibliografia_complementar = request.POST.get('bibliografia_complementar')
        percentual_pratico = request.POST.get('percentual_pratico')
        percentual_teorico= request.POST.get('percentual_teorico')

        Disciplina.objects.create(
        nome_disciplina = nome,
        data_disciplina = data,
        status_disciplina = status,
        plano_ensino_disciplina = plano,
        carga_horaria_disciplina = carga,
        competencias_disciplina = competencias,
        habilidades_disciplina = habilidades,
        ementa_disciplina = ementa,
        conteudo_programatico_disciplina = conteudo,
        bibliografia_basica_disciplina = bibliografia_basica,
        bibliografia_complementar_disciplina =bibliografia_complementar,
        percentual_pratico = percentual_pratico,
        percentual_teorico = percentual_teorico
        )
        return redirect('/pesquisarDisciplinas/')
    else:
        context = {
        "titulo": "Nova Disciplina",
        "botao": "Salvar"
        }
        return render(request, 'curriculo/dadosDisciplina.html', context)





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
