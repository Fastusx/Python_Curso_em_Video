palavras = ('Pumpum', 'Balacobaco', 'Arthur', 'Egoismo', 'Odio', 'Solidão', 'Duvidas', 'incerto', 'Injusto', 'insanidade')
for termo in palavras:
    print(f' Na palavra {termo.upper()} temos: ')
    for letras in termo:
        if letras.lower() in 'aeiou':
            print(f'{letras}')
print()

