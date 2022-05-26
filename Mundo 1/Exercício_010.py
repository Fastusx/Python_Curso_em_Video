n = float(input('Quanto você têm na carteira? R$ '))
dol = float(input('Qual o valor do dolar atualmente? R$ '))
vdolar = n / dol
print(f'Com R${n} você pode comprar US${vdolar:.2f}')
