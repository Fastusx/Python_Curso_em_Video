print('GERADOR DE PA')
print('-=' * 10)
primeiro = int(input('Qual o primeiro termo: '))
razao = int(input('Qual a Razão da PA: '))
termo = primeiro
cont = 1
total = 0
adi = 10
while adi != 0:
    total = total + adi
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo += razao
        cont += 1
    print('PAUSA')
    adi = int(input('Quantos termos você quer a mais? '))
print(f'A PA foi encerrada com {total} termos mostrados!')
print(' FIM!')
