
from django.urls import path
from .views import (
    novoAluno, editarAluno, excluirAluno, pesquisarAluno,
    message_create, message_edit, message_delete, message_list
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
]
