from random import choice
print('''\033[1;31m[1] Pedra
[2] Papel
[3] Tesoura\033[m''')
CPU = ['Pedra', 'Papel', 'Tesoura']
a = int(input('Qual sua opção: '))
b = str(choice(CPU))
print(f'Então você escolheu {a}')
print(f'Eu escolhi...\n {b}')
if a == 1 and b == 'Tesoura':
    print('Você GANHOU, parabéns!!!')
if a == 2 and b == 'Pedra':
    print('Você GANHOU, parabéns!!!')
if a ==  3 and b == 'Papel':
    print('Você GANHOU, parabéns!!!')
Pedra = int(1)
Papel = int(2)
Tesoura = int(3)
if Pedra == 'Pedra' or Papel == 'Papel' or Tesoura == 'Tesoura':
    print('NINGUÉM VENCEU, que pena')
else:
    print('Jogada Inválida!!!!!!!')