Boletim = []
cont = 's'
dado = []
n = 1
while cont in 'sS':
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Nota1: ')))
    dado.append(float(input('Nota2: ')))
    Boletim.append(dado[:])
    dado.clear()
    cont = str(input('Quer continuar? [S/N] '))
print('='*40)
print('Nº  NOME         MÉDIA')#22
print('-'*25)
for aluno in Boletim:
    media = (aluno[1] + aluno[2]) / 2
    print(f'{n:<4}{aluno[0]:<13}{media}')
    n += 1
print('-'*25)
while True:
    v = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if v == 999:
        break
    else:
        print(f'Notas de {Boletim[(v-1)][0]} são {Boletim[v-1][1], Boletim[v-1][2]}')


print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')