from random import randint
from time import sleep
Lista = []
def sortear():
    print(f'Sorteando 5 valores da lista: ', end='')
    for n in range(0, 5):
        Lista.append(randint(0, 9))
        print(f'{Lista[n]} ', end='', flush=True)
        sleep(0.3)
    print('PRONTO!')
def somaPar():
    soma = 0
    for i in Lista:
        if i % 2 == 0:
            soma += i
    print(f'Somando os valores pares de {Lista}, temos {soma}')

sortear()
somaPar()







