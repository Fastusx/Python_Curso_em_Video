from datetime import date
nasc = int(input('Ano de nascimento: '))
hoje = date.today().year
idade = hoje - nasc
print(f'O atleta tem {idade} anos de idade.')
print('Classificação: ', end='')
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 25:
    print('SÊNIOR')
else:
    print('MASTER')
