print('\033[1m-=\033[m' * 15)
print('\033[1;31mPrograma TABUADA inicializado\033[m')
print('\033[1m-=\033[m' * 15)
while True:
    num = int(input('Qual número você quer ver a tabuada [Digite um número negativo para encerrar o programa]? '))
    if num < 0:
        break
    print('-' * 30)
    for c in range(1, 11):
        print(f'{num} X {c} = {num * c}')
    print('-' * 30)
print('Programa TABUADA encerrado com sucesso')
