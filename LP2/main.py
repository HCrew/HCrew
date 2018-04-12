from disciplinas import Disciplina
from professores import Professor
from aluno import Aluno

aluno = Aluno("Victor", desconto=50.0)
professor = Professor(nome="Fernando", ra='123456')
disciplina = Disciplina(nome="LP2", cargaHoraria=80, mensalidade=700, professor=professor)

aluno.adicionaDisciplina(disciplina)
print("O valor da mensalidade é: ", aluno.retornaValorMensalidade())

professor.adicionaDisciplina(disciplina)
print("Carga Horária: ", professor.retornaCargaHoraria())

print("Valor/Hora da disciplina: ", disciplina.retornaValorHora())
