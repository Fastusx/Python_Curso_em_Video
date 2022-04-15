from datetime import datetime
cadastro = {}
cadastro['nome'] = str(input('Nome: '))
cadastro['Ano de nascimento'] = int(input('Ano de nascimento: '))
cadastro['ctps'] = int(input('Carteira de trabalho (0 se não tem) '))
cadastro['idade'] = datetime.today().year - cadastro['Ano de nascimento']
if cadastro['ctps'] != 0:
    cadastro['Ano de contratação'] = int(input('Ano de contratação: '))
    cadastro['Salário'] = float(input('Salário: '))
    cadastro['genero'] = input('Gênero (M/F): ').upper()
    if cadastro['genero'] in 'Mm':
        cadastro['Aposentadoria'] = 65 - cadastro['idade']
    elif cadastro['genero'] in 'Ff':
        cadastro['Aposentadoria'] = 61 - cadastro['idade']
for k, v in cadastro.items():
    print(f'- {k} é {v}')
