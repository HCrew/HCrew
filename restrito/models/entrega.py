from django.db import models
from .atividadeVinculada improt AtividadeVinculada
from contas import Professor

class Entrega(models.Model):
    id_entrega = models.AutoField(primary_key=True)
    id_aluno_entrega = models.ForeignKey(Aluno, models.DO_NOTHING, db_column='id_aluno_entrega')
    id_atividade_vinculada_entrega = models.ForeignKey(AtividadeVinculada, models.DO_NOTHING, db_column='id_atividade_vinculada_entrega')
    titulo_entrega = models.CharField(max_length=50)
    resposta_entrega = models.CharField(max_length=50)
    dt_entrega_entrega = models.DateField()
    status_entrega = models.CharField(max_length=30)
    id_professor_entrega = models.ForeignKey(Professor, models.DO_NOTHING, db_column='id_professor_entrega', blank=True, null=True)
    nota_entrega = models.IntegerField(blank=True, null=True)
    dt_avaliacao_entrega = models.DateField(blank=True, null=True)
    obs_entrega = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_entrega'
        unique_together = (('id_aluno_entrega', 'id_atividade_vinculada_entrega'),)