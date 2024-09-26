Aproveitamento = {}
Dados = {}
total = 0
Lista = []
Dados['nome'] = str(input('Nome: '))
p = int(input(f'Quantas partidas {Dados["nome"]} jogou? '))
for j in range(1, (p+1)):
    Aproveitamento[f'partida {j}'] = int(input(f'Quantos gols na partida {j}? '))
    Lista.append(Aproveitamento[f'partida {j}'])
Dados['gols'] = Lista
for i in Aproveitamento.values():
    total += i
Dados['total'] = total
print('-='*30)
print(Dados)
print('-='*30)
for k, v in Dados.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {Dados["nome"]} jogou {p} partidas.')
for a, b in Aproveitamento.items():
    print(f'    => Na {a}, fez {b} gols. ')
print(f'    Foi um total de {Dados["total"]} gols.')
