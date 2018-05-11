from django.db import models
from .pessoa import Pessoa
# from .login import Login
# from .solicitacaoMatricula import SolicitacaoMatricula


class Aluno(Pessoa):
    ra_aluno = models.IntegerField(unique=True)
    foto_aluno = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nome

    def retorna_carga_horaria(self):
        carga_horaria_total = 0

        return carga_horaria_total  # IMPLEMENTAR ESTE METODO

    def retorna_matricula(self):
        """ Encontrando a matrícula do aluno"""
        # SolicitacaoMatricula.object.get()
        pass

    class Meta:
        managed = False
        db_table = 'tbl_aluno'
