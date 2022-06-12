n = int(input('Digite um número: '))
print(f'Agora você verá todos os números páres existentes de 0 até {n}...')
if n > 1:
    for c in range(2, n + 1, 2):
        print(f' {c} ', end='')
else:
    for c in range(2, n - 1, -2):
        print(f' {c} ', end='')
