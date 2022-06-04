n = float(input('Salário Inicial: R$'))
if n > 1250:
    aumento = n + (n * 10/100)
    print(f'Quem ganhava R${n:.2f} passa a ganhar R${aumento:.2f} agora!')
else:
    aumento = n + (n * 15/100)
    print(f'Quem ganhava R${n:.2f} passa a ganhar R${aumento:.2f} agora!')
