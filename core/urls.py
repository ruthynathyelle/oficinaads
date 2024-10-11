from django.urls import path
from .views import (
    ClienteListView, ClienteCreateView, ClienteEditView, ClienteDetailView,
    FornecedorListView, FornecedorCreateView, FornecedorEditView, FornecedorDetailView,
    FuncionarioListView, FuncionarioCreateView, FuncionarioEditView, FuncionarioDetailView,
    lista_ordens_servico, detalhe_ordem_servico, form_ordem_servico,
    lista_contas_receber, detalhe_conta_receber, nova_conta_receber, editar_conta_receber,
    HomeView
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    # Rotas para Clientes
    path('clientes/', ClienteListView.as_view(), name='clientes_list'),
    path('clientes/novo/', ClienteCreateView.as_view(), name='clientes_create'),
    path('clientes/<int:pk>/editar/', ClienteEditView.as_view(), name='clientes_edit'),
    path('clientes/<int:pk>/', ClienteDetailView.as_view(), name='clientes_detail'),


    # Rotas para Fornecedores
    path('fornecedores/', FornecedorListView.as_view(), name='fornecedores_list'),
    path('fornecedores/novo/', FornecedorCreateView.as_view(), name='fornecedores_create'),
    path('fornecedores/<int:pk>/editar/', FornecedorEditView.as_view(), name='fornecedores_edit'),
    path('fornecedores/<int:pk>/', FornecedorDetailView.as_view(), name='fornecedores_detail'),

    # Rotas para Funcionários
    path('funcionarios/', FuncionarioListView.as_view(), name='funcionarios_list'),
    path('funcionarios/novo/', FuncionarioCreateView.as_view(), name='funcionarios_create'),
    path('funcionarios/<int:pk>/editar/', FuncionarioEditView.as_view(), name='funcionarios_edit'),
    path('funcionarios/<int:pk>/', FuncionarioDetailView.as_view(), name='funcionarios_detail'),

    # Rotas para Ordens de Serviço
    path('ordens_servico/', lista_ordens_servico, name='ordem_servico_lista'),
    path('ordens_servico/<int:ordem_id>/', detalhe_ordem_servico, name='ordem_servico_detail'),
    path('ordens_servico/novo/', form_ordem_servico, name='ordem_servico_create'),
    path('ordens_servico/<int:ordem_id>/editar/', form_ordem_servico, name='ordem_servico_edit'),

    # Rotas para Contas a Receber
    path('contas_receber/', lista_contas_receber, name='conta_receber_lista'),
    path('contas_receber/<int:pk>/', detalhe_conta_receber, name='conta_receber_detail'),
    path('contas_receber/novo/', nova_conta_receber, name='conta_receber_create'),
    path('contas_receber/<int:pk>/editar/', editar_conta_receber, name='conta_receber_edit'),
]
