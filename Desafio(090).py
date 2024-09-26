dados = {}
dados['nome'] = str(input('Nome: '))
dados['média'] = float(input(f'Média de {dados["nome"]}'))
if dados['média'] >= 6:
    dados['situação'] = 'aprovado'
else:
    dados['situação'] = 'reprovado'
print('=-='*15)
for k, v in dados.items():
    print(f'{k} é igual a {v}')
