from .pessoa import Pessoa


class Coordenador(Pessoa):

    def __str__(self):
        return self.nome_coordenador

    def id_coord(self):
        return self.id_coordenador

    class Meta:
        managed = False
        db_table = 'tbl_coordenador'
