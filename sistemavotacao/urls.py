from django.contrib import admin
from django.urls import path
from cadastro.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registrar-pessoa/',registrar_pessoa , name="registrar_pessoa"),
    path('registrar-votacao/',registrar_votacao , name="registrar_votacao"),
    path('registrar-opcao-voto/',registrar_opcao_voto , name="registrar_opcao_voto"),
    path('', index, name="index"),
]
