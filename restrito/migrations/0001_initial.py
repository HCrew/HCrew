

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Atividade',
            fields=[
                ('id_atividade', models.AutoField(primary_key=True, serialize=False)),
                ('titulo_atividade', models.CharField(max_length=70, unique=True)),
                ('descricao_atividade', models.CharField(blank=True, max_length=100, null=True)),
                ('conteudo_atividade', models.CharField(max_length=80)),
                ('tipo_atividade', models.CharField(max_length=30)),
                ('extras_atividade', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'tbl_atividade',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AtividadeVinculada',
            fields=[
                ('id_atividade_vinculada', models.AutoField(primary_key=True, serialize=False)),
                ('rotulo_atividade_vinculada', models.CharField(max_length=50)),
                ('status_atividade_vinculada', models.CharField(max_length=30)),
                ('dt_inicio_respostas', models.DateField()),
                ('dt_fim_respostas', models.DateField()),
            ],
            options={
                'db_table': 'tbl_atividade_vinculada',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Entrega',
            fields=[
                ('id_entrega', models.AutoField(primary_key=True, serialize=False)),
                ('titulo_entrega', models.CharField(max_length=50)),
                ('resposta_entrega', models.CharField(max_length=50)),
                ('dt_entrega_entrega', models.DateField()),
                ('status_entrega', models.CharField(max_length=30)),
                ('nota_entrega', models.IntegerField(blank=True, null=True)),
                ('dt_avaliacao_entrega', models.DateField(blank=True, null=True)),
                ('obs_entrega', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'tbl_entrega',
                'managed': False,
            },
        ),
    ]
