n = int(input('Digite um numero para ver sua tabuada:'))
print('''\033[1;31m[1] Adição
[2] Subtração
[3] Multiplicação
[4] Divisão\033[m''')
op = int(input('Qual a operação desejada ? '))
if op == 1:
     for i in range(1, 11):
         print(f'{n} + {i} = {n + i}')
if op == 2:
    for i in range(1, 11):
        print(f'{n} - {i} = {n - i}')
if op == 3:
    for i in range(1, 11):
        print(f'{n} * {i} = {n * i}')
if op == 4:
    for i in range(1, 11):
        print(f'{n} / {i} = {n / i}')

