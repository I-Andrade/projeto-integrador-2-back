from django.db import models

# Create your models here.

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    tipo = models.IntegerField()
    nome = models.CharField(max_length=254)
    cpf_cnpj = models.CharField(max_length=14)
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=14)
    email = models.CharField(max_length=254)
    cep = models.CharField(max_length=8)
    logradouro = models.CharField(max_length=60)
    bairro = models.CharField(max_length=60)
    complemento = models.CharField(max_length=200)
    cidade = models.CharField(max_length=60)
    uf = models.CharField(max_length=50)
    observacoes = models.TextField(max_length=200)
    ativo = models.BooleanField(default=True)

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
    data_pedido = models.DateField()
    data_entrega = models.DateField()
    obs = models.TextField(max_length=255)  
    status = models.CharField(max_length=10)
    valor_total_bruto = models.FloatField(max_length=10) 
    valor_frete = models.FloatField(max_length=10) 
    desconto = models.FloatField(max_length=10)
    valor_total_liquido = models.FloatField(max_length=10)
    transportadora_id = models.ForeignKey(Transportadora, on_delete=models.CASCADE)
    forma_pagto_id = models.ForeignKey(FormaPagto, on_delete=models.CASCADE)
    status_id = models.ForeignKey(Status, on_delete=models.CASCADE)

class Produto(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=100)
    tamanho = models.CharField(max_length=50)
    cor = models.CharField(max_length=50)
    valor_custo = models.FloatField(max_length=10)
    valor_venda = models.FloatField(max_length=10)
    obs = models.TextField(max_length=255)

class Item_pedido(models.Model):
    id = models.AutoField(primary_key=True)
    valor_custo = models.FloatField(max_length=10)
    valor_venda = models.FloatField(max_length=10)
    quantidade = models.IntegerField()
    nome_crianca = models.CharField(max_length=100)   
    dt_nasc_crianca = models.DateField()
    medidas = models.CharField(max_length=200)
    sexo = models.CharField(max_length=12) 

