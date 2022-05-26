co = float(input('Comprimento do Cateto Oposto: '))
ca = float(input('Comprimento do Cateto Adjacente: '))
hip = (co ** 2) + (ca ** 2)
print(f'A hipotenusa vai medir {hip ** 0.5:.2f}')