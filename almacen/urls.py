from django.urls import path
from almacen.views import *

urlpatterns = [
    path('', listar),
    path('crear/', crear, name="crear"),
    path('eliminar/<int:id>/', eliminar, name="eliminar")
]