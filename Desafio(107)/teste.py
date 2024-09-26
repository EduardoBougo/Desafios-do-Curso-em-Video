import Moeda
p = float(input('Digite o preço: R$'))
print(f'A metade de {p} é {Moeda.metade(p)}')
print(f'O dobro de {p} é {Moeda.dobro(p)}')
print(f'Aumentando 10%, temos {Moeda.aumentar(p, 10)}')
print(f'Reduzindo 13%, temo {Moeda.reduzir(p, 13)}')



