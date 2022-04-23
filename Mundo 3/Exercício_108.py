from modulos import moeda
num = float(input('Preço: R$'))
mais = int(input('Digite um valor de porcentagem para AUMENTAR: '))
menos = int(input('Digite um valor de porcentagem para DIMINUIR: '))
print(f'A metade de {moeda.moeda(num)} é {moeda.moeda(moeda.metade(num))}')
print(f'O dobro de {moeda.moeda(num)} é {moeda.moeda(moeda.dobro(num))}')
print(f'Aumentando {mais}% de {moeda.moeda(num)}, ficaria {moeda.moeda(moeda.aumento(num, mais))}')
print(f'Diminuindo {menos}% de {moeda.moeda(num)}, ficaria {moeda.moeda(moeda.diminuir(num, menos))}')
