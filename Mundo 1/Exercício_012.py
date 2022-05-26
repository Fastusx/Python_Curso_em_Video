n = float(input('Valor do produto: '))
vdesc = int(input('Desconto: '))
desc = n - (n * vdesc / 100)
print(f'O produto que antes custava R${n}, agora com um desconto de {vdesc}%, ficará custando R${desc:.2f}')