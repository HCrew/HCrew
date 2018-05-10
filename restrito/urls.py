from django.urls import path
from .views import (pesquisar_atividades, nova_atividade, editar_atividade, excluir_atividade)

urlpatterns = [
    path('pesquisarAtividades/', pesquisar_atividades),
    path('novaAtividade/', nova_atividade),
    path('editarAtividade/<int:id>/', editar_atividade),
    path('excluirAtividade/<int:id>/', excluir_atividade)
]
