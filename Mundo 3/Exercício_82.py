opcao = 'S'
lista = []
listai = []
listap = []
while opcao in 'Ss':
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    if valor % 2 == 0:
        listap.append(valor)
    else:
        listai.append(valor)
    opcao = input('Quer continuar[S/N]? ').upper()
print(f'A lista completa é: {lista}')
print(f'A lista dos números pares: {listap}')
print(f'A lista dos números impares: {listai}')
