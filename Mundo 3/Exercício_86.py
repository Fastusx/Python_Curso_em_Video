matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for f in range(0, 3):
    for c in range(0, 3):
        matriz[f][c] = int(input(f'Digite um número para [{f}, {c}]: '))
print('-=' * 30)
for f in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[f][c]:^5}]', end='')
    print()
