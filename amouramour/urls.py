"""amouramour URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from amouramour.api import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

#router = routers.DefaultRouter()
router = routers.SimpleRouter(trailing_slash=False)
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'Cliente', views.ClienteViewSet)
router.register(r'Transportadora', views.TransportadoraViewSet)
router.register(r'FormaPagto', views.FormaPagtoViewSet)
router.register(r'Status', views.StatusViewSet)
router.register(r'Pedido', views.PedidoViewSet)
router.register(r'Produto', views.ProdutoViewSet)
router.register(r'Item_pedido', views.Item_pedidoViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls), #Possivelmente excluir após finalização da api
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh', TokenRefreshView.as_view()),
]