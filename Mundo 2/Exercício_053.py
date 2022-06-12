nome = str(input('Frase: ')).upper().strip()
print(f'O inverso de {nome} é {nome[::-1]}')
if nome[::-1] == nome:
    print('Essa frase É um Palíndromo!')
else:
    print('Essa frase NÃO É um Palíndromo!')