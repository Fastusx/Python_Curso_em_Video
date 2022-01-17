somaidade = 0
mediaidade = 0
maisvelho = 0
nomemaisvelho = ''
idademulher = 0
for p in range(1, 5):
    print(f'\033[1m--------- {p}° Pessoa -----------')
    nome = str(input('NOME: '))
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [M/F]: \033[m'))
    somaidade += idade
    mediaidade = somaidade / 4
    if p == 1 and sexo in 'Mm':
        maisvelho = idade
        nomemaisvelho = nome
    if sexo in 'Mm' and idade > maisvelho:
        maisvelho = idade
        nomemaisvelho = nome
    if sexo in 'Ff' and idade < 20:
        idademulher =+ 1
print(f'A média de  idade do grupo é {mediaidade} anos')
print(f'O mais velho é {nomemaisvelho} com {maisvelho} anos de idade')
print(f'Ao todo, são {idademulher} com menos de 20 anos')