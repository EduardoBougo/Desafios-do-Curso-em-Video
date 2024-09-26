from random import randint
Lista = []
m = 'JOGA NA MEGA SENA'
print('_'*20)
print(f'{m:^20}')
print('_'*20)
jogos = int(input('Quantos jogos você quer que eu sorteie? '))
print('-='*3, f'SORTEANDO {jogos} JOGOS', '-='*3)
for j in range(0, jogos):
    n = 0
    while n < 6:
        v = randint(1, 61)
        if v not in Lista:
            Lista.append(v)
            n += 1
    Lista.sort()
    print(f'Jogo {j+1}: {Lista}')
    Lista.clear()
print('-='*5, '<BOA SORTE>', '-='*5)