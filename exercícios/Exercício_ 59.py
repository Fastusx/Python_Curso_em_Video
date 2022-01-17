from time import sleep
maior = 0
primeiro = int(input('Digite o primeiro valor: '))
segundo = int(input('Digite o segundo valor: '))
print('''[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Finalizar o programa''')
opção = int(input('>>>>>> Qual a sua escolha? '))
while opção != 5:
    if opção == 1:
        print(f'A soma entre {primeiro} e {segundo} é igual a {primeiro + segundo}')
    if opção == 2:
        print(f'A multiplicação de {primeiro} e {segundo} é {primeiro * segundo}')
    if opção == 3:
        maior = primeiro
        maior = segundo
        if primeiro > maior:
            print(f'O maior número é {primeiro}')
        if segundo > maior:
            print(f'O maior número é {segundo}')
        if primeiro == segundo:
            print('Não tem número maior!')
    if opção == 4:
        print('Informe os números novamente.')
        primeiro = int(input('Primeiro número: '))
        segundo = int(input('Segundo número: '))
    sleep(1)
    print('-=' * 10, '\n')
    print('''            [ 1 ] Somar
            [ 2 ] Multiplicar
            [ 3 ] Maior
            [ 4 ] Novos números
            [ 5 ] Finalizar o programa''')
    opção = int(input('>>>>>> Qual a sua nova escolha? '))
print('Encerrando...\n', '-=' * 10)
sleep(2)