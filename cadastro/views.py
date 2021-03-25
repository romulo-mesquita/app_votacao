from django.shortcuts import render, redirect

from cadastro.forms import *
from cadastro.models import * 

def registrar_pessoa(request):

    form = Pessoaform() 
    todas_pessoas = Pessoa.objects.all()
    if request.method == "POST":

        form = Pessoaform(request.POST)

        if form.is_valid():

            form.save()
            return redirect("registrar_pessoa")

            
    context = {
        "form": form,
        "todas_pessoas" : todas_pessoas,
        "nome_pagina": "Pessoa",

    }

    return render(request,"registrar_pessoa.html",context)


def registrar_votacao(request):

    form = Votacaoform() 
    todas_votacoes = Votacao.objects.all()
    if request.method == "POST":

        form = Votacaoform(request.POST)

        if form.is_valid():

            form.save()
            return redirect("registrar_votacao")

            
    context = {
         "form": form,
         "todas_votacoes" : todas_votacoes,
         "nome_pagina": "Votação",

    }

    return render(request,"registrar_votacao.html",context)

def registrar_opcao_voto(request):


    form = Opcao_votoform() 
    todas_opcoes_voto = Opcao_voto.objects.all()
    if request.method == "POST":

        form = Opcao_votoform(request.POST)

        if form.is_valid():

            form.save()
            return redirect("registrar_opcao_voto")

    context = {
         "form": form,
         "todas_opcoes_voto" : todas_opcoes_voto,
         "nome_pagina": "Opção de voto",

    }

    return render(request,"registrar-opcao-voto.html",context)




def index(request):

    context = {
         "nome_pagina": "Menu",
    }

    return render(request,"index.html",context)


