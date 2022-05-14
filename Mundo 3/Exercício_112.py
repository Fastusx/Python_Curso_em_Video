from utilidadescev import moeda, dado
num = dado.leiadinheiro('Digite o preço:R$ ')
mais = int(input('Digite um valor de porcentagem para AUMENTAR: '))
menos = int(input('Digite um valor de porcentagem para DIMINUIR: '))
moeda.resumo(num, mais, menos)
