m1 = int(input('Informe a primeira medida: '))

m2 = int(input('informe a segunda medida: '))

m3 = int(input('Informe a terceira medida: '))

condição_de_existência = abs( m2 - m3) < m1 < m2 + m3

if condição_de_existência == True and  m1 == m2 == m3:

    print('Essas medidas PODEM formar um triângulo EQUILÁTERO!!!')

elif  condição_de_existência == True and m1 == m2 != m3 or m1 != m2 == m3:

    print('Essas medidas PODEM formar um triângulo ISÓSCELES!!!')

elif condição_de_existência == True and m1 != m2 != m3:

    print("Essas medidas PODEM formar um triângulo Escaleno!!!")

elif condição_de_existência == False:

    print('Essas medidas NÃO PODEM formar um triângulo!!!')


