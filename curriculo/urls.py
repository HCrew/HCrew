from django.urls import path
from .views import(
    novoCurso, editarCurso, excluirCurso, pesquisarCurso, pesquisarDisciplinas, novaDisciplina)

urlpatterns = [
    path('incluirCurso/', novoCurso),
    path('editarCurso/<int:id>/', editarCurso),
    path('excluirCurso/<int:id>/', excluirCurso),
    path('pesquisarCurso/', pesquisarCurso),
    path('pesquisarDisciplinas/', pesquisarDisciplinas),
    path('novaDisciplina/', novaDisciplina)
]
