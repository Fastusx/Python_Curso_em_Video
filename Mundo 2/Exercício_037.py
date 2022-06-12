n = int(input('Número inteiro: '))
print('''Escolha uma dos bases para conversão:
[1] Binário
[2] Octal
[3] Hexadecimal''')
opcao = int(input('sua opção: '))
print(f'O número {n} convertido para', end='')
if opcao == 1:
    print(f' Binário fica {bin(n) [2:]}')
elif opcao == 2:
    print(f' Octal fica {oct(n) [2:]}')
else:
    print(f'Hexadecimal fica {hex(n) [2:]}')
