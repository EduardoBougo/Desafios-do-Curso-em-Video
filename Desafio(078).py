Lista = list()
for numero in range(0, 5):
    n = int(input(f'Digite um valor para posição {numero}:'))
    Lista.append(n)
Ordem = Lista[:]
Lista.sort()
Maior = Lista[4]
Menor = Lista[0]
print(f'Os valores digitados foram {Ordem}')
print(f'O menor valor digitado foi {Lista[0]}, na posição {Ordem.index(Menor)} ')
print(f'O maoir valor digitado foi {Lista[4]}, na posição {Ordem.index(Maior)}')














