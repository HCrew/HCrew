from django.db import models

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