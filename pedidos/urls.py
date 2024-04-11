from django.urls import path, include
from pedidos.api.view import PedidosViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('pedidos',PedidosViewSet)

urlpatterns = [
    path('', include(router.urls))
]
