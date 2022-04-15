def aluno(nota, sit=False):
    """
          -> Ler notas de vários alunos mostrando totoal de notas, maior e menor nota, média e situação
    :param nota: nota dos alunos indicados (podem ser vários)
    :param sit: (opcional) mostrar situação ou não(Aprovado, Recuperação ou Reprovado)
    :return: total de notas, maior nota, menor nota, média aritmética das notas e situação (opcional)
    código por Arthur Santos, 14/07/2022
    """
    dictnts = {}
    dictnts['Total'] = len(nota)
    dictnts['Maior'] = max(nota)
    dictnts['Menor'] = min(nota)
    dictnts['média'] = sum(nota)/len(nota)
    if sit:
        if dictnts['média'] >= 7:
            dictnts['Situação'] = 'Aprovado'
        elif 5 <= dictnts['média'] < 7:
            dictnts['Situação'] = 'Recuperação'
        else:
            dictnts['Situação'] = 'Reprovado'

    return dictnts


n = []
while True:
    resp = float(input(f'Nota do aluno(a): '))
    n.append(resp)
    r = input('Tem mais [S/N]? ').upper()
    if r in 'Nn':
        break

print(aluno(n, sit=True))
help(aluno)
