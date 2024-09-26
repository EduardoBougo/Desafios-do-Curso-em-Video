Time = []
Dados = {}
gols = []
Aproveitamento = {}
n = 1
continuar = ['n', 'nao', 'não', 's', 'sim']
c = ['n', 'nao', 'não']
while True:
    Dados.clear()
    gols.clear()
    Aproveitamento.clear()
    totalg = 0
    Dados['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {Dados["nome"]} jogou? '))
    for p in range(1, partidas+1):
        Aproveitamento[f'partida {p}'] = int(input(f'Quantos gols na partida {p}? '))
        gols.append(Aproveitamento[f'partida {p}'])
    for g in Aproveitamento.values():
        totalg += g
    Dados['gols'] = gols.copy()
    Dados['total'] = totalg
    Time.append(Dados.copy())
    while True:
        cont = str(input('Quer continuar? [S/N] ')).lower()
        if cont in continuar:
            break
        print('ERRO! Responda apenas S ou N.')
    if cont in c:
        break
print('-='*30)
print(f'Nº NOME           GOLS           TOTAL')#38
print('-'*38)
for k, v in enumerate(Time):
    print(f'{k+1:<2} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*38)
while True:
    b =  int(input('Mostrar dados de qual jogador? (999 interrompe)'))
    if b == 999:
        break
    print(f' -- LEVANTAMENTO DO JOGADOR {Time[b-1]["nome"]}:')
    for i in Time[b-1]["gols"]:
        print(f'No jogo {n} fez {i} gols.')
        n += 1
