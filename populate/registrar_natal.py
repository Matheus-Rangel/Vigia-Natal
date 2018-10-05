import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vigia_natal.settings')

import django
django.setup()

from map_app.models import Instituicao, Orgao, Despesa

ROOTDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Despesas')
INSTITUICOESDIR = [os.path.join(ROOTDIR, instituicao) for instituicao in os.listdir(ROOTDIR)]
INSTITUICOES = [i.basename for i in INSTITUICOESDIR]

def validar_instituicao(nome_instituicao):
    print(Instituicao.objects.filter(nome = nome_instituicao))

def main():
    print(INSTITUICOES)
    for i in INSTITUICOES:
        validar_instituicao(i)

if __name__ == '__main__':
    main()
