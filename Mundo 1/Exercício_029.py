n = float(input('Velocidade atual do carro: '))
if n > 80:
    multa = (n - 80) * 7
    print('\033[1;31mMULTADO!!! Você ultrapassou a velocidade limite de 80km/h')
    print(f'Você de deve pagar uma multa de\033[m \033[1;33mR${multa:.2f}!\033[m')
else:
    print(f'\033[1;92mSua velocidade atual é de {n}KM/H, muito bem!')
print('\033[1;92mTenha um bom dia! Dirija com segurança!\033[m')