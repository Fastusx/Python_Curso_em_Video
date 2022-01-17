primeiro_valor = int(input('Digite um valor: '))

segundo_valor = int(input('Digite outro valor: '))

terceiro_valor = int(input('Digite um terceiro valor: '))

print('''\033[1;34mQual é a comparação desejada?\033[m 
\033[1;31m[1] O maior número
[2] O menor número\033[m''')

opção = int(input('Informe a sua opção: '))

print('\033[1;33m   observação: se ambos os números forem equivalentes, o valor será ser "Valores iguais"\033[m')

if opção == 1 and primeiro_valor > segundo_valor and primeiro_valor > terceiro_valor:
    print(f'Então {primeiro_valor} é o maior')
elif opção == 1 and segundo_valor > primeiro_valor and segundo_valor > terceiro_valor:
    print(f'Então {segundo_valor} é o maior')
elif opção == 1 and terceiro_valor > primeiro_valor and terceiro_valor > segundo_valor:
    print(f'Então {terceiro_valor} é o maior')
elif opção == 2 and primeiro_valor < segundo_valor and primeiro_valor < terceiro_valor:
    print(f'Então {primeiro_valor} é o menor')
elif opção == 2 and segundo_valor < primeiro_valor and segundo_valor < terceiro_valor:
    print(f'Então {segundo_valor} é o menor')
elif opção == 2 and terceiro_valor < primeiro_valor and terceiro_valor < segundo_valor:
    print(f'Então {terceiro_valor} é o menor')
elif opção < 1:
    print('Opção invalida!!! ')
elif opção > 2:
    print('Opção invalida!!!')
else:
    print('Valores iguais')
