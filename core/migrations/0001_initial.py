# Generated by Django 5.1.1 on 2024-10-11 15:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=1)),
                ('nascimento', models.DateField(blank=True, null=True)),
                ('cpf', models.CharField(max_length=14, unique=True)),
                ('endereco_rua', models.CharField(max_length=100)),
                ('endereco_bairro', models.CharField(max_length=100)),
                ('endereco_numero', models.CharField(max_length=10)),
                ('cep', models.CharField(max_length=9)),
                ('data_cadastro', models.DateField(auto_now_add=True)),
                ('telefone_fixo', models.CharField(max_length=15)),
                ('telefone_celular', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cnpj', models.CharField(max_length=18, unique=True)),
                ('endereco_rua', models.CharField(max_length=100)),
                ('endereco_bairro', models.CharField(max_length=100)),
                ('endereco_numero', models.CharField(max_length=10)),
                ('cep', models.CharField(max_length=9)),
                ('data_cadastro', models.DateField(auto_now_add=True)),
                ('telefone_fixo', models.CharField(max_length=15)),
                ('telefone_celular', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Escolaridade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cnpj', models.CharField(max_length=18, unique=True)),
                ('endereco_rua', models.CharField(max_length=100)),
                ('endereco_bairro', models.CharField(max_length=100)),
                ('endereco_numero', models.CharField(max_length=10)),
                ('cep', models.CharField(max_length=9)),
                ('data_cadastro', models.DateField(auto_now_add=True)),
                ('telefone_fixo', models.CharField(max_length=15)),
                ('telefone_celular', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('valor_venda', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantidade_estoque', models.PositiveIntegerField()),
                ('marca', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=10)),
                ('nascimento', models.DateField(blank=True, null=True)),
                ('cpf', models.CharField(max_length=14, unique=True)),
                ('endereco_rua', models.CharField(max_length=100)),
                ('endereco_bairro', models.CharField(max_length=100)),
                ('endereco_numero', models.CharField(max_length=10)),
                ('cep', models.CharField(max_length=9)),
                ('data_cadastro', models.DateField(auto_now_add=True)),
                ('telefone_fixo', models.CharField(blank=True, max_length=15, null=True)),
                ('telefone_celular', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cargo')),
                ('escolaridade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.escolaridade')),
            ],
        ),
        migrations.CreateModel(
            name='OrdemServico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao_problema', models.TextField()),
                ('data', models.DateField(auto_now_add=True)),
                ('valor_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cliente')),
                ('tecnico', models.ForeignKey(limit_choices_to={'cargo__nome': 'Técnico'}, on_delete=django.db.models.deletion.CASCADE, to='core.funcionario')),
            ],
        ),
        migrations.CreateModel(
            name='ContaReceber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ordem_servico', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.ordemservico')),
            ],
        ),
        migrations.CreateModel(
            name='ItemOrdemServico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.PositiveIntegerField()),
                ('valor_total_item', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ordem_servico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itens', to='core.ordemservico')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.produto')),
            ],
        ),
    ]
