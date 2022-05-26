n = float(input('Qual o salário do funcionário? '))
p = int(input('Qual a porcentagem de aumento salarial? '))
au = n + (n * p/100)
print(f'Um funcionário que ganhava R${n}, com {p}% de aumento, passa a receber {au:.2f}!')
