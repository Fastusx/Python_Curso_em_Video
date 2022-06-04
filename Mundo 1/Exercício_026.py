nome = str(input('Digite uma frase: ')).upper().strip()
print(f'A letra "A" aparece {nome.count("A")} vezes na frase! ')
print(f'A primeira ocorrência da letra "A" na frase acontece na posição {nome.find("A") + 1}')
print(f'A última ocorrência da letra "A" na frase acontece na posição {nome.rfind("A") + 1}')
