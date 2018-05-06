from django.db import models
from contas.models.professor import Professor

class Atividade(models.Model):
    id_atividade = models.AutoField(primary_key=True)
    titulo_atividade = models.CharField(unique=True, max_length=70)
    descricao_atividade = models.CharField(max_length=100, blank=True, null=True)
    conteudo_atividade = models.CharField(max_length=80)
    tipo_atividade = models.CharField(max_length=30)
    extras_atividade = models.CharField(max_length=30, blank=True, null=True)
    id_professor_atividade = models.ForeignKey(Professor, models.DO_NOTHING, db_column='id_professor_atividade')

    def __str__(self):
        return self.titulo_atividade

    class Meta:
        managed = False
        db_table = 'tbl_atividade'
