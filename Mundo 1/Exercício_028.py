from time import sleep
from random import randrange
print('\033[1;33m-=\033[m' * 50)
print('\033[1;34mVou pensar num número entre 0 e 5. Tente adivinhar...\033[m')
print('\033[1;33m-=\033[m' * 50)
print('\033[1;35mPROCESSANDO...\033[m')
sleep(1)
cpu = randrange(0, 6)
ch = int(input('Qual número você adivinhou? '))
print('\033[1;34mO número que eu escolhi foi...')
sleep(1)
print(f'{cpu}\033[m')
if cpu == ch:
    print('\033[1;32mVOCÊ ACERTOU, PARABÉNS!!!\033[m')
elif ch > 5 or ch < 0:
    print('\033[1;31mERRO. Lembre-se que é um número entre 0 e 5!\033[m')
else:
    print('\033[1;37mvocê errou, que pena\033[m.\n Tente Novamente!')
