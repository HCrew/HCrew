class Disciplina:

    def __init__(self, nome="", cargaHoraria=0, mensalidade=0.0, professor=None):
        self.__nome = nome
        self.__cargaHoraria = cargaHoraria
        self.__mensalidade = mensalidade
        self.__professor = professor

    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome

    def getCargaHoraria(self):
        return self.__cargaHoraria

    def setCargaHoraria(self, cargaHoraria):
        self.__cargaHoraria = cargaHoraria
    
    def getMensalidade(self):
        return self.__mensalidade

    def setMensalidade(self, mensalidade):
        self.__mensalidade = mensalidade

    def getProfessor(self):
        return self.__professor

    def setProfessor(self, professor):
        self.__professor = professor

    def retornaValorHora(self):
        valor = (self.__mensalidade*6)/self.__cargaHoraria
        return valor
