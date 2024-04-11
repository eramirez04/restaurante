from django.urls import path, include
from rest_framework import routers
from .api import view

router = routers.DefaultRouter()
router.register('factura', view.FacturaView)

urlpatterns = [
    path('', include(router.urls))
]
