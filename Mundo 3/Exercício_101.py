def voto(ano):
    from datetime import datetime
    idade = datetime.now().year - ano
    if 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: voto OPCIONAL!'
    elif idade >= 18:
        return f'com {idade} anos: voto OBRIGATÓRIO'
    else:
        return f'Com {idade}: voto NEGADO'


ano = int(input('Qual o seu ano de nascimento? '))
voto(ano)





