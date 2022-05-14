from django.contrib.auth.models import User, Group
from django.db.models import Cliente, Transportadora, FormaPagto, Status, Pedido, Produto, Item_pedido
from rest_framework import viewsets
from amouramour.api.serializers import UserSerializer, GroupSerializer, ClienteSerializer, TransportadoraSerializer, FormaPagtoSerializer, StatusSerializer, PedidoSerializer, ProdutoSerializer, Item_pedidoSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class TransportadoraViewSet(viewsets.ModelViewSet):
    queryset = Transportadora.objects.all()
    serializer_class = TransportadoraSerializer

class FormaPagtoViewSet(viewsets.ModelViewSet):
    queryset = FormaPagto.objects.all()
    serializer_class = FormaPagtoSerializer

class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer     

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class Item_pedidoViewSet(viewsets.ModelViewSet):
    queryset = Item_pedido.objects.all()
    serializer_class = Item_pedidoSerializer               

