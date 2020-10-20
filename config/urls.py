from django.contrib import admin
from django.urls import path, include
from IOT.views import LampViewSet,UsuarioViewSet,HistViewSet
from rest_framework import routers



router = routers.DefaultRouter()
router.register(r'Lamp',LampViewSet)
router.register(r'Usuario',UsuarioViewSet)
router.register(r'Hist',HistViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),

]
