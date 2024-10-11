from django.contrib import admin
from .models import Cliente, Fornecedor, Produto, Funcionario, Cargo, Escolaridade, OrdemServico, ItemOrdemServico, ContaReceber, Empresa

# Modelos básicos
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'telefone_celular', 'email', 'data_cadastro')
    search_fields = ('nome', 'cpf', 'email')
    list_filter = ('sexo', 'data_cadastro')
    ordering = ('nome',)

@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cnpj', 'telefone_fixo', 'email', 'data_cadastro')
    search_fields = ('nome', 'cnpj', 'email')
    ordering = ('nome',)

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'marca', 'valor_venda', 'quantidade_estoque')
    search_fields = ('nome', 'marca')
    list_filter = ('marca',)
    ordering = ('nome',)

# Modelos relacionados a funcionários
@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'cargo', 'escolaridade', 'telefone_celular', 'email')
    search_fields = ('nome', 'cpf', 'cargo__nome')
    list_filter = ('cargo', 'escolaridade')
    ordering = ('nome',)

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    ordering = ('nome',)

@admin.register(Escolaridade)
class EscolaridadeAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    ordering = ('nome',)

# Ordem de Serviço e Itens
class ItemOrdemServicoInline(admin.TabularInline):
    model = ItemOrdemServico
    extra = 1

@admin.register(OrdemServico)
class OrdemServicoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'tecnico', 'data', 'valor_total')
    search_fields = ('cliente__nome', 'tecnico__nome')
    list_filter = ('data', 'tecnico')
    inlines = [ItemOrdemServicoInline]  # Permite adicionar itens diretamente na OS
    ordering = ('-data',)

@admin.register(ContaReceber)
class ContaReceberAdmin(admin.ModelAdmin):
    list_display = ('ordem_servico', 'valor')
    search_fields = ('ordem_servico__cliente__nome',)
    ordering = ('ordem_servico',)

# Empresa
@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cnpj', 'telefone_fixo', 'email', 'data_cadastro')
    search_fields = ('nome', 'cnpj')
    ordering = ('nome',)
