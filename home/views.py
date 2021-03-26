from django.shortcuts import render, redirect

from cadastro.models import *
from adm_votocao.models import *
from datetime import datetime, timezone


def home_view(request):
    objVotacoes = Votacao.objects.all()
    now = datetime.now(timezone.utc)
    # listVotacoes = []
    # print(now)
    # for q in objVotacoes:
    #     if q.horario_inicio > datetime.now() and q.horario_termino < datetime.now():
    #         listVotacoes.append(q)

    context = {
        "listVotacoes": objVotacoes,
    }

    return render(request, "index.html", context)
