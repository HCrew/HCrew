from django.db import models

class Professor(models.Model):
    id_professor = models.AutoField(primary_key=True)
    login_professor = models.CharField(unique=True, max_length=50)
    senha_professor = models.CharField(max_length=50)
    nome_professor = models.CharField(max_length=100)
    email_professor = models.CharField(unique=True, max_length=70)
    celular_professor = models.IntegerField(unique=True)
    dt_expiracao_professor = models.DateField(default='1900-01-01')
    apelido_professor = models.CharField(max_length=70)

    def __str__(self):
        return self.nome_professor

    class Meta:
        managed = False
        db_table = 'tbl_professor'