<<<<<<< HEAD
# Generated by Django 2.0.4 on 2018-05-01 06:17
=======
# Generated by Django 2.0.3 on 2018-05-01 02:30
>>>>>>> e79821e6a5b123a4d8d422f142ebcba59fbdeb18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id_curso', models.AutoField(primary_key=True, serialize=False)),
                ('nome_curso', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'db_table': 'tbl_curso',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id_disciplina', models.AutoField(primary_key=True, serialize=False)),
                ('nome_disciplina', models.CharField(max_length=100, unique=True)),
                ('data_disciplina', models.DateField()),
                ('status_disciplina', models.CharField(max_length=15)),
                ('plano_ensino_disciplina', models.CharField(max_length=50)),
                ('carga_horaria_disciplina', models.IntegerField()),
                ('competencias_disciplina', models.CharField(max_length=50)),
                ('habilidades_disciplina', models.CharField(max_length=50)),
                ('ementa_disciplina', models.CharField(max_length=50)),
                ('conteudo_programatico_disciplina', models.CharField(max_length=100)),
                ('bibliografia_basica_disciplina', models.CharField(max_length=100)),
                ('bibliografia_complementar_disciplina', models.CharField(max_length=100)),
                ('percentual_pratico', models.IntegerField()),
                ('percentual_teorico', models.IntegerField()),
            ],
            options={
                'db_table': 'tbl_disciplina',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DisciplinaOfertada',
            fields=[
                ('id_disciplina_ofertada', models.AutoField(primary_key=True, serialize=False)),
                ('dt_inicio_matricula_disciplina_ofertada', models.DateField(blank=True, null=True)),
                ('dt_fim_matricula_disciplina_ofertada', models.DateField(blank=True, null=True)),
                ('id_disciplina_disciplina_ofertada', models.IntegerField()),
                ('id_curso_disciplina_ofertada', models.IntegerField()),
                ('ano_disciplina_ofertada', models.IntegerField()),
                ('semestre_disciplina_ofertada', models.IntegerField()),
                ('turma_disciplina_ofertada', models.CharField(max_length=10)),
                ('metodologia_disciplina_ofertada', models.CharField(blank=True, max_length=50, null=True)),
                ('recursos_disciplina_ofertada', models.CharField(blank=True, max_length=50, null=True)),
                ('criterio_avaliacao_disciplina_ofertada', models.CharField(blank=True, max_length=50, null=True)),
                ('plano_aula_disciplina_ofertada', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'tbl_disciplina_ofertada',
                'managed': False,
            },
        ),
    ]
