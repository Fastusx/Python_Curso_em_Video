matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spares = maior = coluna3 = 0
for f in range(0, 3):
    for c in range(0, 3):
        matriz[f][c] = int(input(f'Digite um número para [{f}, {c}]: '))
print('-=' * 30)
for f in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[f][c]:^5}]', end='')
        if matriz[f][c] % 2 == 0:
            spares += matriz[f][c]
    print()
print('-=' * 30)
print(f'A soma dos pares da matriz é: {spares}')
for f in range(0, 3):
    coluna3 += matriz[f][2]
print(f'A soma dos números da terceira coluna é: {coluna3}')
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior número da segunda linha da matriz é: {maior}')
