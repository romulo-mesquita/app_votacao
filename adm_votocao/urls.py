from django.urls import path
from .import views

urlpatterns = [
    path('votar/<int:id_votacao>/', views.votar, name="votar"),
]
