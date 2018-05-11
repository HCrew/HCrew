from django.db import models


class Login(models.Model):
    id = models.AutoField(primary_key=True)
    login = models.CharField(unique=True, max_length=50, blank=True, null=True)
    senha = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_login'
