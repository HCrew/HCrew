from django.shortcuts import render

def index(request):
    context = {
        "titulo": "Faculdade Impacta de Tecnologia"
    }
    return render(request, 'index.html', context)

def sobre(request):
    context = {
        "titulo": "Sobre nós"
    }
    return render(request, 'sobre.html', context)

def cursos(request):
    context = {
        "titulo": "Nossos cursos",
        "cursos": ['Análise e Desenvolvimento de Sistemas', 'Administração', 'Gestão de Tecnologia da Informação', 'Jogos Digitais', 'Redes de Computadores', 'Banco de Dados'],
        "siglas": ['ads', 'adm', 'gti', 'jd', 'rc', 'bd'],
        "descricao": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    }
    return render(request, 'cursos.html', context)

def contato(request):
    context = {
        "titulo": "Contato"
    }
    return render(request, 'contato.html', context)

def login(request):
    context = {
        "titulo": "Área restrita"
    }
    return render(request, 'login.html', context)

def disciplinaADS(request):
    context = {
        "titulo": "Análise e Desenvolvimento de Sistemas"
    }
    return render(request, 'disciplinaADS.html', context)

def novaDisciplina(request):
    context = {
        "titulo": "Nova disciplina"
    }
    return render(request, 'novaDisciplina.html', context)

def novoAluno(request):
    context = {
        "titulo": "Novo aluno"
    }
    return render(request, 'novoAluno.html', context)

def novoCurso(request):
    context = {
        "titulo": "Novo curso"
    }
    return render(request, 'novoCurso.html', context)

def matricula(request):
    context = {
        "titulo": "Matricula"
    }
    return render(request, 'matricula.html', context)

def ads(request):
    context = {
        "titulo": "Análise e Desenvolvimento de Sistemas",
        "sobre": "Entender as necessidades das empresas é fundamental para fazê-las crescer e gerar bons resultados. Desta maneira, um dos caminhos para alavancar os negócios e se destacar no mercado de trabalho é o da Tecnologia. Para isso, a Faculdade Impacta oferece a graduação em Análise e Desenvolvimento de Sistemas, que prepara você para atuar em todas as etapas de projetos de tecnologia da informação - concepção, gerência e manutenção, aplicação e mensuração de resultados. O curso é voltado para a criação de programas, softwares e sistemas para as empresas. As etapas do projeto de sistemas de software, como análise, projeto, teste, gestão, implantação e manutenção de sistemas de informação também estão entre os aprendizados da graduação."
    }
    return render(request, 'detalhesCurso.html', context)

def adm(request):
    context = {
        "titulo": "Administração",
        "sobre": "Tornar-se um líder. Ser um empreendedor. Fazer investimentos. Você tem inúmeras possibilidades na graduação em Administração da Faculdade Impacta. O curso é voltado para as exigências do mercado de trabalho atual e aborda de forma ampla o universo corporativo. Você vai aprender a definir as melhores estratégias para o bom funcionamento das empresas, para gerar lucros, controlar gastos e se destacar com qualidade entre as concorrentes. Gerir equipes, negociar com fornecedores, solucionar diferentes problemas, atingir resultados positivos, aumentar a produtividade e aplicar novas tecnologias nas organizações também são funções do administrador. Ao final do 2.º ano, os alunos já terão o diploma de Tecnólogo em Processos Gerenciais."
    }
    return render(request, 'detalhesCurso.html', context)