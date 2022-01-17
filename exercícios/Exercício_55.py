maior = 0
menor = 0
for p in range(1, 7):
    peso = float(input(f'O peso da {p}° Pessoa (em KG): '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
              maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso é {maior}kg e o menor é {menor}kg')


