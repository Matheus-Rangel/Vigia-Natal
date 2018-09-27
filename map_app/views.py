import json

from django.shortcuts import render
from django.utils import timezone

from map_app.models import Despesa, Orgao
from map_app.forms import DespesaForm, OrgaoForm


from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import (TemplateView, DetailView, ListView,
                                    CreateView, UpdateView)
# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'

class DadosGeraisView(TemplateView):
    template_name = 'dados_gerais.html'
    def get_context_data(self, **kwargs):
        context = super(DadosGeraisView, self).get_context_data(**kwargs)
        context['despesas_instituicoes'] = json.loads(r"""
        [
           {
              "Instituição": "PREFEITURA MUNICIPAL DO NATAL",
              "Empenhado": "2.100.230.120,66",
              "Anulado": "385.686.291,91",
              "Liquidado": "960.354.861,58",
              "Pago": "760.599.006,56"
           },
           {
              "Instituição": "INST PREV SOCIAL DOS SERV DO MUN DO NATAL",
              "Empenhado": "205.087.141,32",
              "Anulado": "170.065,94",
              "Liquidado": "150.859.473,54",
              "Pago": "143.995.529,44"
           },
           {
              "Instituição": "COMPANHIA DE SERVIÇOS URBANOS DO NATAL",
              "Empenhado": "177.971.988,93",
              "Anulado": "1.756.671,03",
              "Liquidado": "113.730.367,02",
              "Pago": "91.445.826,58"
           },
           {
              "Instituição": "CAMARA MUNICIPAL DO NATAL",
              "Empenhado": "43.590.246,63",
              "Anulado": "721.601,59",
              "Liquidado": "35.500.858,85",
              "Pago": "35.409.261,75"
           },
           {
              "Instituição": "FUNDAÇÃO CULTURAL CAPITANIA DAS ARTES",
              "Empenhado": "21.003.566,25",
              "Anulado": "3.740.872,38",
              "Liquidado": "11.499.154,99",
              "Pago": "7.763.659,85"
           },
           {
              "Instituição": "EMPRESA DE FOMENTO E SEGURANÇA ALIMENTAR",
              "Empenhado": "5.072.252,69",
              "Anulado": "5.923,05",
              "Liquidado": "3.364.892,79",
              "Pago": "2.346.549,42"
           },
           {
              "Instituição": "AG REG DE SERV DE SANEAM BÁSICO DO MUN DO NATAL",
              "Empenhado": "3.204.536,20",
              "Anulado": "259.931,83",
              "Liquidado": "1.566.673,65",
              "Pago": "1.566.673,65"
           },
           {
              "Instituição": "PROCON",
              "Empenhado": "1.007.499,66",
              "Anulado": "28.808,00",
              "Liquidado": "628.391,23",
              "Pago": "609.069,39"
           }
        ]""")
        context['despesa_prefeitura_por_orgaos'] = json.loads(r"""
        [
           {
              "Orgão": "SECRETARIA MUNICIPAL DE SAUDE",
              "Empenhado": "992.383.997,52",
              "Anulado": "306.259.450,73",
              "Liquidado": "360.715.205,69",
              "Pago": "253.203.492,04"
           },
           {
              "Orgão": "SECRETARIA MUNICIPAL DE EDUCACAO",
              "Empenhado": "459.318.101,92",
              "Anulado": "29.171.553,81",
              "Liquidado": "236.732.950,53",
              "Pago": "180.628.676,36"
           },
           {
              "Orgão": "SECRETARIA MUNICIPAL DE ADMINISTRAÇÃO",
              "Empenhado": "291.468.172,10",
              "Anulado": "5.876.105,26",
              "Liquidado": "181.886.244,35",
              "Pago": "163.648.197,10"
           },
           {
              "Orgão": "SECRETARIA MUNICIPAL DE SERVICOS URBANOS",
              "Empenhado": "68.021.862,03",
              "Anulado": "13.808.203,71",
              "Liquidado": "31.591.994,68",
              "Pago": "29.814.399,36"
           },
           {
              "Orgão": "PROCURADORIA GERAL DO MUNICIPIO",
              "Empenhado": "49.530.440,45",
              "Anulado": "13.727.476,98",
              "Liquidado": "19.791.653,99",
              "Pago": "14.609.815,41"
           },
           {
              "Orgão": "SECRETARIA MUNIC. DO TRABALHO E ASSISTENCIA SOCIAL",
              "Empenhado": "41.790.075,15",
              "Anulado": "1.108.902,55",
              "Liquidado": "28.419.612,86",
              "Pago": "26.423.782,36"
           },
           {
              "Orgão": "SECRETARIA MUNICIPAL DE OBRAS PÚBLICAS E INFRA-EST",
              "Empenhado": "35.647.980,69",
              "Anulado": "2.808.941,10",
              "Liquidado": "12.244.050,16",
              "Pago": "11.788.991,04"
           },
           {
              "Orgão": "SECRETARIA MUNICIPAL DE MOBILIDADE URBANA",
              "Empenhado": "34.417.339,20",
              "Anulado": "3.704.945,33",
              "Liquidado": "21.798.318,37",
              "Pago": "21.350.075,70"
           },
           {
              "Orgão": "SECRETARIA MUNICIPAL DE TRIBUTACAO",
              "Empenhado": "29.905.315,71",
              "Anulado": "19.518,53",
              "Liquidado": "17.061.409,99",
              "Pago": "16.853.588,37"
           },
           {
              "Orgão": "SECRETARIA MUNICIPAL DE SEGURANÇA PÚBLICA E DEFESA",
              "Empenhado": "24.306.301,08",
              "Anulado": "519.997,97",
              "Liquidado": "14.879.744,33",
              "Pago": "14.782.712,88"
           },
           {
              "Orgão": "SECRETARIA MUNICIPAL DO MEIO AMBIENTE E URBANISMO",
              "Empenhado": "21.165.372,96",
              "Anulado": "1.655.310,41",
              "Liquidado": "11.126.420,33",
              "Pago": "6.265.500,60"
           },
           {
              "Orgão": "SECRETARIA MUNICIPALDE ESPORTE E  LAZER",
              "Empenhado": "11.098.865,20",
              "Anulado": "1.392.010,34",
              "Liquidado": "4.689.731,75",
              "Pago": "4.481.527,48"
           },
           {
              "Orgão": "SECRETARIA MUNICIPAL PLANEJAMENTO",
              "Empenhado": "10.112.184,51",
              "Anulado": "4.176.585,76",
              "Liquidado": "2.891.020,97",
              "Pago": "2.803.653,23"
           },
           {
              "Orgão": "SECRETARIA MUNICIPAL DE COMUNICAÇÃO SOCIAL",
              "Empenhado": "8.515.980,80",
              "Anulado": "98.992,00",
              "Liquidado": "4.974.880,52",
              "Pago": "2.949.996,80"
           },
           {
              "Orgão": "SECRETARIA MUNICIPAL DE GOVERNO",
              "Empenhado": "8.373.736,93",
              "Anulado": "129.607,26",
              "Liquidado": "4.110.876,12",
              "Pago": "3.907.407,12"
           },
           {
              "Orgão": "SEC. MUNIC. DE HABITAÇÃO, REGULARIZAÇÃO FUNDIÁRIA",
              "Empenhado": "4.280.084,57",
              "Anulado": "198.033,00",
              "Liquidado": "2.161.166,95",
              "Pago": "2.031.257,24"
           },
           {
              "Orgão": "SECRETARIA MUNICIPAL DE TURISMO",
              "Empenhado": "3.374.175,52",
              "Anulado": "8.871,26",
              "Liquidado": "1.796.557,91",
              "Pago": "1.717.823,18"
           },
           {
              "Orgão": "CONTROLADORIA GERAL DO MUNICIPIO",
              "Empenhado": "3.349.769,77",
              "Anulado": "43.114,80",
              "Liquidado": "2.109.777,89",
              "Pago": "2.087.430,09"
           },
           {
              "Orgão": "SECRETARIA MUNICIPAL DE POLÍTICAS PARA AS MULHERES",
              "Empenhado": "1.877.984,80",
              "Anulado": "41.312,03",
              "Liquidado": "1.018.223,52",
              "Pago": "895.659,53"
           },
           {
              "Orgão": "GABINETE DO VICE PREFEITO",
              "Empenhado": "1.292.379,75",
              "Anulado": "937.359,08",
              "Liquidado": "355.020,67",
              "Pago": "355.020,67"
           }
        ]
        """)
        context['despesas_obras_e_instalacoes_por_orgaos'] = json.loads(r"""
        [
           {
              "Orgão": "SECRETARIA MUNICIPAL DE OBRAS PÚBLICAS E INFRA-EST",
              "Empenhado": "14.924.112,81",
              "Anulado": "2.508.422,80",
              "Liquidado": "1.807.141,23",
              "Pago": "1.591.604,25"
           },
           {
              "Orgão": "SECRETARIA MUNICIPAL DE EDUCACAO",
              "Empenhado": "10.908.714,97",
              "Anulado": "1.640.558,65",
              "Liquidado": "343.672,00",
              "Pago": "166.196,23"
           },
           {
              "Orgão": "SECRETARIA MUNICIPAL DE SAUDE",
              "Empenhado": "2.064.853,14",
              "Anulado": "60.100,00",
              "Liquidado": "488.697,79",
              "Pago": "134.156,36"
           },
           {
              "Orgão": "SECRETARIA MUNICIPAL DE MOBILIDADE URBANA",
              "Empenhado": "2.059.630,60",
              "Anulado": "728.622,22",
              "Liquidado": "350.305,57",
              "Pago": "214.816,99"
           },
           {
              "Orgão": "SECRETARIA MUNICIPALDE ESPORTE E  LAZER",
              "Empenhado": "1.310.095,58",
              "Anulado": "1.000.000,00",
              "Liquidado": "172.093,30",
              "Pago": "172.093,30"
           },
           {
              "Orgão": "SECRETARIA MUNICIPAL DE SERVICOS URBANOS",
              "Empenhado": "1.172.717,62",
              "Anulado": "89.009,32",
              "Liquidado": "392.279,24",
              "Pago": "392.279,24"
           },
           {
              "Orgão": "SEC. MUNIC. DE HABITAÇÃO, REGULARIZAÇÃO FUNDIÁRIA",
              "Empenhado": "394.669,58",
              "Anulado": "0,00",
              "Liquidado": "0,00",
              "Pago": "0,00"
           },
           {
              "Orgão": "SECRETARIA MUNICIPAL DE SEGURANÇA PÚBLICA E DEFESA",
              "Empenhado": "14.875,00",
              "Anulado": "0,00",
              "Liquidado": "0,00",
              "Pago": "0,00"
           },
           {
              "Orgão": "SECRETARIA MUNICIPAL DO MEIO AMBIENTE E URBANISMO",
              "Empenhado": "10.816,00",
              "Anulado": "0,00",
              "Liquidado": "0,00",
              "Pago": "0,00"
           }
        ]
        """)
        return context

class DespesaListView(ListView):
    model = Despesa
    def get_queryset(self):
        return Despesa.objects.all()

class OrgaoListView(ListView):
    model = Orgao
    def get_queryset(self):
        return Orgao.objects.all()

class DespesaDetailView(DetailView):
    model = Despesa

class OrgaoDetailView(DetailView):
    model = Orgao
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['despesa_list'] = Despesa.objects.filter(orgao = self.kwargs['pk'])
        return context

class CreateDespesaView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'map_app/despesa_detail.html'
    form_class = DespesaForm
    model = Despesa

class CreateOrgaoView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'map_app/orgao_detail.html'
    form_class = OrgaoForm
    model = Orgao

class DespesaUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'map_app/despesa_detail.html'
    form_class = DespesaForm
    model = Despesa

class OrgaoUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'map_app/orgao_info.html'
    form_class = OrgaoForm
    model = Orgao
