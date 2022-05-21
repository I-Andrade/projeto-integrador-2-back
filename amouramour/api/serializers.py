from django.contrib.auth.models import User, Group
from rest_framework import serializers
from amouramour.api.models import Cliente, FormaPagto, Pedido, Produto, Status, Transportadora, Item_pedido

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class TransportadoraSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transportadora
        fields = '__all__'

class FormaPagtoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FormaPagto
        fields = '__all__'

class StatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'

class PedidoSerializer(serializers.HyperlinkedModelSerializer):
    #cliente = ClienteSerializer(many=False, read_only=True)

    class Meta:
        model = Pedido
        #fields = ['cliente_id','cliente']
        fields = '__all__'

class ProdutoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'

class Item_pedidoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item_pedido
        fields = '__all__'        

