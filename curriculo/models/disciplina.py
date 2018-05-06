from django.db import models
from contas.models.coordenador import Coordenador

class Disciplina(models.Model):
    id_disciplina = models.AutoField(primary_key=True)
    nome_disciplina = models.CharField(unique=True, max_length=100)
    data_disciplina = models.DateField()
    status_disciplina = models.CharField(max_length=15)
    plano_ensino_disciplina = models.CharField(max_length=50)
    carga_horaria_disciplina = models.IntegerField()
    competencias_disciplina = models.CharField(max_length=50)
    habilidades_disciplina = models.CharField(max_length=50)
    ementa_disciplina = models.CharField(max_length=50)
    conteudo_programatico_disciplina = models.CharField(max_length=100)
    bibliografia_basica_disciplina = models.CharField(max_length=100)
    bibliografia_complementar_disciplina = models.CharField(max_length=100)
    percentual_pratico = models.IntegerField()
    percentual_teorico = models.IntegerField()
    id_coordenador_disciplina = models.ForeignKey(Coordenador, models.DO_NOTHING, db_column='id_coordenador_disciplina')


    def __str__(self):
        return self.nome_disciplina

    class Meta:
        managed = False
        db_table = 'tbl_disciplina'
