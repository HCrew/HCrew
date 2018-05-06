from django.shortcuts import render, redirect

from curriculo.models import Disciplina
from contas.models import Coordenador
from .models import Curso

# Create your views here.

#---START DISCIPLINA---#

def pesquisarDisciplinas(request):
    context = {
        "disciplina" : Disciplina.objects.all(),
        "titulo": "Lista de Disciplinas"
        }
    return render(request, 'curriculo/listaDisciplinas.html', context)


def novaDisciplina(request):
    if request.POST:
        Disciplina.objects.create(
        nome_disciplina = request.POST.get('nome'),
        data_disciplina = request.POST.get('data'),
        status_disciplina = request.POST.get('status'),
        plano_ensino_disciplina = request.POST.get('plano'),
        carga_horaria_disciplina = request.POST.get('carga'),
        competencias_disciplina = request.POST.get('competencias'),
        habilidades_disciplina = request.POST.get('habilidades'),
        ementa_disciplina = request.POST.get('ementa'),
        conteudo_programatico_disciplina = request.POST.get('conteudo'),
        bibliografia_basica_disciplina = request.POST.get('bibliografia_basica'),
        bibliografia_complementar_disciplina = request.POST.get('bibliografia_complementar'),
        percentual_pratico = request.POST.get('percentual_pratico'),
        percentual_teorico = request.POST.get('percentual_teorico'),
        id_coordenador_disciplina = request.POST.get('id')
        )
        return render(request,'/pesquisarDisciplinas/', context)

    else:
        coordenadores = Coordenador.objects.all()
        context = {
        "titulo": "Nova Disciplina",
        "botao": "Salvar",
        "coordenadores": coordenadores
        }
        return render(request, 'curriculo/dadosDisciplina.html', context)



def editarDisciplina(request, id):
    if request.POST:
        disciplina = Disciplina.objects.get(id_disciplina = id)
        disciplina.nome_disciplina = request.POST.get('nome')
        disciplina.data_disciplina = request.POST.get('data')
        disciplina.status_disciplina = request.POST.get('status')
        disciplina.plano_ensino_disciplina = request.POST.get('plano')
        disciplina.carga_horaria_disciplina = request.POST.get('carga')
        disciplina.competencias_disciplina = request.POST.get('competencias')
        disciplina.habilidades_disciplina = request.POST.get('habilidades')
        disciplina.ementa_disciplina = request.POST.get('ementa')
        disciplina.conteudo_programatico_disciplina = request.POST.get('conteudo')
        disciplina.bibliografia_basica_disciplina = request.POST.get('bibliografia_basica')
        disciplina.bibliografia_complementar_disciplina = request.POST.get('bibliografia_complementar')
        disciplina.percentual_pratico = request.POST.get('percentual_pratico')
        disciplina.percentual_teorico = request.POST.get('percentual_teorico')
        disciplina.id_coordenador_disciplina = request.POST.get('id')
        disciplina.save()

        return redirect('/pesquisarDisciplinas/')
    else:
        disciplina = Disciplina.objects.get(id_disciplina = id)
        coordenadores = Coordenador.objects.all()
        context = {
            "titulo":"Editar Disciplina",
            "botao":"Atualizar",
            "disciplina":disciplina,
            "coordenadores": coordenadores
            }
        return render(request, 'curriculo/dadosDisciplina.html', context)



def excluirDisciplina(request, id):
    if request.POST:
        disciplina = Disciplina.objects.get(id_disciplina = id)
        disciplina.delete()
        return redirect('/pesquisarDisciplinas/')
    else:
        disciplina = Disciplina.objects.get(id_disciplina = id)
        coordenadores = Coordenador.objects.all()
        context = {
            "titulo":"Excluir Disciplina",
            "botao":"Excluir",
            "disciplina": disciplina,
            "coordenadores": coordenadores
        }
        return render(request, 'curriculo/dadosDisciplina.html', context)

#----END DISCIPLINA----#


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
