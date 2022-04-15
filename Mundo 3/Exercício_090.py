aluno = dict()
aluno['Nome'] = str(input('Qual o nome do aluno? '))
aluno['Média'] = int(input(f'média de {aluno["Nome"]}?  '))
if 7 > aluno['Média'] > 5:
    aluno['Situação'] = 'recuperação'
elif aluno['Média'] <= 5:
    aluno['Situação'] = 'Reprovado'
else:
    aluno['Situação'] = 'Aprovado'
for k, v in aluno.items():
    print(f'- {k} é igual a {v}')
