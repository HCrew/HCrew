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
        "cursos": [
            {
                "curso": "Análise e Desenvolvimento de Sistemas",
                "url": "/ADS/"
            },
            {
                "curso": "Administração",
                "url": "/ADM/"
            },
            {
                "curso": "Gestão de Tecnologia da Informação",
                "url": ""
            },
            {
                "curso": "Jogos Digitais",
                "url": ""
            },
            {
                "curso": "Redes de Computadores",
                "url": ""
            },
            {
                "curso": "Banco de Dados",
                "url": ""
            }
        ],
        "descricao": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut "
                     "labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco "
                     "laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in "
                     "voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat "
                     "cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
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
        "titulo": "Análise e Desenvolvimento de Sistemas",
        "semestres": [
            {
                "semestre": "1º Semestre",
                "disciplinas": [
                    {
                        "nome": "Lógica de programação",
                        "cargaHoraria": "80"
                    },
                    {
                        "nome": "Matematica aplicada",
                        "cargaHoraria": "80"
                    },
                    {
                        "nome": "Modelagem de banco de dados",
                        "cargaHoraria": "80"
                    },
                    {
                        "nome": "Introdução a Internet das Coisas",
                        "cargaHoraria": "80"
                    },
                    {
                        "nome": "Linguagem de programação 1",
                        "cargaHoraria": "80"
                    }
                ]
            },
            {

                "semestre": "2º Semestre",
                "disciplinas": [
                    {
                        "nome": "Ambiente Desenvolvimento e Operação",
                        "cargaHoraria": "80"
                    },
                    {
                        "nome": "Engenharia de Software",
                        "cargaHoraria": "80"
                    },
                    {
                        "nome": "Tecnologia Web",
                        "cargaHoraria": "80"
                    },
                    {
                        "nome": "Linguagem SQL",
                        "cargaHoraria": "80"
                    },
                    {
                        "nome": "Linguagem de programação 2",
                        "cargaHoraria": "80"
                    }
                ]
            },
            {
                "semestre": "3º Semestre",
                "disciplinas": [
                    {
                        "nome": "Desenvolvimento de Aplicações Distribuidas",
                        "cargaHoraria": "80"
                    },
                    {
                        "nome": "Engenharia de requisitos",
                        "cargaHoraria": "80"
                    },
                    {
                        "nome": "Estrutura de dados",
                        "cargaHoraria": "80"
                    },
                    {
                        "nome": "Interface homem computador",
                        "cargaHoraria": "80"
                    },
                    {
                        "nome": "Oficina de Projeto de Empresa 1",
                        "cargaHoraria": "80"
                    }
                ]
            },
            {
                "semestre": "4º Semestre",
                "disciplinas": [
                    {
                        "nome": "Arquitetura e projetos de sistemas",
                        "cargaHoraria": "80"
                    },
                    {
                        "nome": "Desenvolvimento de Aplicações Distribuídas",
                        "cargaHoraria": "80"
                    },
                    {
                        "nome": "Oficina de Projeto de Empresa 2",
                        "cargaHoraria": "80"
                    },
                    {
                        "nome": "Qualidade de Software",
                        "cargaHoraria": "80"
                    },
                    {
                        "nome": "Redes e Segurança de Sistemas de Informação",
                        "cargaHoraria": "80"
                    }
                ]
            }

        ]
    }
    return render(request, 'disciplinaADS.html', context)


def disciplinaBancoDeDados(request):
    context = {
        "titulo": "Banco de Dados",
        "semestres": [
            {
                "semestre": "1º Semestre",
                "disciplinas": [
                    {
                        "nome": "Fundamentos de banco de dados",
                        "cargaHoraria": "80"
                    },
                    {
                        "nome": "Introdução a internet das coisas",
                        "cargaHoraria": "80"
                    },
                    {
                        "nome": "Linguagem de programação",
                        "cargaHoraria": "80"
                    },
                    {
                        "nome": "Matematica aplicada",
                        "cargaHoraria": "80"
                    },
                    {
                        "nome": "Logica de programação",
                        "cargaHoraria": "80"
                    }
                ]
            },
            {

                "semestre": "2º Semestre",
                "disciplinas": [
                    {
                        "nome": "Análise Exploratória de Dados",
                        "cargaHoraria": "80"
                    },
                    {
                        "nome": "Ambiente de Desenvolvimento e Operação",
                        "cargaHoraria": "80"
                    },
                    {
                        "nome": "Desenvolvimento de Sistemas",
                        "cargaHoraria": "80"
                    },
                    {
                        "nome": "Engenharia de Software",
                        "cargaHoraria": "80"
                    },
                    {
                        "nome": "Linguagem SQL",
                        "cargaHoraria": "80"
                    }
                ]
            },
            {
                "semestre": "3º Semestre",
                "disciplinas": [
                    {
                        "nome": "Developing Database",
                        "cargaHoraria": "80"
                    },
                    {
                        "nome": "Estrutura de Dados",
                        "cargaHoraria": "80"
                    },
                    {
                        "nome": "Business Intelligence",
                        "cargaHoraria": "80"
                    },
                    {
                        "nome": "Data Analytics",
                        "cargaHoraria": "80"
                    },
                    {
                        "nome": "OPE1 - Oficina Projeto Empresa",
                        "cargaHoraria": "80"
                    }
                ]
            },
            {
                "semestre": "4º Semestre",
                "disciplinas": [
                    {
                        "nome": "Administração de Banco de Dados",
                        "cargaHoraria": "80"
                    },
                    {
                        "nome": "Qualidade de Governança de Dados",
                        "cargaHoraria": "80"
                    },
                    {
                        "nome": "Segurança de Banco de Dados: ",
                        "cargaHoraria": "80"
                    },
                    {
                        "nome": "Big Data",
                        "cargaHoraria": "80"
                    },
                    {
                        "nome": "Computação Cognitiva",
                        "cargaHoraria": "80"
                    }
                ]
            }

        ]
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
        "sobre": "Entender as necessidades das empresas é fundamental para fazê-las crescer e gerar bons resultados. "
                 "Desta maneira, um dos caminhos para alavancar os negócios e se destacar no mercado de trabalho é o "
                 "da Tecnologia. Para isso, a Faculdade Impacta oferece a graduação em Análise e Desenvolvimento de "
                 "Sistemas, que prepara você para atuar em todas as etapas de projetos de tecnologia da informação "
                 "- concepção, gerência e manutenção, aplicação e mensuração de resultados. O curso é voltado para a "
                 "criação de programas, softwares e sistemas para as empresas. As etapas do projeto de sistemas de "
                 "software, como análise, projeto, teste, gestão, implantação e manutenção de sistemas de informação "
                 "também estão entre os aprendizados da graduação."
    }
    return render(request, 'detalhesCurso.html', context)


def adm(request):
    context = {
        "titulo": "Administração",
        "sobre":
            "Tornar-se um líder. Ser um empreendedor. Fazer investimentos. Você tem inúmeras possibilidades na "
            "graduação em Administração da Faculdade Impacta. O curso é voltado para as exigências do mercado de "
            "trabalho atual e aborda de forma ampla o universo corporativo. Você vai aprender a definir as melhores "
            "estratégias para o bom funcionamento das empresas, para gerar lucros, controlar gastos e se destacar "
            "com qualidade entre as concorrentes. Gerir equipes, negociar com fornecedores, solucionar diferentes "
            "problemas, atingir resultados positivos, aumentar a produtividade e aplicar novas tecnologias nas "
            "organizações também são funções do administrador. Ao final do 2.º ano, os alunos já terão o diploma "
            "de Tecnólogo em Processos Gerenciais."
    }
    return render(request, 'detalhesCurso.html', context)
