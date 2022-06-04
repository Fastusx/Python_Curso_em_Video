n = int(input('\033[1;92mDigite um número qualquer: \033[m'))
if n % 2 == 0:
    print(f'\033[1;34m{n} é um número PAR!\033[m')
else:
    print(f'\033[1;31m{n} é um número ÍMPAR!\033[m')