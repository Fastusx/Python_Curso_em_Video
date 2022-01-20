cont18 = homem = mulher = 0
while True:
    idade = int(input('Idade: '))
    sexo = (input('Sexo[M/F]: ')).upper()
    print('-' * 20)
    opcao = (input('Quer continuar[S/N]: ')).upper()
    if idade > 18:
        cont18 += 1
    if sexo in 'Mm':
        homem += 1
    if sexo in 'Ff' and idade < 20:
        mulher += 1
    if opcao in 'Nn':
        break
print(f'O total de pessoas com mais de 18 anos é {cont18}')
print(f'Ao todo temos {homem} homem(ns) cadastrado(s)')
print(f'E temos {mulher} mulher(es) com menos de 18 anos cadastrada(s)')
