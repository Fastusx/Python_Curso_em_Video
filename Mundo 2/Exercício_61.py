print('GERADOR DE PA')
print('-=' * 10)
primeiro = int(input('Qual o primeiro termo: '))
razão = int(input('Qual a Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo} -> ', end='')
    termo += razão
    cont += 1
print(' FIM!')
