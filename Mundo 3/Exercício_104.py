def leiaint(n):
    n = input(n)
    while True:
        if n.isdigit():
            return n
        else:
            n = input('ERRO! Digite um número vádido: ')


a = leiaint('Digite um número: ')
print(f'O número que você digitou foi {a}.')
