def escreva(stri):
    tamanho = len(stri) + 4
    print('-' * tamanho)
    print(f'{stri.center(tamanho)}')
    print('-' * tamanho)


while True:
    palavra = input('Escreva qualquer palavra ou frase: ')
    escreva(stri=palavra)
    opcao = input('Quer continuar [S/N]? ').upper()
    if opcao in 'Nn':
        break
print('<<< Obrigado por testar!!! >>>')