from django.utils.timezone import now
from django.db import models
from .aluno import Aluno
from .professor import Professor


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
        return '{self.id_aluno_mensagem} : {self.id_professor_mensagem}'.format(self=self)

    class Meta:
        managed = False
        db_table = 'tbl_mensagem'
