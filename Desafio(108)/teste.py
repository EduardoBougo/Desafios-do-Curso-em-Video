import Moeda
p = float(input('Digite o preço: R$'))
print(f'A metade de {Moeda.moeda(p)} é {Moeda.moeda(Moeda.metade(p))}')
print(f'O dobro de {Moeda.moeda(p)} é {Moeda.moeda(Moeda.dobro(p))}')
print(f'Aumentando 10%, temos {Moeda.moeda(Moeda.aumentar(p, 10))}')
print(f'Reduzindo 13%, temo {Moeda.moeda(Moeda.reduzir(p, 13))}')



