class Aluno:
        
    def __init__(self, nome='', email='', ra='', celular='', desconto=0.0, disciplinas=[]):
        self.__nome = nome
        self.__email = email
        self.__ra = ra
        self.__celular = celular
        self.__desconto = desconto
        self.__disciplinas = disciplinas

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

    def getCelular(self):
        return self.__celular

    def setCelular(self, celular):
        self.__celular = celular

    def getDesconto(self):
        return self.__celular

    def setDesconto(self, celular):
        self.__celular = celular

    def getDisciplinas(self):
        return self.__disciplinas

    def adicionaDisciplina(self, disciplina):
        self.__disciplinas.append(disciplina)

    def aumentaDesconto(self, porcentagem):
        self.__desconto += porcentagem

    def diminuiDesconto(self, porcentagem):
        self.__desconto -= porcentagem

    def retornaSobrenome(self):
        return ' '.join(self.__nome.split(' ')[1:])

    def retornaValorMensalidade(self):
        mensalidade = 0
        for i in range(len(self.__disciplinas)):
            mensalidade += self.__disciplinas[i].getMensalidade()
        return mensalidade - (mensalidade*self.__desconto/100)

    def retornaCargaHoraria(self):
        horasTotais = float()
        for disciplina in self.getDisciplinas():
            horasTotais += disciplina.getCargaHoraria()
        return horasTotais
