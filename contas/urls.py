
from django.urls import path
from .views import (
    novoAluno, editarAluno, excluirAluno, pesquisarAluno,
    pesquisarCoordenador, novoCoordenador, editarCoordenador, excluirCoordenador,
    message_list, message_create, message_edit, message_delete,
    novoProfessor,editarProfessor, excluirProfessor, pesquisarProfessor
)

urlpatterns = [
    path('incluirAluno/', novoAluno),
    path('editarAluno/<int:id>/', editarAluno),
    path('excluirAluno/', excluirAluno),
    path('pesquisarAluno/', pesquisarAluno),


    # Mensagens
    path('mensagens/', message_list, name='message_list'),
    path('mensagens/nova/', message_create, name='message_create'),
    path('mensagens/<int:pk>/editar', message_edit, name='message_edit'),
    path('mensagens/remover', message_delete, name='message_delete'),

    #Professor
    path('incluirProfessor/', novoProfessor),
    path('editarProfessor/<int:id>/', editarProfessor),
    path('excluirProfessor/<int:id>/', excluirProfessor),
    path('pesquisarProfessor/', pesquisarProfessor),

    #Coordenador
    path('pesquisarCoordenador/', pesquisarCoordenador),
    path('novoCoordenador/', novoCoordenador),
    path('editarCoordenador/<int:id>/', editarCoordenador),
    path('excluirCoordenador/<int:id>/', excluirCoordenador)
    ]
