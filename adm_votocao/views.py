from django.shortcuts import render, redirect

from cadastro.models import *
from datetime import datetime, timezone


def votar(request, id_votacao):

    objVotacao = Votacao.objects.get(pk=id_votacao)

    listOpcaoVoto = Opcao_voto.objects.filter(votacao=objVotacao)
    if request.POST:
        idOpcaoVoto = request.POST.get('voto', None)
        objOpcaoVoto = Opcao_voto.objects.get(pk=idOpcaoVoto)

        objOpcaoVoto.quantidade_votos += 1
        objOpcaoVoto.save()
        return redirect('index')

    context = {
        "objVotacao": objVotacao,
        "listOpcaoVoto": listOpcaoVoto,
    }

    return render(request, "votar.html", context)
