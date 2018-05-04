from django.db import models
from .pessoa import Pessoa

class Professor(Pessoa):
    apelido_professor = models.CharField(max_length=70)


    def __str__(self):
        return self.nome_professor

    def retorna_carga_horaria(self):
        return 'Metodo não implementado' #IMPLEMENTAR ESTE METODO

    class Meta:
        managed = False
        db_table = 'tbl_professor'