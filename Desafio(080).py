Lista = []
for c in range(0, 5):
    n = int(input('Digite um valor:'))
    if c == 0 or n > Lista[-1]: # Ultimo valor da lista
        Lista.append(n)
        print('Valor adicionado ao final da lista....')
    else:
        pos = 0
        while pos < len(Lista): #Enquanto pos for menor que o numero de itens na lista
            if n <= Lista[pos]:
                Lista.insert(pos, n)
                print(f'Valor adicionado na posição {pos} ')
                break
            pos += 1
print(f'Os valores digitados em ordem foram : {Lista}')
