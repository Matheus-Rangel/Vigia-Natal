import os
import requests
import json
from re import sub
from decimal import Decimal

ROOTDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Despesas')
INSTITUICOESDIR = [os.path.join(ROOTDIR, instituicao) for instituicao in os.listdir(ROOTDIR)]


def create_orgao(nome_orgao, id_instituicao):
    url = 'http://localhost:8000/api/orgao/create'
    r = requests.post(url, json = {'nome':nome_orgao, 'instituicao':id_instituicao}, auth=('bot', 'bot123'))
    print(r.json())
    return r.status_code

def create_instituicao(nome_instituicao):
    url = 'http://localhost:8000/api/instituicao/create'
    r = requests.post(url, json = {'nome':nome_instituicao}, auth=('bot', 'bot123'))
    print(r.json())
    return r.status_code

def create_despesa(despesa):
    url = 'http://localhost:8000/api/despesa/create'
    r = requests.post(url, json = despesa, auth=('bot', 'bot123'))
    return r.json()

def validar_instituicao(nome_instituicao):
    url = 'http://localhost:8000/api/instituicao/nome/' + nome_instituicao
    r = requests.get(url)
    try:
        return r.json()["id"]
    except KeyError:
        create_instituicao(nome_instituicao)
        return validar_instituicao(nome_instituicao)

def validar_orgao(nome_orgao, id_instituicao):
    url = 'http://localhost:8000/api/orgao/nome/' + nome_orgao + '/instituicao/' + str(id_instituicao)
    r = requests.get(url)
    try:
        return r.json()["id"]
    except KeyError:
        create_orgao(nome_orgao, id_instituicao)
        return validar_orgao(nome_orgao, id_instituicao)

def formatizar_despesas(despesas, id_instituicao, orgao_id):
    for despesa in despesas:
        despesa_f = {'instituicao':id_instituicao, 'orgao':orgao_id}
        despesa_f['empenhado'] = sub(r'[^\d,]', '', despesa['empenhado']).replace(',','.')
        despesa_f['anulado'] = sub(r'[^\d,]', '', despesa['anulado']).replace(',','.')
        despesa_f['liquidado'] = sub(r'[^\d,]', '', despesa['liquidado']).replace(',','.')
        despesa_f['pago'] = sub(r'[^\d,]', '', despesa['pago']).replace(',','.')
        despesa_f['descricao'] = despesa['historico'] + ". Itens:"
        for item in despesa['itens']:
            despesa_f['descricao'] += item['descricao'] + ". Quantidade: " + item['quantidade'] + ". Valor unitario: R$" + item['valor_unitario'] + ". Valor total: R$" + item['valor_total'] + "."
        dia, mes, ano = despesa['data'].split('/')
        despesa_f['data_inicio'] = ano + '-' + mes + '-' + dia
        print(create_despesa(despesa_f))

def carregar_despesas(i, id_instituicao):
    for file in os.listdir(i):
        nome_orgao, ext = os.path.splitext(file)
        orgao_id = validar_orgao(nome_orgao, id_instituicao)
        f = open(os.path.join(i, file), "rb")
        despesas = json.load(f)
        formatizar_despesas(despesas, id_instituicao, orgao_id)

def main():
    for i in INSTITUICOESDIR:
        id_instituicao = validar_instituicao(os.path.basename(i))
        carregar_despesas(i, id_instituicao)

if __name__ == '__main__':
    main()
