from datetime import date
ano = int(input('Ano qualquer[Digite 0 para escolher o ano atual]: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'{ano} É um ano bissexto!')
else:
    print(f'{ano} NÃO é um ano bissexto!')
