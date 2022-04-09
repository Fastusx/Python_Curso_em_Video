from random import randint
from time import sleep
from operator import itemgetter
jogadas = {'Jogador 1': randint(1, 6),
           'Jogador 2': randint(1, 6),
           'Jogador 3': randint(1, 6),
           'Jogador 4': randint(1, 6)}
rank = []
for k, v in jogadas.items():
    print(f'O {k} tirou {v} no dado!')
    sleep(1)
rank = sorted(jogadas.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
print('== RANKING DOS JOGADORES ==')
for c, v in enumerate(rank):
    print(f'{c + 1}º Lugar: {v[0]} com {v[1]}')
