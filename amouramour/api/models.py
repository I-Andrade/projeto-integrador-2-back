from django.db import models

# Create your models here.

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    tipo = models.IntegerField()
    nome = models.CharField(max_length=254)
    cpf_cnpj = models.CharField(max_length=14)
    data_nascimento = models.DateField(null=True)
    telefone = models.CharField(max_length=14, null=True)
    email = models.CharField(max_length=254, null=True)
    cep = models.CharField(max_length=8, null=True)
    logradouro = models.CharField(max_length=60, null=True)
    numero = models.CharField(max_length=10, null=True)
    bairro = models.CharField(max_length=60, null=True)
    complemento = models.CharField(max_length=200, null=True)
    cidade = models.CharField(max_length=60, null=True)
    uf = models.CharField(max_length=50, null=True)
    observacoes = models.TextField(max_length=200, null=True)
    ativo = models.BooleanField(default=True, null=True)

class Transportadora(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=254)

class FormaPagto(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=60)   
    parcelas = models.IntegerField()

class Status(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=60) 

class Pedido(models.Model):
    id = models.AutoField(primary_key=True)
    cliente_id = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_pedido = models.DateField(auto_now_add=True)
    data_entrega = models.DateField()
    obs = models.TextField(max_length=255, null=True)  
    status = models.CharField(max_length=10)
    valor_total_bruto = models.FloatField(max_length=10) 
    valor_frete = models.FloatField(max_length=10, null=True) 
    desconto = models.FloatField(max_length=10, null=True)
    valor_total_liquido = models.FloatField(max_length=10)
    transportadora_id = models.ForeignKey(Transportadora, on_delete=models.CASCADE)
    forma_pagto_id = models.ForeignKey(FormaPagto, on_delete=models.CASCADE)
    status_id = models.ForeignKey(Status, on_delete=models.CASCADE)

class Produto(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=100)
    tamanho = models.CharField(default="Único", max_length=50, null=True)
    cor = models.CharField(max_length=50)
    valor_custo = models.FloatField(max_length=10)
    valor_venda = models.FloatField(max_length=10)
    obs = models.TextField(max_length=255, null=True)

class Item_pedido(models.Model):
    id = models.AutoField(primary_key=True)
    valor_custo = models.FloatField(max_length=10)
    valor_venda = models.FloatField(max_length=10)
    quantidade = models.IntegerField(null=True)
    nome_crianca = models.CharField(max_length=100)   
    dt_nasc_crianca = models.DateField(null=True)
    medidas = models.CharField(max_length=200, null=True)
    sexo = models.CharField(max_length=12, null=True) 

