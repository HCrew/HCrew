from django.db import models

class Curso(models.Model):
    id_curso = models.AutoField(primary_key=True)
    nome_curso = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'tbl_curso'