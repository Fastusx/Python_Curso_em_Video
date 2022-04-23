from modulos import moeda
num = float(input('Preço: R$'))
mais = int(input('Digite um valor de porcentagem para AUMENTAR: '))
menos = int(input('Digite um valor de porcentagem para DIMINUIR: '))
print(f'A metade de {moeda.moeda(num)} é {moeda.metade(num,True)}')
print(f'O dobro de {moeda.moeda(num)} é {moeda.dobro(num,True)}')
print(f'Aumentando {mais}% de {moeda.moeda(num)}, ficaria {moeda.aumento(num, mais, True)}')
print(f'Diminuindo {menos}% de {moeda.moeda(num)}, ficaria {moeda.diminuir(num, menos, True)}')
