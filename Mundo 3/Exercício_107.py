from modulos import moeda
num = float(input('Preço: R$'))
print(f'A metade de {num} é {moeda.metade(num):.1f}')
print(f'O dobro de {num} é {moeda.dobro(num):.1f}')
print(f'Aumentando 10% de {num}, ficaria {moeda.aumento(num):.1f}')
