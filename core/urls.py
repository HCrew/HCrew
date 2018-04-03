from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contato/', views.contato, name='contato'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('cursos/', views.cursos, name='cursos'),
    path('form_novo_curso/', views.form_novo_curso, name='form_novo_curso'),
    path('disciplina_cursos/', views.disciplina_cursos, name='disciplina_cursos'),
    path('aImpacta/', views.aImpacta, name='aImpacta'),
    path('detalhesCurso/', views.detalhesCurso, name='detalhesCurso')
]
