from django.shortcuts import render

# Create your views here.

from .models import Fornecedor
from .forms import FornecedorForm
from .models import Funcionario
from .forms import FuncionarioForm
from django.forms import modelformset_factory
from .models import OrdemServico, ItemOrdemServico
from .forms import OrdemServicoForm, ItemOrdemServicoForm
from .models import ContaReceber
from .forms import ContaReceberForm
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from .forms import ClienteForm  # Certifique-se de que você tenha um form para o Cliente

from django.shortcuts import render

class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')
class ClienteListView(View):
    def get(self, request):
        clientes = Cliente.objects.all()
        return render(request, 'clientes/clientes_list.html', {'clientes': clientes})

class ClienteCreateView(View):
    def get(self, request):
        form = ClienteForm()
        return render(request, 'clientes/clientes_create.html', {'form': form})

    def post(self, request):
        # Coleta os dados do formulário
        nome = request.POST.get('nome')
        sexo = request.POST.get('sexo')
        nascimento = request.POST.get('nascimento')
        cpf = request.POST.get('cpf')
        endereco_rua = request.POST.get('endereco_rua')
        endereco_bairro = request.POST.get('endereco_bairro')
        endereco_numero = request.POST.get('endereco_numero')
        cep = request.POST.get('cep')
        telefone_fixo = request.POST.get('telefone_fixo')
        telefone_celular = request.POST.get('telefone_celular')
        email = request.POST.get('email')

        # Cria uma nova instância do Cliente
        cliente = Cliente(
            nome=nome,
            sexo=sexo,
            nascimento=nascimento,
            cpf=cpf,
            endereco_rua=endereco_rua,
            endereco_bairro=endereco_bairro,
            endereco_numero=endereco_numero,
            cep=cep,
            telefone_fixo=telefone_fixo,
            telefone_celular=telefone_celular,
            email=email
        )
        cliente.save()  # Salva o cliente no banco de dados
        return redirect('clientes_list')  # Redireciona para a lista de clientes

class ClienteEditView(View):
    def get(self, request, pk):
        cliente = get_object_or_404(Cliente, pk=pk)
        form = ClienteForm(instance=cliente)
        return render(request, 'clientes/clientes_edit.html', {'form': form})

    def post(self, request, pk):
        cliente = get_object_or_404(Cliente, pk=pk)
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('clientes_list')
        return render(request, 'clientes/clientes_edit.html', {'form': form})

class ClienteDetailView(View):
    def get(self, request, pk):
        cliente = get_object_or_404(Cliente, pk=pk)
        return render(request, 'clientes/clientes_detail.html', {'cliente': cliente})


 # Certifique-se de ter um form para Fornecedor

class FornecedorListView(View):
    def get(self, request):
        fornecedores = Fornecedor.objects.all()
        return render(request, 'fornecedores/fornecedores_list.html', {'fornecedores': fornecedores})

class FornecedorCreateView(View):
    def get(self, request):
        form = FornecedorForm()
        return render(request, 'fornecedores/fornecedores_create.html', {'form': form})

    def post(self, request):
        form = FornecedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fornecedores_list')
        return render(request, 'fornecedores/fornecedores_create.html', {'form': form})

class FornecedorEditView(View):
    def get(self, request, pk):
        fornecedor = get_object_or_404(Fornecedor, pk=pk)
        form = FornecedorForm(instance=fornecedor)
        return render(request, 'fornecedores/fornecedores_edit.html', {'form': form})

    def post(self, request, pk):
        fornecedor = get_object_or_404(Fornecedor, pk=pk)
        form = FornecedorForm(request.POST, instance=fornecedor)
        if form.is_valid():
            form.save()
            return redirect('fornecedores_list')
        return render(request, 'fornecedores/fornecedores_edit.html', {'form': form})

class FornecedorDetailView(View):
    def get(self, request, pk):
        fornecedor = get_object_or_404(Fornecedor, pk=pk)
        return render(request, 'fornecedores/clientes_detail.html', {'fornecedor': fornecedor})

# core/views.py
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from .models import Cliente

class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'clientes/cliente_confirm_delete.html'
    success_url = reverse_lazy('clientes_list')

  # Certifique-se de ter um form para Funcionário

class FuncionarioListView(View):
    def get(self, request):
        funcionarios = Funcionario.objects.all()
        return render(request, 'funcionarios/funcionarios_list.html', {'funcionarios': funcionarios})

class FuncionarioCreateView(View):
    def get(self, request):
        form = FuncionarioForm()
        return render(request, 'funcionarios/funcionarios_create.html', {'form': form})

    def post(self, request):
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('funcionarios_list')
        return render(request, 'funcionarios/funcionarios_create.html', {'form': form})

class FuncionarioEditView(View):
    def get(self, request, pk):
        funcionario = get_object_or_404(Funcionario, pk=pk)
        form = FuncionarioForm(instance=funcionario)
        return render(request, 'funcionarios/funcionarios_create.html', {'form': form})

    def post(self, request, pk):
        funcionario = get_object_or_404(Funcionario, pk=pk)
        form = FuncionarioForm(request.POST, instance=funcionario)
        if form.is_valid():
            form.save()
            return redirect('funcionarios_list')
        return render(request, 'funcionarios/funcionarios_create.html', {'form': form})

class FuncionarioDetailView(View):
    def get(self, request, pk):
        funcionario = get_object_or_404(Funcionario, pk=pk)
        return render(request, 'funcionarios/funcionarios_detail.html', {'funcionario': funcionario})





# Listar Ordens de Serviço
def lista_ordens_servico(request):
    ordens = OrdemServico.objects.all()
    return render(request, 'ordens_servico/ordem_servico_lista.html', {'ordens': ordens})


# Detalhes de uma Ordem de Serviço
def detalhe_ordem_servico(request, ordem_id):
    ordem = get_object_or_404(OrdemServico, id=ordem_id)
    return render(request, 'ordens_servico/ordem_servico_detail.html', {'ordem': ordem})


# Criar ou Editar Ordem de Serviço
def form_ordem_servico(request, ordem_id=None):
    if ordem_id:
        ordem = get_object_or_404(OrdemServico, id=ordem_id)
    else:
        ordem = OrdemServico()

    ItemFormSet = modelformset_factory(ItemOrdemServico, form=ItemOrdemServicoForm, extra=1, can_delete=True, min_num=1)

    if request.method == 'POST':
        form = OrdemServicoForm(request.POST, instance=ordem)
        formset = ItemFormSet(request.POST, queryset=ordem.itens.all())

        if form.is_valid() and formset.is_valid():
            ordem = form.save()
            itens = formset.save(commit=False)

            for item in itens:
                item.ordem_servico = ordem
                item.save()

            formset.save_m2m()
            return redirect('ordem_servico_lista')
    else:
        form = OrdemServicoForm(instance=ordem)
        formset = ItemFormSet(queryset=ordem.itens.all())

    return render(request, 'ordens_servico/ordem_servico_create.html', {
        'form': form,
        'item_forms': formset,
        'ordem': ordem,
    })
# views.py



# Lista de Contas a Receber
def lista_contas_receber(request):
    contas = ContaReceber.objects.all()
    return render(request, 'contas_receber/conta_receber_lista.html', {'contas': contas})

# Detalhes da Conta a Receber
def detalhe_conta_receber(request, pk):
    conta = get_object_or_404(ContaReceber, pk=pk)
    return render(request, 'contas_receber/conta_receber_detail.html', {'conta': conta})

# Adicionar Nova Conta a Receber
def nova_conta_receber(request):
    if request.method == 'POST':
        form = ContaReceberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('conta_receber_lista')
    else:
        form = ContaReceberForm()
    return render(request, 'contas_receber/conta_receber_create.html', {'form': form})

# Editar Conta a Receber
def editar_conta_receber(request, pk):
    conta = get_object_or_404(ContaReceber, pk=pk)
    if request.method == 'POST':
        form = ContaReceberForm(request.POST, instance=conta)
        if form.is_valid():
            form.save()
            return redirect('conta_receber_lista')
    else:
        form = ContaReceberForm(instance=conta)
    return render(request, 'contas_receber/conta_receber_edit.html', {'form': form})
