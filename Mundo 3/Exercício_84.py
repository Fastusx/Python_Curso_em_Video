maior = menor = 0
temp = []
lista = []
while True:
    temp.append(input('Nome: '))
    temp.append(float(input('Peso: ')))
    if lista.__len__() == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    lista.append(temp[:])
    temp.clear()
    resp = input('Quer continuar [S/N]: ').upper()
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'{lista.__len__()} pessoas cadastradas')
print(f'A lista dos mais pesados ficou: {maior}kg. Peso de ', end='')
for c in lista:
    if c[1] == maior:
        print(f'[{c[0]}] ', end='')
print()
print(f'A lista dos mais leves ficou: {menor}kg. Peso de ', end='')
for c in lista:
    if c[1] == menor:
        print(f'[{c[0]}] ', end='')
print()
