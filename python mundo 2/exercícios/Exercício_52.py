num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[1;33m', end=' ')
        tot += 1
    else:
        print('\033[m', end=' ')
    print(c, end=' ')
print(f'\n\033[mO número {num} foi dividido {tot} vezes')
if tot == 2:
    print('O número É PRIMO!')
else:
    print('o número NÃO É PRIMO')

