cont = soma = maior = menor = media = 0
prox = 'S'
while prox in 'Ss':
    n = int(input('Digite um número: '))
    soma += n
    cont += 1
    prox = str(input('Quer continuar[S/N]: ')).upper()
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
media = soma / cont
print(f'Você digitou {cont} números e a média foi {media:.2f}\nO maior valor lido foi {maior} e o menor foi {menor}')



