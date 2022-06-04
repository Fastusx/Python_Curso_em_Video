n = float(input('Distância total da viagem(Km): '))
if n <= 200:
    preco = n * 0.5
    print(f'Você está prestes a fazer uma viagem de {n}Km.\n E o preço da sua viagem será de R${preco:.2f} ')
else:
    preco = n * 0.45
    print(f'Você está prestes a fazer uma viagem de {n}Km.\n E o preço da sua viagem será de R${preco:.2f} ')
