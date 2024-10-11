from django import forms
from .models import Cliente
from .models import Fornecedor
from .models import Funcionario
from .models import OrdemServico, ItemOrdemServico, Produto
from .models import ContaReceber



class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'nome', 'sexo', 'nascimento', 'cpf', 'endereco_rua', 'endereco_bairro',
            'endereco_numero', 'cep', 'telefone_fixo', 'telefone_celular', 'email'
        ]
        widgets = {
            'nascimento': forms.DateInput(attrs={'type': 'date'}),
            'cpf': forms.TextInput(attrs={'placeholder': '999.999.999-99'}),
            'cep': forms.TextInput(attrs={'placeholder': '99999-999'}),
            'telefone_fixo': forms.TextInput(attrs={'placeholder': '(99) 9999-9999'}),
            'telefone_celular': forms.TextInput(attrs={'placeholder': '(99) 99999-9999'}),
        }

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        if not cpf:
            raise forms.ValidationError("O CPF é obrigatório.")
        return cpf

    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        if not nome:
            raise forms.ValidationError("O nome é obrigatório.")
        return nome
  # Ou especifique os campos que deseja incluir


class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = ['nome',
            'cnpj',
            'endereco_rua',
            'endereco_bairro',
            'endereco_numero',
            'cep',
            'telefone_fixo',
            'telefone_celular',
            'email']  # Remova 'data_cadastro'
        widgets = {
            'cnpj': forms.TextInput(attrs={'placeholder': '99.999.999/9999-99'}),
            'telefone_fixo': forms.TextInput(attrs={'placeholder': '(99) 9999-9999'}),
            'telefone_celular': forms.TextInput(attrs={'placeholder': '(99) 99999-9999'}),
        }

    def clean_cnpj(self):
        cnpj = self.cleaned_data.get('cnpj')
        if not cnpj:
            raise forms.ValidationError("CNPJ é obrigatório.")
        return cnpj

    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        if not nome:
            raise forms.ValidationError("Nome é obrigatório.")
        return nome


class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = [
            'nome', 'sexo', 'nascimento', 'cpf', 'endereco_rua', 'endereco_bairro',
            'endereco_numero', 'cep', 'telefone_fixo', 'telefone_celular', 'email',
            'cargo', 'escolaridade'
        ]
        widgets = {
            'nascimento': forms.DateInput(attrs={'type': 'date'}),
            'cpf': forms.TextInput(attrs={'placeholder': '999.999.999-99'}),
            'cep': forms.TextInput(attrs={'placeholder': '99999-999'}),
            'telefone_fixo': forms.TextInput(attrs={'placeholder': '(99) 9999-9999'}),
            'telefone_celular': forms.TextInput(attrs={'placeholder': '(99) 99999-9999'}),
        }

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        if not cpf:
            raise forms.ValidationError("O CPF é obrigatório.")
        return cpf

    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        if not nome:
            raise forms.ValidationError("O nome é obrigatório.")
        return nome

from django import forms
from .models import OrdemServico

class OrdemServicoForm(forms.ModelForm):
    class Meta:
        model = OrdemServico
        fields = ['tecnico', 'cliente', 'descricao_problema', 'valor_total']
        widgets = {
            'descricao_problema': forms.Textarea(attrs={'rows': 3}),
            'valor_total': forms.NumberInput(attrs={'step': '0.01'}),
        }



class ItemOrdemServicoForm(forms.ModelForm):
    class Meta:
        model = ItemOrdemServico
        fields = ['produto', 'quantidade', 'valor_total_item']
        widgets = {
            'quantidade': forms.NumberInput(attrs={'min': '1'}),
        }

    def __init__(self, *args, **kwargs):
        super(ItemOrdemServicoForm, self).__init__(*args, **kwargs)
        # Atualiza o valor total do item com base no preço do produto e na quantidade
        if 'produto' in self.data:
            try:
                produto_id = int(self.data.get('produto'))
                produto = Produto.objects.get(id=produto_id)
                self.fields['valor_total_item'].initial = produto.valor_venda * int(self.data.get('quantidade', 1))
            except (ValueError, TypeError, Produto.DoesNotExist):
                pass

    def clean(self):
        cleaned_data = super().clean()
        produto = cleaned_data.get("produto")
        quantidade = cleaned_data.get("quantidade")
        if produto and quantidade:
            valor_total_item = produto.valor_venda * quantidade
            cleaned_data['valor_total_item'] = valor_total_item
        return cleaned_data

# forms.py


class ContaReceberForm(forms.ModelForm):
    class Meta:
        model = ContaReceber
        fields = ['ordem_servico', 'valor']
