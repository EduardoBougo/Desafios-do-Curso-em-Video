Lista = []
D = ('s')
while D == 's':
    Valor = (int(input('Digite um valor:')))
    if (Valor not in Lista):
        Lista.append(Valor)
        print('Valor adicionador com sucesso....')
    else:
        print('Valor duplicado! Não vou adicionar....')
    D = input('Deseja continuar?[S/N] ').lower()
Lista.sort()
print('=-='*15)
print(f'Os valores digitados foram:{Lista}')