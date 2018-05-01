from django.db import models
from django.utils.timezone import now


class Aluno(models.Model):
    id_aluno = models.AutoField(primary_key=True)
    login_aluno = models.CharField(unique=True, max_length=50)
    senha_aluno = models.CharField(max_length=70)
    nome_aluno = models.CharField(max_length=100)
    email_aluno = models.CharField(unique=True, max_length=70)
    celular_aluno = models.IntegerField(unique=True)
    dt_expiracao_aluno = models.DateField(default='1900-01-01')
    ra_aluno = models.IntegerField(unique=True)
    foto_aluno = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nome_aluno

    class Meta:
        managed = False
        db_table = 'tbl_aluno'


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


class Professor(models.Model):
    id_professor = models.AutoField(primary_key=True)
    login_professor = models.CharField(unique=True, max_length=50)
    senha_professor = models.CharField(max_length=50)
    nome_professor = models.CharField(max_length=100)
    email_professor = models.CharField(unique=True, max_length=70)
    celular_professor = models.IntegerField(unique=True)
    dt_expiracao_professor = models.DateField()
    apelido_professor = models.CharField(max_length=70)

    def __str__(self):
        return self.nome_professor

    class Meta:
        managed = False
        db_table = 'tbl_professor'


class Mensagem(models.Model):
    id_mensagem = models.AutoField(primary_key=True)
    id_aluno_mensagem = models.ForeignKey(Aluno, models.DO_NOTHING, db_column='id_aluno_mensagem')
    id_professor_mensagem = models.ForeignKey(Professor, models.DO_NOTHING, db_column='id_professor_mensagem')
    assunto_mensagem = models.CharField(max_length=50)
    referencia_mensagem = models.CharField(max_length=50)
    conteudo_mensagem = models.CharField(max_length=60)
    status_mensagem = models.CharField(max_length=30)
    dt_envio_mensagem = models.DateField(default=now)
    dt_resposta_mensagem = models.DateField(blank=True, null=True)
    resposta_mensagem = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return '{self.id_aluno_mensagem} : {self.id_professor_mensagem}'

    class Meta:
        managed = False
        db_table = 'tbl_mensagem'
