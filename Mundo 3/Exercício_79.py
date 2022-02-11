valor = 0
opcao = 'S'
lista = []
while opcao not in 'Nn':
    valor = int(input('Digite um valor: '))
    if valor >= 0:
        lista.append(valor)
    proucura = lista.count(valor)
    if proucura > 1:
        lista.append(valor)
        del lista[valor]
        valor = int(input('Número repetido, digite outro valor: '))
    opcao = input('Quer continuar[S/N]? ').upper()
lista.sort()
print(lista)
