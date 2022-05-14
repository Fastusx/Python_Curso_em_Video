def leiaint(n=0):
    while True:
        try:
            n = int(input('Digite um número inteiro: '))
        except(ValueError, TypeError):
            print('\033[31mPor favor, digite um número inteiro válido!\033[m')
        except KeyboardInterrupt:
            print('\033[31mO usuário não digitou nenhum valor.\033[m')
            return 0
        else:
            return n


def leiafloat(r=0):
    while True:
        try:
            r = float(input('Digite um número real: '))
        except(TypeError, ValueError):
            print('\033[31mPor favor, digite um número real válido!\033[m')
        except KeyboardInterrupt:
            print('\033[31mO usuário não digitou nenhum valor.\033[m')
            return 0
        else:
            return r


print(f'o número inteiro digitado foi {leiaint()} e o número real digitado foi {leiafloat()}')