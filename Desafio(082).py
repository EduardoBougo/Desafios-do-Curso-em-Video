Lista = []
Par = []
Impar = []
continuar = 's'
while continuar in 'sS':
    Lista.append(int(input('Digite um valor: ')))
    continuar = input('Deseja continuar? [S/N]')
Lista.sort()
print('=-='*15)
print(f'A lista completa é {Lista}')
for c in range(0, len(Lista)):
    if Lista[c] % 2 == 0:
        Par.append(Lista[c])
    elif Lista[c] % 2 == 1:
        Impar.append(Lista[c])
print(f'A lista de Pares {Par}')
print(f'A lista de Impares {Impar}')



