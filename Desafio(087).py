Lista = [[], [], []]
n = pares = soma3 = linha2 = 0
for a in range(1, 4):
    for b in range(1, 4):
        Lista[(a-1)].append(int(input(f'Digite um valor pa a posição [{a}, {b}]')))
print('=-='*20)
for l in Lista:
    print(f'[{Lista[n][0]:^5}][{Lista[n][1]:^5}][{Lista[n][2]:^5}]')
    n += 1
print('=-='*20)
for c in range(0, 3):
    for d in range(0, 3):
        if Lista[c][d] % 2 == 0:
            pares += Lista[c][d]
print(f'A soma dos valores pares é {pares}')
for linha in Lista:
    soma3 += linha[2]
print(f'A soma dos valores da terceira coluna é {soma3}')
for va in Lista[1]:
    if linha2 == 0:
        linha2 = va
    if va > linha2:
        linha2 = va
print(f'O maior valor da segunda linha é {linha2}')

