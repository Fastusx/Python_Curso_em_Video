jogador = {}
time = []
partidas = []

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador? '))
    tot = int(input(f'Quantas partidas {jogador["nome"]}? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'      Quantos gols na partida {c}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    opcao = input('Quer continuar [S/N]? ')
    if opcao in 'Nn':
        break
print('-=' * 30)
print('Cod', end='')
for i in jogador.keys():
    print(f' {i:<15}', end='')
print()
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    m = int(input('Mostrar dados de qual jogador, digite pelo código[999 para finalizar]? '))
    if m == 999:
        break
    if m >= len(time):
        print(f'ERRO! NÃO EXISTE JOGADOR COM CÓDIGO {m}')
    else:
        print(f'LEVANTAMENTO DO JOGADOR {time[m]["nome"]}')
        for i, v in enumerate(time[m]['gols']):
            print(f'{i + 1}º partida: {v} gols.')
print('<<< VOLTE SEMPRE >>>')
