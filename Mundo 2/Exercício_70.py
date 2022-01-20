total = mais1000 = cont = menor = 0
barato = ''
print('-' * 20)
print('LOJA THURZÃO TECH')
print('-' * 20)
while True:
    item = input('Produto: ')
    preco = int(input('Preço: R$ '))
    cont += 1
    total += preco
    if cont == 1 or preco < menor:
        menor = preco
        barato = item
    if preco > 1000:
        mais1000 += 1
    opcao = ' '
    while opcao not in 'SN':
        opcao = input('QUER CONTINUAR [S/N]: ').upper()
    if opcao == 'N':
        break
print(f'O total da compra foi {total}')
print(f'Temos {mais1000} produto(s) custando mais de R$1000,00')
print(f'O produto mais barato foi {barato} por R${menor},00')
