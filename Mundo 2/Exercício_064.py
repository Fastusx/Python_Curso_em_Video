num = cont = soma = 0
while num != 999:
    num = int(input('Digite um número [999 para parar]: '))
    if num != 999:
        cont += 1
        soma += num
print(f'Você digitou {cont} números e a soma entre eles é {soma}')
