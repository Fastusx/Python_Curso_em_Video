def leiadinheiro(num):
    valido = False
    while not valido:
        entrada = str(input(num)).strip().replace(',', '.')
        if entrada.isalpha():
            print('Erro! Valor inv�lido')
        else:
            valido = True
            return float(entrada)
