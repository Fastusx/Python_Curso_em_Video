def area(height, length):
    a = height * length
    print(f'A área do terreno de um terreno {height}m x {length}m é {a:.2f}m²')


print('-' * 20)
print('Controle de terrenos')
print('-' * 20)

alt = float(input('Altura do terreno: '))
comp = float(input('Comprimento do terreno: '))
area(alt, comp)
