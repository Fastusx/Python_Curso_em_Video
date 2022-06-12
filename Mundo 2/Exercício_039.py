from datetime import date
nasc = int(input('Ano de nascimento: '))
hoje = date.today().year
falt = hoje - nasc
print(f'Quem nasceu em em {nasc} tem {falt} em {hoje}')
if falt == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif falt < 18:
    print(f'Ainda faltam {18 - falt} anos para o alistamento')
    print(f'Seu alistamento será {hoje + (18 - falt) }')
else:
    print(f'Você já deveria ter se alistado a {abs(18 - falt)} anos!')
    print(f'Deveria ter se alistado em {hoje - (abs(18 - falt))}')
    