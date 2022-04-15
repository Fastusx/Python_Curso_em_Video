print('\033[1;31m===========\033[m \033[1;34mLOJAS SANTOS\033[m \033[1;31m===========\033[m')
preço_inicial = (float(input('Informe o preço do produto escolhido: ')))
print('''Qual vai ser a forma de pagamento
\033[1;31m[1] À vista no dinheiro/cheque
[2] À vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão\033[m ''')
condição_de_pagamento = int(input('Qual a sua opção? '))
if condição_de_pagamento == 1:
    total = preço_inicial - (preço_inicial * 0.10)
elif condição_de_pagamento == 2:
    total = preço_inicial - (preço_inicial * 0.5)
elif condição_de_pagamento == 3:
    total = preço_inicial
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de {parcela}')
elif condição_de_pagamento == 4:
    vezes_parceladas = int(input('Em quantas vezes vai querer parcelar? '))
    total = preço_inicial + ( preço_inicial * 0.2)
    parcela = total / vezes_parceladas
    print(f'Sua compra será parcelada em {vezes_parceladas}x de {parcela} COM JUROS')
print(f'Sua compra de R${preço_inicial:.2f} vai custar R${total:.2f} no final.')