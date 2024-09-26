from time import sleep
from random import randint
from operator import itemgetter
Ranking = []
dado = {}
n = 1
print('Valores soteados:')
dado = {'Jodador 1': randint(0, 6),
'Jodador 2': randint(0, 6),
'Jodador 3': randint(0, 6),
'Jodador 4': randint(0, 6)}
for k, v in dado.items():
    print(f'{k} tirou {v} no dado.')
Ranking = sorted(dado.items(), key=itemgetter(1), reverse=True)
print('=-='*20)
print('== RANKING DOS JOGADORES ==')
for k, v in enumerate(Ranking):
    print(f'{n}º Lugar: {v[0]} com {k}')
    n += 1


