from random import sample
print('\033[1m-=' * 20)
print('               MEGA SENA')
print('-=\033[m' * 20)
sub = []
lista = []
while True:
    jogos = int(input('Quantos jogos você quer sortear? '))
    print('\033[1m-=' * 6, f' SORTEANDO {jogos} JOGOS', '-=\033[m' * 6)
    print()
    for c in range(1, jogos + 1):
        n = sample(range(1, 101), 6)
        sub.append(n)
        lista.append(sub[:])
        sub.clear()
        print(f'{c}º jogo: {n}')
    print()
    print('-' * 45)
    opcao = str(input('Quer continuar[S/N]? ')).upper()
    if opcao in 'Nn':
        break
print(f'Todos os jogos sorteados foram: {lista}', end='')
