from contas.models import Professor

class DisciplinaOfertada(models.Model):
    id_disciplina_ofertada = models.AutoField(primary_key=True)
    id_coordenador_disciplina_ofertada = models.ForeignKey(Coordenador, models.DO_NOTHING, db_column='id_coordenador_disciplina_ofertada')
    dt_inicio_matricula_disciplina_ofertada = models.DateField(blank=True, null=True)
    dt_fim_matricula_disciplina_ofertada = models.DateField(blank=True, null=True)
    id_disciplina_disciplina_ofertada = models.IntegerField()
    id_curso_disciplina_ofertada = models.IntegerField()
    ano_disciplina_ofertada = models.IntegerField()
    semestre_disciplina_ofertada = models.IntegerField()
    turma_disciplina_ofertada = models.CharField(max_length=10)
    id_professor_disciplina_ofertada = models.ForeignKey(Professor, models.DO_NOTHING, db_column='id_professor_disciplina_ofertada', blank=True, null=True)
    metodologia_disciplina_ofertada = models.CharField(max_length=50, blank=True, null=True)
    recursos_disciplina_ofertada = models.CharField(max_length=50, blank=True, null=True)
    criterio_avaliacao_disciplina_ofertada = models.CharField(max_length=50, blank=True, null=True)
    plano_aula_disciplina_ofertada = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_disciplina_ofertada'
        unique_together = (('id_disciplina_disciplina_ofertada', 'id_curso_disciplina_ofertada', 'ano_disciplina_ofertada', 'semestre_disciplina_ofertada', 'turma_disciplina_ofertada'),)