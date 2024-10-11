from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    sexo = models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Feminino')])
    nascimento = models.DateField(null=True, blank=True)
    cpf = models.CharField(max_length=14, unique=True)
    endereco_rua = models.CharField(max_length=100)
    endereco_bairro = models.CharField(max_length=100)
    endereco_numero = models.CharField(max_length=10)
    cep = models.CharField(max_length=9)
    data_cadastro = models.DateField(auto_now_add=True)
    telefone_fixo = models.CharField(max_length=15)
    telefone_celular = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.nome

class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18, unique=True)
    endereco_rua = models.CharField(max_length=100)
    endereco_bairro = models.CharField(max_length=100)
    endereco_numero = models.CharField(max_length=10)
    cep = models.CharField(max_length=9)
    data_cadastro = models.DateField(auto_now_add=True)
    telefone_fixo = models.CharField(max_length=15)
    telefone_celular = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.nome


class Cargo(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Escolaridade(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    sexo = models.CharField(max_length=10, choices=[('M', 'Masculino'), ('F', 'Feminino')])
    nascimento = models.DateField(null=True, blank=True)
    cpf = models.CharField(max_length=14, unique=True)
    endereco_rua = models.CharField(max_length=100)
    endereco_bairro = models.CharField(max_length=100)
    endereco_numero = models.CharField(max_length=10)
    cep = models.CharField(max_length=9)
    data_cadastro = models.DateField(auto_now_add=True)
    telefone_fixo = models.CharField(max_length=15, null=True, blank=True)
    telefone_celular = models.CharField(max_length=15)
    email = models.EmailField()
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    escolaridade = models.ForeignKey(Escolaridade, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    valor_venda = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade_estoque = models.PositiveIntegerField()
    marca = models.CharField(max_length=50)  # Para mais detalhes, pode ser ForeignKey para outro modelo de Marca

    def __str__(self):
        return self.nome


class OrdemServico(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tecnico = models.ForeignKey(Funcionario, on_delete=models.CASCADE, limit_choices_to={'cargo__nome': 'Técnico'})  # Filtrando para técnicos
    descricao_problema = models.TextField()
    data = models.DateField(auto_now_add=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"OS: {self.id} - Cliente: {self.cliente.nome}"


class ItemOrdemServico(models.Model):
    ordem_servico = models.ForeignKey(OrdemServico, on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    valor_total_item = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantidade} x {self.produto.nome} - OS: {self.ordem_servico.id}"

    def save(self, *args, **kwargs):
        if self.produto.quantidade_estoque < self.quantidade:
            raise ValueError("Estoque insuficiente para o produto")
        self.produto.quantidade_estoque -= self.quantidade
        self.produto.save()
        self.valor_total_item = self.quantidade * self.produto.valor_venda
        super().save(*args, **kwargs)


class ContaReceber(models.Model):
    ordem_servico = models.OneToOneField('OrdemServico', on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Conta a Receber - OS: {self.ordem_servico.id} - Valor: R${self.valor}"


class Empresa(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18, unique=True)
    endereco_rua = models.CharField(max_length=100)
    endereco_bairro = models.CharField(max_length=100)
    endereco_numero = models.CharField(max_length=10)
    cep = models.CharField(max_length=9)
    data_cadastro = models.DateField(auto_now_add=True)
    telefone_fixo = models.CharField(max_length=15)
    telefone_celular = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.nome
