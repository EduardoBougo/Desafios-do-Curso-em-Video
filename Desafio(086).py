Lista = [[], [], []]
n = 0
for a in range(1, 4):
    for b in range(1, 4):
        Lista[(a-1)].append(int(input(f'Digite um valor pa a posição [{a}, {b}]')))
print('=-='*20)
for l in Lista:
    print(f'[{Lista[n][0]:^5}][{Lista[n][1]:^5}][{Lista[n][2]:^5}]')
    n += 1



