from django.urls import path
from .views import ( pesquisarAtividades, novaAtividade, editarAtividade, excluirAtividade)

urlpatterns = [
path('pesquisarAtividades/', pesquisarAtividades),
path('novaAtividade/', novaAtividade),
path('editarAtividade/<int:id>/', editarAtividade),
path('excluirAtividade/<int:id>/', excluirAtividade)
]
