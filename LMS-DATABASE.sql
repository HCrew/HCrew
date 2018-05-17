-- ****************************************************************
-- ******CRIAR UMA BANCO DE DADOS COM O NOME "lmsImpacta"******
-- ****************************************************************

DROP DATABASE IF EXISTS lmsimpacta;
CREATE DATABASE lmsimpacta;

\c lmsimpacta;

CREATE TABLE IF NOT EXISTS public.tbl_login
(
   id serial,
   login character varying(50),
   senha character varying(50),
   CONSTRAINT pk_id_login PRIMARY KEY (id),
   CONSTRAINT unique_login UNIQUE (login)
);


CREATE TABLE IF NOT EXISTS public.tbl_coordenador
(
   id serial,
   id_login integer NOT NULL,
   nome character varying(100) NOT NULL,
   email character varying(70) NOT NULL,
   celular integer NOT NULL,
   dt_expiracao date NOT NULL DEFAULT '01/01/1900',
   CONSTRAINT pk_id_coordenador PRIMARY KEY (id),
   CONSTRAINT unique_column_email_coordenador UNIQUE (email),
   CONSTRAINT unique_column_celular_coordenador UNIQUE (celular),
   CONSTRAINT fk_login_coordenador FOREIGN KEY (id_login) REFERENCES tbl_login (id)
);


CREATE TABLE IF NOT EXISTS public.tbl_aluno
(
   id serial,
   id_login integer NOT NULL,
   nome character varying(100) NOT NULL,
   email character varying(70) NOT NULL,
   celular integer NOT NULL,
   dt_expiracao date NOT NULL DEFAULT '01/01/1900',
   ra_aluno integer NOT NULL,
   foto_aluno character varying(100),
   CONSTRAINT pk_id_aluno PRIMARY KEY (id),
   CONSTRAINT unique_column_email_aluno UNIQUE (email),
   CONSTRAINT unique_column_celular_aluno UNIQUE (celular),
   CONSTRAINT unique_column_ra_aluno UNIQUE (ra_aluno),
   CONSTRAINT fk_login_aluno FOREIGN KEY (id_login) REFERENCES tbl_login (id)
);


CREATE TABLE IF NOT EXISTS public.tbl_professor
(
   id serial,
   id_login integer NOT NULL,
   nome character varying(100) NOT NULL,
   email character varying(70) NOT NULL,
   celular integer NOT NULL,
   dt_expiracao date NOT NULL DEFAULT '01/01/1900',
   apelido_professor character varying(70) NOT NULL,
   CONSTRAINT pk_id_professor PRIMARY KEY (id),
   CONSTRAINT unique_column_email_professor UNIQUE (email),
   CONSTRAINT unique_column_celular_professor UNIQUE (celular),
   CONSTRAINT fk_login_professor FOREIGN KEY (id_login) REFERENCES tbl_login (id)
);


CREATE TABLE IF NOT EXISTS public.tbl_disciplina
(
   id_disciplina serial,
   nome_disciplina character varying(100) NOT NULL,
   data_disciplina date NOT NULL DEFAULT current_timestamp,
   status_disciplina character varying(15) NOT NULL DEFAULT 'Aberta',
   plano_ensino_disciplina character varying(50) NOT NULL,
   carga_horaria_disciplina integer NOT NULL,
   competencias_disciplina character varying(50) NOT NULL,
   habilidades_disciplina character varying(50) NOT NULL,
   ementa_disciplina character varying(50) NOT NULL,
   conteudo_programatico_disciplina character varying(100) NOT NULL,
   bibliografia_basica_disciplina character varying(100) NOT NULL,
   bibliografia_complementar_disciplina character varying(100) NOT NULL,
   percentual_pratico integer NOT NULL,
   percentual_teorico integer NOT NULL,
   id_coordenador_disciplina integer NOT NULL,
   CONSTRAINT pk_id_disciplina PRIMARY KEY (id_disciplina),
   CONSTRAINT unique_column_nome_disciplina UNIQUE (nome_disciplina),
   CONSTRAINT fk_id_coordenador FOREIGN KEY (id_coordenador_disciplina) REFERENCES tbl_coordenador (id)
);


CREATE TABLE IF NOT EXISTS public.tbl_curso
(
   id_curso serial,
   nome_curso character varying(100) NOT NULL,
   CONSTRAINT pk_id_curso PRIMARY KEY (id_curso),
   CONSTRAINT unique_column_curso UNIQUE (nome_curso)
);


CREATE TABLE IF NOT EXISTS public.tbl_disciplina_ofertada
(
   id_disciplina_ofertada serial,
   id_coordenador_disciplina_ofertada integer NOT NULL,
   dt_inicio_matricula_disciplina_ofertada date,
   dt_fim_matricula_disciplina_ofertada date,
   id_disciplina_disciplina_ofertada integer NOT NULL,
   id_curso_disciplina_ofertada integer NOT NULL,
   ano_disciplina_ofertada integer NOT NULL,
   semestre_disciplina_ofertada integer NOT NULL,
   turma_disciplina_ofertada character varying(10) NOT NULL,
   id_professor_disciplina_ofertada integer,
   metodologia_disciplina_ofertada character varying(50),
   recursos_disciplina_ofertada character varying(50),
   criterio_avaliacao_disciplina_ofertada character varying(50),
   plano_aula_disciplina_ofertada character varying(50),
   CONSTRAINT pk_id_disciplina_ofertada PRIMARY KEY (id_disciplina_ofertada),
   CONSTRAINT unique_columns_disciplina_ofertada UNIQUE (id_disciplina_disciplina_ofertada, id_curso_disciplina_ofertada, ano_disciplina_ofertada, semestre_disciplina_ofertada, turma_disciplina_ofertada),
   CONSTRAINT fk_id_coordenador FOREIGN KEY (id_coordenador_disciplina_ofertada) REFERENCES tbl_coordenador (id),
   CONSTRAINT fk_id_professor FOREIGN KEY (id_professor_disciplina_ofertada) REFERENCES tbl_professor (id)
);


CREATE TABLE IF NOT EXISTS public.tbl_solicitacao_matricula
(
   id_solicitacao_matricula serial,
   id_aluno_solicitacao_matricula integer NOT NULL,
   id_disciplina_ofertada_solicitacao_matricula integer NOT NULL,
   dt_solicitacao_solicitacao_matricula date NOT NULL,
   id_coordenador_solicitacao_matricula integer,
   status_solicitacao_matricula character varying(20) DEFAULT 'Solicitada',
   CONSTRAINT pk_id_solicitacao_matricula PRIMARY KEY (id_solicitacao_matricula),
   CONSTRAINT fk_id_coordenador_solicitacao_matricula FOREIGN KEY (id_coordenador_solicitacao_matricula) REFERENCES tbl_coordenador (id),
   CONSTRAINT fk_id_aluno_solicitacao_matricula FOREIGN KEY (id_aluno_solicitacao_matricula) REFERENCES tbl_aluno (id)
);


CREATE TABLE IF NOT EXISTS public.tbl_atividade
(
   id_atividade serial,
   titulo_atividade character varying(70) NOT NULL,
   descricao_atividade character varying(100),
   conteudo_atividade character varying(80) NOT NULL,
   tipo_atividade character varying(30) NOT NULL,
   extras_atividade character varying(30),
   id_professor_atividade integer NOT NULL,
   CONSTRAINT pk_id_atividade PRIMARY KEY (id_atividade),
   CONSTRAINT fk_id_professor_atividade FOREIGN KEY (id_professor_atividade) REFERENCES tbl_professor (id),
   CONSTRAINT unique_column_titulo_atividade UNIQUE (titulo_atividade)
);


CREATE TABLE IF NOT EXISTS public.tbl_atividade_vinculada
(
   id_atividade_vinculada serial,
   id_atividade_atividade_vinculada integer NOT NULL,
   id_professor_atividade_vinculada integer NOT NULL,
   id_disciplina_ofertada_atividade_vinculada integer NOT NULL,
   rotulo_atividade_vinculada character varying(50) NOT NULL,
   status_atividade_vinculada character varying(30) NOT NULL,
   dt_inicio_respostas date NOT NULL,
   dt_fim_respostas date NOT NULL,
   CONSTRAINT pk_id_atividade_vinculada PRIMARY KEY (id_atividade_vinculada),
   CONSTRAINT fk_id_atividade_atividade_vinculada FOREIGN KEY (id_atividade_atividade_vinculada) REFERENCES tbl_atividade (id_atividade),
   CONSTRAINT fk_id_professor_atividade_vinculada FOREIGN KEY (id_professor_atividade_vinculada) REFERENCES tbl_professor (id),
   CONSTRAINT fk_id_disciplina_ofertada_atividade_vinculada FOREIGN KEY (id_disciplina_ofertada_atividade_vinculada) REFERENCES tbl_disciplina_ofertada (id_disciplina_ofertada)
);


CREATE TABLE IF NOT EXISTS public.tbl_entrega
(
   id_entrega serial,
   id_aluno_entrega integer NOT NULL,
   id_atividade_vinculada_entrega integer NOT NULL,
   titulo_entrega character varying(50) NOT NULL,
   resposta_entrega character varying(50) NOT NULL,
   dt_entrega_entrega date NOT NULL DEFAULT current_timestamp,
   status_entrega character varying(30) NOT NULL,
   id_professor_entrega integer,
   nota_entrega integer,
   dt_avaliacao_entrega date,
   obs_entrega character varying(100),
   CONSTRAINT pk_id_entrega PRIMARY KEY (id_entrega),
   CONSTRAINT fk_id_aluno_entrega FOREIGN KEY (id_aluno_entrega) REFERENCES tbl_aluno (id),
   CONSTRAINT fk_id_atividade_vinculada_entrega FOREIGN KEY (id_atividade_vinculada_entrega) REFERENCES tbl_atividade_vinculada (id_atividade_vinculada),
   CONSTRAINT fk_id_professor_entrega FOREIGN KEY (id_professor_entrega) REFERENCES tbl_professor (id),
   CONSTRAINT unique_columns_entrega UNIQUE (id_aluno_entrega, id_atividade_vinculada_entrega)
);



CREATE TABLE IF NOT EXISTS public.tbl_mensagem
(
   id_mensagem serial,
   id_aluno_mensagem integer NOT NULL,
   id_professor_mensagem integer NOT NULL,
   assunto_mensagem character varying(50) NOT NULL,
   referencia_mensagem character varying(50) NOT NULL,
   conteudo_mensagem character varying(60) NOT NULL,
   status_mensagem character varying(30) NOT NULL,
   dt_envio_mensagem date NOT NULL,
   dt_resposta_mensagem date,
   resposta_mensagem character varying(50),
   CONSTRAINT pk_id_mensagem_mensagem PRIMARY KEY (id_mensagem),
   CONSTRAINT fk_id_aluno_mensagem FOREIGN KEY (id_aluno_mensagem) REFERENCES tbl_aluno (id),
   CONSTRAINT fk_id_professor FOREIGN KEY (id_professor_mensagem) REFERENCES tbl_professor (id)
);

INSERT INTO tbl_login(login, senha) VALUES
('aluno', 'aluno'),
('professor', 'professor'),
('coordenador', 'coordenador');

INSERT INTO tbl_coordenador(id_login, nome, email, celular) VALUES
(3, 'Coordenador João', 'coordenador@impacta.com.br', 123456789);

INSERT INTO tbl_aluno(id_login, nome, email, celular, ra_aluno, foto_aluno) VALUES
(1, 'Aluno Jack', 'aluno@impacta.com.br', 987654321, 1800123, '');

INSERT INTO tbl_professor(id_login, nome, email, celular, apelido_professor) VALUES
(2, 'Professor Cazé', 'professor@impacta.com.br', 567891234, 'Chupa-cabra');