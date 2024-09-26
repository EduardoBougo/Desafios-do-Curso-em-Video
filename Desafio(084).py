Lista = []
dados = []
cont = 's'
Pmaior = []
Pmenor = []
maiorpeso = menorpeso = 0
while cont in 'Ss':
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    Lista.append(dados[:])
    if len(Lista) == 1:
        menorpeso = maiorpeso = dados[1]
    else:
        if dados[1] > maiorpeso:
            maiorpeso = dados[1]
        elif dados[1] < menorpeso:
            menorpeso = dados[1]
    dados.clear()
    cont = str(input('quer continuar? [S/N] '))
for p in Lista:
    if p[1] == maiorpeso:
        Pmaior.append(p[0])
    elif p[1] == menorpeso:
        Pmenor.append(p[0])
print('=-='*20)
print(f'Ao todo você cadastrou {len(Lista)} pessoas.')
print(f'O maior peso foi {maiorpeso}Kg. Peso de {Pmaior}.')
print(f'O menor peso foi {menorpeso}Kg. Peso de {Pmenor}.')


