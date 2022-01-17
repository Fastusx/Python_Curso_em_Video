from random import randrange
tentativas = 0
print('Oi, es sou seu computador...\nacabei de pensar em um número entre 1 e 10')
cpu = int(randrange(1, 11))
palpite = int(input("Qual o seu palpite: "))
while palpite != cpu:
    if palpite > cpu:
        palpite = int(input('Menos... Tente novamente: '))
    if palpite < cpu:
        palpite = int(input('Mais... Tente novamente: '))
    tentativas += 1
print(f'CORRETO!!!, o CPU realmente escolheu {cpu}\nVocê adivinhou em {tentativas + 1} tentativas, parabéns!')


