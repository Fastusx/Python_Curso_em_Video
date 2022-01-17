sexo = str(input('Informe seu sexo[M/F]: ')).strip().upper()[0]
while sexo not in 'FfMm' and sexo != int and sexo != float:
    sexo = str(input('Dados inválidos, por favor informe novamente o seu sexo[M/F]: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso')