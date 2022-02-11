contp = 0
num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
tupla = num
tuplaa = tupla
print(f'Você digitou os valores {tupla}')
print(f"O algarismo 9(Nove) apareceu {tupla.count(9)}")
if 3 in tupla:
    print(f'O algarismo 3(Três) aparece pela primeira vez na {tupla.index(3) + 1}° posição')
else:
    print('Nessa tupla não o existe o algarismo 3')
for tuplaa in tupla:
    if tuplaa % 2 == 0:
        contp += 1
    else:
        continue
print(f'A tupla apresentou {contp} números pares')
