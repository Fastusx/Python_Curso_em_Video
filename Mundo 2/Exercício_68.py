from random import randrange
num = cont = 0
while True:
    opcao = input('Qual você escolha [P/I]? ').upper()
    num = int(input('Digite um número de 0 até 10: '))
    cpu = randrange(0, 10)
    soma = num + cpu
    if num > 10 or num < 0:
        print('Valor inválido (Lembre-se, tem que ser um valor POSITIVO e NÃO PODE ser maior que 10 e nem menor que 0)')
        opcao = input('Qual você escolha [P/I]? ').upper()
        num = int(input('Digite um número de 0 até 10: '))
    if opcao in 'Pp' and soma % 2 == 0 or opcao in 'Ii' and soma % 2 == 1:
        if opcao in 'Pp' and soma % 2 == 0:
            print(f'Você jogou {num} e o Computador jogou {cpu}, total de {soma}, PAR')
        if opcao in 'Ii' and soma % 2 == 1:
            print(f'Você jogou {num} e o Computador jogou {cpu}, total de {soma}, ÍMPAR')
        print('Você ganhou!!!')
        print('Vamos jogar novamente...')
        cont += 1
    if opcao in 'Pp' and soma % 2 == 1 or opcao in 'Ii' and soma % 2 == 0:
        if opcao in 'Pp' and soma % 2 == 1:
            print(f'Você jogou {num} e o Computador jogou {cpu}, total de {soma}, ÍMPAR')
        if opcao in 'Ii' and soma % 2 == 0:
            print(f'Você jogou {num} e o Computador jogou {cpu}, total de {soma}, PAR')
        print('Você perdeu, que pena!')
        break
print(f'GAME OVER, você ganhou {cont} vezes consecutivas')
