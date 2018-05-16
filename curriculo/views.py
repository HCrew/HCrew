from django.shortcuts import render, redirect

from curriculo.models import Disciplina
from contas.models import Coordenador
from .models import Curso


def pesquisar_disciplinas(request):
    context = {
        "disciplina": Disciplina.objects.all(),
        "titulo": "Lista de Disciplinas"
        }
    return render(request, 'listaDisciplinas.html', context)


def visualizar_disciplina(request, id):
    if request.POST:
        print('post')
        return redirect('/pesquisarDisciplinas/')
    else:
        disciplina = Disciplina.objects.get(id_disciplina=id)
        context = {
            "titulo": "Vizualizar Disciplina",
            "botao": "Voltar",
            "disciplina": disciplina
        }
        return render(request, 'dadosDisciplina.html', context)


def nova_disciplina(request):
    if request.POST:
        Disciplina.objects.create(
            nome_disciplina=request.POST.get('nome'),
            status_disciplina=request.POST.get('status'),
            plano_ensino_disciplina=request.POST.get('plano'),
            carga_horaria_disciplina=request.POST.get('carga'),
            competencias_disciplina=request.POST.get('competencias'),
            habilidades_disciplina=request.POST.get('habilidades'),
            ementa_disciplina=request.POST.get('ementa'),
            conteudo_programatico_disciplina=request.POST.get('conteudo'),
            bibliografia_basica_disciplina=request.POST.get('bibliografia_basica'),
            bibliografia_complementar_disciplina=request.POST.get('bibliografia_complementar'),
            percentual_pratico=request.POST.get('percentual_pratico'),
            percentual_teorico=request.POST.get('percentual_teorico'),
            id_coordenador_disciplina=request.POST.get('id_coord')

        )
        return redirect('/pesquisarDisciplinas')

    else:
        coordenadores = Coordenador.objects.all()
        context = {
            "titulo": "Nova Disciplina",
            "botao": "Salvar",
            "coordenadores": coordenadores
        }
        return render(request, 'dadosDisciplina.html', context)


def editar_disciplina(request, id):
    if request.POST:
        disciplina = Disciplina.objects.get(id_disciplina=id)
        disciplina.nome_disciplina = request.POST.get('nome')
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
        disciplina.id_coordenador_disciplina = request.POST.get('id_coord')
        disciplina.save()

        return redirect('/pesquisarDisciplinas/')
    else:
        disciplina = Disciplina.objects.get(id_disciplina=id)
        coordenadores = Coordenador.objects.all()
        context = {
            "titulo": "Editar Disciplina",
            "botao": "Atualizar",
            "disciplina": disciplina,
            "coordenadores": coordenadores
            }
        return render(request, 'dadosDisciplina.html', context)


def excluir_disciplina(request, id):
    if request.POST:
        disciplina = Disciplina.objects.get(id_disciplina=id)
        disciplina.delete()
        return redirect('/pesquisarDisciplinas/')
    else:
        disciplina = Disciplina.objects.get(id_disciplina=id)
        coordenadores = Coordenador.objects.all()
        context = {
            "titulo": "Excluir Disciplina",
            "botao": "Excluir",
            "disciplina": disciplina,
            "coordenadores": coordenadores
        }
        return render(request, 'dadosDisciplina.html', context)


def novo_curso(request):
    if request.POST:
        Curso.objects.create(
            nome_curso=request.POST.get('nome')
        )
        return redirect('/pesquisarCurso/')
    else:
        context = {
            "titulo": "Novo Curso",
            "botao": "Salvar"
        }
        return render(request, 'dadosCurso.html', context)


def editar_curso(request, id):
    if request.POST:
        curso = Curso.objects.get(id_curso=id)

        curso.nome_curso = request.POST.get('nome')

        curso.save()

        return redirect('/pesquisarCurso/')
    else:
        curso = Curso.objects.get(id_curso=id)
        context = {
            "titulo": "Editar Curso",
            "botao": "Atualizar",
            "Curso": Curso,
            "curso": curso
        }
        return render(request, 'dadosCurso.html', context)


def excluir_curso(request, id):
    if request.POST:
        curso = Curso.objects.get(id_curso=id)
        curso.delete()
        return redirect('/pesquisarCurso/')
    else:
        curso = Curso.objects.get(id_curso=id)
        context = {
            "titulo": "Excluir Curso",
            "botao": "Excluir",
            "curso": curso,
        }
        return render(request, 'dadosCurso.html', context)


def pesquisar_curso(request):
    context = {
        "Cursos": Curso.objects.all(),
        "titulo": "Cursos"
    }
    return render(request, 'listaCursos.html', context)


def vizualizar_curso(request):
    context = {
        "Cursos": Curso.objects.all(),
        "titulo": "Cursos"
    }
    return render(request, 'vizualizarCursos.html', context)
