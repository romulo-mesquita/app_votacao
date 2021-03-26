from django.shortcuts import render, redirect

from cadastro.models import *
from adm_votocao.models import *
import datetime
from django.utils import timezone


def home_view(request):
    objVotacoes = Votacao.objects.filter(horario_termino__gt=timezone.now())
    context = {
        "listVotacoes": objVotacoes,
    }

    return render(request, "index.html", context)
