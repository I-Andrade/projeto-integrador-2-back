from django.contrib.auth.models import User, Group
from rest_framework import serializers
from amouramour.api.models import Cliente, FormaPagto, Pedido, Produto, Status, Transportadora, Item_pedido

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'groups']

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class TransportadoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transportadora
        fields = '__all__'

class FormaPagtoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormaPagto
        fields = '__all__'

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'

class PedidoSerializer(serializers.ModelSerializer):
    #cliente = ClienteSerializer(many=False, read_only=True)

    class Meta:
        model = Pedido
        #fields = ['cliente_id','cliente']
        fields = '__all__'

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'

class Item_pedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item_pedido
        fields = '__all__'        

