from django.urls import path, include
from productos.api.ModelViewSet import ProductosModelViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('productos', ProductosModelViewSet)

urlpatterns = [
    path('', include(router.urls))
]
