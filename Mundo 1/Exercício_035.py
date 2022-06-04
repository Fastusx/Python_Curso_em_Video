n1 = float(input('Primeira medida: '))
n2 = float(input('Segunda medida: '))
n3 = float(input('Terceira medida: '))
if abs(n1 - n2) < n3 < (n1 + n2) or abs(n3 - n2) < n1 < (n3 + n2) or abs(n1 - n3) < n2 < (n1 + n3):
    print('Essa medidas podem formar um triângulo!')
else:
    print('Essas medidas não podem formar um triângulo!')
