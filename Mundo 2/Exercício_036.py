casa = float(input('Valor da casa: '))
salario = float(input('Salário do comprador: '))
anos = int(input('Anos de financiamento: '))
prest = casa / (anos * 12)
minimo = salario * 30 / 100
print(f'Para pagar uma casa de R${casa} em {anos} anos,', end='')
print(f' a prestaçao será de R${prest:.2f} ')
if prest <= minimo:
    print('ACESSO pode ser CONCEDIDO!')
else:
    print('ACESSO NEGADO')
