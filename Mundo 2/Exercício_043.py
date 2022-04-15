print('''Informe o seu gênero
\033[1;31m[1] Masculino
[2] Feminino\033[m''')
gênero = int(input('Escolha uma opção: '))
peso = float(input('Informe o seu peso(kg): '))
altura = float(input('Informe sua altura(m): '))
IMC = float(peso / (altura ** 2))
print(f'Com um IMC (Índice de Massa Corporal) de {IMC :.1f}')
if gênero == 2 and IMC < 19.1:
    print('Você está abaixo do peso ideal!')
elif gênero == 2 and IMC < 25.8:
    print('Você está no peso ideal!')
elif gênero == 2 and IMC < 27.3:
    print('você está com Sobrepeso!')
elif gênero == 2 and IMC < 32.3:
    print('Você está com Obesidade!')
elif gênero == 2 and IMC > 32.3:
    print('Você está com Obesidade Mórbida')
elif gênero == 1 and IMC < 20.7:
    print('Você está abaixo do peso ideal!')
elif gênero == 1 and IMC < 26.4:
    print('Você está no peso ideal!')
elif gênero == 1 and IMC < 27.8:
    print('você está com Sobrepeso!')
elif gênero == 1 and IMC < 31.1:
    print('Você está com Obesidade!')
elif gênero == 1 and IMC > 31.1:
    print('Você está com Obesidade Mórbida')

