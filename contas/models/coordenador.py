from django.db import models
from .login import Login


class Coordenador(models.Model):
    id_coordenador = models.AutoField(primary_key=True)
    id_login = models.ForeignKey(Login, models.DO_NOTHING, db_column='id_login')
    nome_coordenador = models.CharField(max_length=100)
    email_coordenador = models.CharField(unique=True, max_length=70)
    celular_coordenador = models.IntegerField(unique=True)
    dt_expiracao_coordenador = models.DateField()

    def __str__(self):
        return self.nome_coordenador

    def id_coord(self):
        return self.id_coordenador

    class Meta:
        managed = False
        db_table = 'tbl_coordenador'
