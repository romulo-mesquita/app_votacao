from django import forms
from cadastro.models import *


class Pessoaform(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ["nome_completo","cpf","data_nascimento","email"]

class Votacaoform(forms.ModelForm):
    class Meta:
        model = Votacao
        fields = ["nome_completo","descricao","anonimo","voto_unico","horario_inicio","horario_termino"]

class Opcao_votoform(forms.ModelForm):
    class Meta:
        model = Opcao_voto
        fields = ["nome_completo","votacao","codigo_votacao"]
