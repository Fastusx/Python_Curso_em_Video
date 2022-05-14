from Exercício_115.lib.arquivo import *
from Exercício_115.lib.interface import *
from time import sleep

arq = 'CursoemVídeo.txt'
if not ArquivoExiste(arq):
    CriarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        LerArquivo(arq)
    elif resposta == 2:
        cabecalho('\033[1;31m          CADASTRAR PESSOAS\033[m')
        nome = str(input('\033[1;32mNome: \033[m'))
        idade = Leiaint('\033[1;32mIdade: \033[m')
        Cadastrar(arq, nome, idade)
    elif resposta == 3:
        print('\033[1mSaindo do sistema...\033[m')
        sleep(1)
        break
    else:
        print('\033[1;31mPor favor, digite uma opção válida\033[m')
print('\033[1mAté logo!\033[m')
