from django.db import models
from .login import Login


class Pessoa(models.Model):

    id = models.AutoField(primary_key=True)
    id_login = models.ForeignKey(Login, models.DO_NOTHING, db_column='id_login')
    nome = models.CharField(max_length=100)
    email = models.CharField(unique=True, max_length=70)
    celular = models.IntegerField(unique=True)
    dt_expiracao = models.DateField(default='1900-01-01')

    def retorna_sobrenome(self):
        return self.nome.split(' ')[-1]

    def retorna_carga_horaria(self):
        return 'Metodo não implementado'

    @property
    def login(self):
        return Login.objects.get(self)

    class Meta:
        abstract = True
