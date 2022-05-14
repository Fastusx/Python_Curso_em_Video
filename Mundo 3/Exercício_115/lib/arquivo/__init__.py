from Exercício_115.lib.interface import *


def ArquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def CriarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Ouve um erro na criação do arquivo!')
    else:
        print(f'\033[1;30mArquivo {nome} criado com sucesso!\033[m')


def LerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Falha ao ler o arquivo!')
    else:
        cabecalho('\033[1;31m          PESSOAS CADASTRADAS\033[m')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'\033[1;35m{dado[0]:<30}\033[m\033[1;35m{dado[1]:>3} anos\033[m')


def Cadastrar(arq, nome='Desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro ao abrir o arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro ao escrever os dados!')
        else:
            print(f'Novo cadastro de {nome} adicionado!')
            a.close()
