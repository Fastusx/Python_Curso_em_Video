def linha():
    print('-=' * 20)


def p1(i, f, p):

    print(f'Contagem de {i} até {f} de {p} em {p}')
    for cont in range(i, f + 1, p):
        print(f'{cont} ', end='')


linha()
print('Contagem de 1 até 10 de 1 em 1:')
for cont in range(1, 11, 1):
    print(f'{cont} ', end='')
print('FIM!')
linha()
print('Contagem de 10 até 0 de 2 em 2:')
for cont in range(10, -1, -2):
    print(f'{cont} ', end='')
print('FIM!')
linha()

print('\n  Agora é com você!')
inicio = int(input('Informe o ÍNICIO: '))
final = int(input('Informe o FINAL: '))
passo = int(input('Quantos passos quer pular? '))
linha()
p1(inicio, final, passo)
linha()
