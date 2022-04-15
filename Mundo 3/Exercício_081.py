opcao = 'S'
lista = []
while opcao in 'Ss':
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    opcao = input('Quer continuar[S/N]? ').upper()
print(f'Você digitou {lista.__len__()} elementos')
print(f'Os valores em ordem decrescente são {lista.sort(reverse=True)}')
print(lista)
proucura = lista.count(5)
if proucura != 0:
    print('O valor 5 FAZ parte da lista!')
else:
    print('O valor 5 NÃO faz parte da lista!')
