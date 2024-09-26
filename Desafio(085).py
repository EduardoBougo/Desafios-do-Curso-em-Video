Lista = [[], []]
for c in range(1,8):
    valor = int(input(f'Digite o {c}º valor:'))
    if valor % 2 == 1: #Impar
        Lista[0].append(valor)
    if valor % 2 == 0: #Par
        Lista[1].append(valor)
Lista[0].sort()
Lista[1].sort()
print('=-='*20)
print(f'Os valores Pares digitados foram {Lista[1]}')
print(f'Os valores Impares digitados foram {Lista[0]}')


