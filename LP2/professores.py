class Professor:

    def __init__(self, nome='', email='', ra='', celular=''):
        self.__nome = nome
        self.__email = email
        self.__ra = ra
        self.__celular = celular
        self.__disciplinas = []

    def getNome(self):
        return self.__nome        

    def setNome(self, nome):
        self.__nome = nome

    def getEmail(self):
        return self.__email

    def setEmail(self, email):
        self.__email = email

    def getRA(self):
        return self.__ra

    def setRA(self, cargaHoraria):
        self.__ra = ra

    def getCelular(self):
        return self.__celular

    def setCelular(self, celular):
        self.__celular = celular

    def getDisciplinas(self):
        return self.__disciplinas

    def retornaSobrenome(self):
        return ' '.join(self.__nome.split(' ')[1:])

    def adicionaDisciplina(self, disciplina):
        if disciplina.getProfessor().getRA() == self.__ra:
            self.__disciplinas.append(disciplina)
        else:
            return "Professor não associado a esta disciplina!"

    def retornaCargaHoraria(self):
        somaCarga = 0
        for i in self.__disciplinas:
            somaCarga += i.getCargaHoraria()/20
        return somaCarga
    