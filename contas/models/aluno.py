from django.db import models
from .pessoa import Pessoa

class Aluno(Pessoa):
    ra_aluno = models.IntegerField(unique=True)
    foto_aluno = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nome_aluno

    def retorna_carga_horaria(self):
        return 'Metodo não implementado' #IMPLEMENTAR ESTE METODO

    class Meta:
        managed = False
        db_table = 'tbl_aluno'