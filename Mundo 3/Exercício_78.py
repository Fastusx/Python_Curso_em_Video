lista = []
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor pra a posição {c}: ')))
maior = max(lista)
menor = min(lista)
print(f'Você digitou os valores {lista}')
print(f'O MAIOR valor informado foi {maior} nas posições ', end='')
for i, c in enumerate(lista):
    if c == maior:
        print(f'{i}... ', end='')
print()
print(f'O MENOR valor informado foi {menor} nas posições ', end='')
for i, c in enumerate(lista):
    if c == menor:
        print(f'{i}...', end='')
print()
print('Programa finalizado!')
