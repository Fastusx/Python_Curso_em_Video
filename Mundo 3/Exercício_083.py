mat = input('Digite a expressão: ')
lista = []
for simb in mat:
    if simb == '(':
        lista.append('(')
    elif simb == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Sua expressão é VÁLIDA!')
else:
    print('Sua expressão é INVÁLIDA!')
