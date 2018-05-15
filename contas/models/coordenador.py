from .pessoa import Pessoa


class Coordenador(Pessoa):

    def __str__(self):
        return self.nome

    def id_coord(self):
        return self.id

    class Meta:
        managed = False
        db_table = 'tbl_cordenador'
