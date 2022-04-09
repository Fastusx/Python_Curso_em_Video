jogo = {}
gols = []
jogo['nome'] = input('Nome do jogador? ')
jogo['Partidas'] = int(input(f'Quantas partidas {jogo["nome"]} jogou? '))
for c in range(1, jogo['Partidas'] + 1):
    gols.append(int(input(f'Quantos gols na partida {c}? ')))
    jogo['gols'] = gols
    jogo['Total'] = sum(gols)
print('\n')
print('-=' * 38)
print(jogo)
print('-=' * 38)
for k, v in jogo.items():
    print(f'O campo {k} tem valor {v}')
print('-=' * 38)
print(f'O jogador {jogo["nome"]} jogou {jogo["Partidas"]}.')
for i, v in enumerate(jogo['gols']):
    print(f'     => Na partida {i + 1}, fez {v}')
print(f'Foi um total de {jogo["Total"]} gols.')
