primeira_nota = float(input('Informe a sua primeira nota: '))

segunda_nota = float(input('Informe a sua segunda nota: '))

media = float((primeira_nota + segunda_nota) / 2)

print(f'A sua média é {media}')

if media < 5:

    print('Você foi REPROVADO!!!')

elif media >= 5 and media <= 6.9:

    print('Você ficou de RECUPERAÇÃO!!!')

elif media >= 7:

    print('Você foi APROVADO!!!')

elif media > 10.0:

    print('Média máxima ultrapassada, valores inválidos!!!')



