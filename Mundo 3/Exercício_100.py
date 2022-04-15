from random import randint
from time import sleep


def sorteia(lst):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        num = randint(1, 10)
        lst.append(num)
        print(f'{num} ', end='', flush=True)
        sleep(0.3)
    print('PRONTO!')


def somap(lst):
    soma = 0
    for valor in lst:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares da {lst}, temos {soma}')


numeros = []
sorteia(numeros)
somap(numeros)
