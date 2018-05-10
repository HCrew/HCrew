from django.db import models
from contas.models.professor import Professor
from .atividade import Atividade
from curriculo.models.disciplinaOfertada import DisciplinaOfertada


class AtividadeVinculada(models.Model):
    id_atividade_vinculada = models.AutoField(primary_key=True)
    id_atividade_atividade_vinculada = models.ForeignKey(
        Atividade, models.DO_NOTHING, db_column='id_atividade_atividade_vinculada'
    )
    id_professor_atividade_vinculada = models.ForeignKey(
        Professor, models.DO_NOTHING, db_column='id_professor_atividade_vinculada'
    )
    id_disciplina_ofertada_atividade_vinculada = models.ForeignKey(
        DisciplinaOfertada, models.DO_NOTHING, db_column='id_disciplina_ofertada_atividade_vinculada'
    )
    rotulo_atividade_vinculada = models.CharField(max_length=50)
    status_atividade_vinculada = models.CharField(max_length=30)
    dt_inicio_respostas = models.DateField()
    dt_fim_respostas = models.DateField()

    class Meta:
        managed = False
        db_table = 'tbl_atividade_vinculada'
