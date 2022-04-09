cont = contm = 0
vc = {}
dados = []
nome = []
idade = []
nomesm = []
sexo = []
amedia = []
while True:
    vc['Nome'] = input('Nome: ')
    nome.append(vc.copy()['Nome'])
    cont += 1
    vc['Sexo'] = input('Sexo [M/F]: ').upper()
    sexo.append(vc.copy()['Sexo'])
    vc['Idade'] = int(input('Idade: '))
    dados.append(vc.copy())
    idade.append(vc.copy()['Idade'])
    opcao = input('Quer continuar [S/N]? ').upper()
    media = float(sum(idade)) / (len(idade))
    if vc['Sexo'] in 'Ff':
        nomesm.append(vc.copy()['Nome'])
    if vc['Idade'] > media:
        amedia.append(vc.copy())
    if opcao in 'Nn':
        break
print(f'A)  Ao todo temos {cont} pessoas cadastradas.')
print()
print(f'B)  A média de idade é de {media:5.2f}')
print()
print(f'C)  As mulheres cadastradas foram {nomesm}')
print()
print(f'D)  Pessoas que estão acima da média: ')
for p in dados:
    if p['Idade'] >= media:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
print()
print('<<< ENCERRADO!!! >>>')
