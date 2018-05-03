from django.db import models

class Coordenador(models.Model):
    id_coordenador = models.AutoField(primary_key=True)
    login_coordenador = models.CharField(unique=True, max_length=50)
    senha_coordenador = models.CharField(max_length=50)
    nome_coordenador = models.CharField(max_length=100)
    email_coordenador = models.CharField(unique=True, max_length=70)
    celular_coordenador = models.IntegerField(unique=True)
    dt_expiracao_coordenador = models.DateField(default='1900-01-01')

    def __str__(self):
        return self.nome_coordenador


    class Meta:
        managed = False
        db_table = 'tbl_cordenador'