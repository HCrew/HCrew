from django.db import models


class Pessoa(models.Model):

    id = models.AutoField(primary_key=True)
    login = models.CharField(unique=True, max_length=50)
    senha = models.CharField(max_length=70)
    nome = models.CharField(max_length=100)
    email = models.CharField(unique=True, max_length=70)
    celular = models.IntegerField(unique=True)
    dt_expiracao = models.DateField()

    def retorna_sobrenome(self):
        return self.nome.split(' ')[-1]

    def retorna_carga_horaria(self):
        return 'Metodo não implementado'

    class Meta:
        abstract = True