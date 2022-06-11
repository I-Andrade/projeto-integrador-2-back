from django.contrib.auth.models import User, Group
from rest_framework.serializers import ModelSerializer,SerializerMethodField
from amouramour.api.models import Cliente, FormaPagto, Pedido, Produto, Status, Transportadora, Item_pedido

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'groups']

class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']

class TransportadoraSerializer(ModelSerializer):
    class Meta:
        model = Transportadora
        fields = '__all__' 

class FormaPagtoSerializer(ModelSerializer):
    class Meta:
        model = FormaPagto
        fields = '__all__'

class StatusSerializer(ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'

class ProdutoSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'

class PedidoSerializer(ModelSerializer):
    produtos = ProdutoSerializer(many=True, read_only=True)
    nome_cliente = SerializerMethodField()

    def get_nome_cliente(self, obj): 
        return obj.cliente_id.nome

    class Meta:
        model = Pedido
        fields = '__all__'

class ClienteSerializer(ModelSerializer):
    pedidos = PedidoSerializer(many=True, read_only=True)

    class Meta:
        model = Cliente
        fields = '__all__'

class Item_pedidoSerializer(ModelSerializer):
    class Meta:
        model = Item_pedido
        fields = '__all__'