from datetime import date
totmaior = 0
totmenor = 0
atual = date.today().year
for c in range(1, 8):
    ano = int(input(f'Ano de nascimento da {c}° pessoa: '))
    idade = atual - ano
    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1
print(f'No total, o número de pessoas MAIORES de idade é {totmaior}')
print(f'Já o número de pessoas MENORES de idade é {totmenor}')