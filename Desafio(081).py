Lista = []
continuar = 's'
while continuar == 's':
    Lista.append(int(input('Digite um valor: ')))
    continuar = input('Deseja continuar? [S/N]').lower()
print('=-='*15)
print(f'Foram digitados {len(Lista)} números')
Lista.sort(reverse=True)
print(f'A lista em ordem decresente : {Lista}')
if 5 in Lista:
    print(f'O valor 5 está na lista na posição {Lista.index(5)}')
else:
    print('O valor 5 não foi digitado.')







