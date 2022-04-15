def ficha(nome='', gols=''):
    if nome == '':
        nome = 'desconhecido'
    if gols == '' or gols is str:
        gols = 0
    return f'O jogador {nome} fez {gols} gols no campeonato'


nome = input('Nome do jogador: ')
gols = (input('Gols feitos: '))
print(ficha(nome, gols))
