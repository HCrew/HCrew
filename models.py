# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
# from django.db import models

'''
   AS CLASSES DESSA MODEL JÁ FOREM DISTRIBUIDAS PARA OS MODELS DOS APP ONDE CADA UM DEVE FICAR
   NO TRELLO TEM O QUE CADA APP POSSUI DE MODEL 
'''

"""
class Aluno(models.Model):
    id_aluno = models.AutoField(primary_key=True)
    login_aluno = models.CharField(unique=True, max_length=50)
    senha_aluno = models.CharField(max_length=70)
    nome_aluno = models.CharField(max_length=100)
    email_aluno = models.CharField(unique=True, max_length=70)
    celular_aluno = models.IntegerField(unique=True)
    dt_expiracao_aluno = models.DateField()
    ra_aluno = models.IntegerField(unique=True)
    foto_aluno = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_aluno'


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
    id_disciplina_ofertada_atividade_vinculada = models.ForeignKey('TblDisciplinaOfertada', models.DO_NOTHING, db_column='id_disciplina_ofertada_atividade_vinculada')
    rotulo_atividade_vinculada = models.CharField(max_length=50)
    status_atividade_vinculada = models.CharField(max_length=30)
    dt_inicio_respostas = models.DateField()
    dt_fim_respostas = models.DateField()

    class Meta:
        managed = False
        db_table = 'tbl_atividade_vinculada'


class Coordenador(models.Model):
    id_coordenador = models.AutoField(primary_key=True)
    login_coordenador = models.CharField(unique=True, max_length=50)
    senha_coordenador = models.CharField(max_length=50)
    nome_coordenador = models.CharField(max_length=100)
    email_coordenador = models.CharField(unique=True, max_length=70)
    celular_coordenador = models.IntegerField(unique=True)
    dt_expiracao_coordenador = models.DateField()

    class Meta:
        managed = False
        db_table = 'tbl_cordenador'


class Curso(models.Model):
    id_curso = models.AutoField(primary_key=True)
    nome_curso = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'tbl_curso'


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

    class Meta:
        managed = False
        db_table = 'tbl_disciplina'


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
    id_professor_disciplina_ofertada = models.ForeignKey('TblProfessor', models.DO_NOTHING, db_column='id_professor_disciplina_ofertada', blank=True, null=True)
    metodologia_disciplina_ofertada = models.CharField(max_length=50, blank=True, null=True)
    recursos_disciplina_ofertada = models.CharField(max_length=50, blank=True, null=True)
    criterio_avaliacao_disciplina_ofertada = models.CharField(max_length=50, blank=True, null=True)
    plano_aula_disciplina_ofertada = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_disciplina_ofertada'
        unique_together = (('id_disciplina_disciplina_ofertada', 'id_curso_disciplina_ofertada', 'ano_disciplina_ofertada', 'semestre_disciplina_ofertada', 'turma_disciplina_ofertada'),)


class Entrega(models.Model):
    id_entrega = models.AutoField(primary_key=True)
    id_aluno_entrega = models.ForeignKey(Aluno, models.DO_NOTHING, db_column='id_aluno_entrega')
    id_atividade_vinculada_entrega = models.ForeignKey(AtividadeVinculada, models.DO_NOTHING, db_column='id_atividade_vinculada_entrega')
    titulo_entrega = models.CharField(max_length=50)
    resposta_entrega = models.CharField(max_length=50)
    dt_entrega_entrega = models.DateField()
    status_entrega = models.CharField(max_length=30)
    id_professor_entrega = models.ForeignKey('TblProfessor', models.DO_NOTHING, db_column='id_professor_entrega', blank=True, null=True)
    nota_entrega = models.IntegerField(blank=True, null=True)
    dt_avaliacao_entrega = models.DateField(blank=True, null=True)
    obs_entrega = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_entrega'
        unique_together = (('id_aluno_entrega', 'id_atividade_vinculada_entrega'),)


class Mensagem(models.Model):
    id_mensagem = models.AutoField(primary_key=True)
    id_aluno_mensagem = models.ForeignKey(Aluno, models.DO_NOTHING, db_column='id_aluno_mensagem')
    id_professor_mensagem = models.ForeignKey('TblProfessor', models.DO_NOTHING, db_column='id_professor_mensagem')
    assunto_mensagem = models.CharField(max_length=50)
    referencia_mensagem = models.CharField(max_length=50)
    conteudo_mensagem = models.CharField(max_length=60)
    status_mensagem = models.CharField(max_length=30)
    dt_envio_mensagem = models.DateField()
    dt_resposta_mensagem = models.DateField(blank=True, null=True)
    resposta_mensagem = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_mensagem'


class Professor(models.Model):
    id_professor = models.AutoField(primary_key=True)
    login_professor = models.CharField(unique=True, max_length=50)
    senha_professor = models.CharField(max_length=50)
    nome_professor = models.CharField(max_length=100)
    email_professor = models.CharField(unique=True, max_length=70)
    celular_professor = models.IntegerField(unique=True)
    dt_expiracao_professor = models.DateField()
    apelido_professor = models.CharField(max_length=70)

    class Meta:
        managed = False
        db_table = 'tbl_professor'


class SolicitacaoMatricula(models.Model):
    id_solicitacao_matricula = models.AutoField(primary_key=True)
    id_aluno_solicitacao_matricula = models.ForeignKey(Aluno, models.DO_NOTHING, db_column='id_aluno_solicitacao_matricula')
    id_disciplina_ofertada_solicitacao_matricula = models.IntegerField()
    dt_solicitacao_solicitacao_matricula = models.DateField()
    id_coordenador_solicitacao_matricula = models.ForeignKey(Coordenador, models.DO_NOTHING, db_column='id_coordenador_solicitacao_matricula', blank=True, null=True)
    status_solicitacao_matricula = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_solicitacao_matricula'
"""