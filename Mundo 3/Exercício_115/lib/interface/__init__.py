def Leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('\033[31mPor favor, digite um número inteiro válido!\033[m')
        except KeyboardInterrupt:
            print('\033[31mO usuário não digitou nenhum valor.\033[m')
            return 0
        else:
            return n


def linha(tam=42):
    return '-' * tam


def cabecalho(str):
    print(linha())
    print(str.center(42))
    print(linha())


def menu(lista):
    cabecalho('\033[1;31m         MENU PRINCIPAL\033[m')
    c = 1
    for item in lista:
        print(f'\033[1;32m{c}\033[m - \033[1;34m{item}\033[m')
        c += 1
    print(linha())
    opc = Leiaint('\033[1;32mSua opção:\033[m ')
    return opc
