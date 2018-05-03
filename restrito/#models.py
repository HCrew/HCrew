from django.db import models
from contas.models import Aluno, Professor
from curriculo.models import DisciplinaOfertada

"""
    USAR MODELS QUE ESTÃO NA PASTA MODELS
"""


class Atividade(models.Model):
    id_atividade = models.AutoField(primary_key=True)
    titulo_atividade = models.CharField(unique=True, max_length=70)
    descricao_atividade = models.CharField(max_length=100, blank=True, null=True)
    conteudo_atividade = models.CharField(max_length=80)
    tipo_atividade = models.CharField(max_length=30)
    extras_atividade = models.CharField(max_length=30, blank=True, null=True)
    id_professor_atividade = models.ForeignKey(Professor, models.DO_NOTHING, db_column='id_professor_atividade')

    class Meta:
        managed = False
        db_table = 'tbl_atividade'


class AtividadeVinculada(models.Model):
    id_atividade_vinculada = models.AutoField(primary_key=True)
    id_atividade_atividade_vinculada = models.ForeignKey(Atividade, models.DO_NOTHING, db_column='id_atividade_atividade_vinculada')
    id_professor_atividade_vinculada = models.ForeignKey(Professor, models.DO_NOTHING, db_column='id_professor_atividade_vinculada')
    id_disciplina_ofertada_atividade_vinculada = models.ForeignKey(DisciplinaOfertada, models.DO_NOTHING, db_column='id_disciplina_ofertada_atividade_vinculada')
    rotulo_atividade_vinculada = models.CharField(max_length=50)
    status_atividade_vinculada = models.CharField(max_length=30)
    dt_inicio_respostas = models.DateField()
    dt_fim_respostas = models.DateField()

    class Meta:
        managed = False
        db_table = 'tbl_atividade_vinculada'


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
