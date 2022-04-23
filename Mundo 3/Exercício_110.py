from modulos import moeda
num = float(input('Preço: R$'))
mais = int(input('Digite um valor de porcentagem para AUMENTAR: '))
menos = int(input('Digite um valor de porcentagem para DIMINUIR: '))
moeda.resumo(num, mais, menos)
