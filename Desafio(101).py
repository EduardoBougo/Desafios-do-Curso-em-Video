def voto(nasc):
    from datetime import datetime
    idade = datetime.now().year - nasc
    if 18 <= idade <= 65:
        v = 'VOTO OBRIGATÓRIO'
    if 16 <= idade <18 or idade >= 65:
        v = 'VOTO OPICIONAL'
    if idade <16:
        v = 'NÃO VOTA'
    print(f'Com {idade} anos: {v}')


voto(int(input('Em que ano você nasceu? ')))





