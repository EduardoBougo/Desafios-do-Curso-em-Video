Lista = []
Dados = {}
soma = média = 0
c = ['n', 'nao', 'não', 's', 'sim']
r = ['n', 'nao', 'não']
while True:
    Dados['nome'] = str(input('Nome: '))
    while True:
        sexo = str(input('Sexo [M/F]: ')).upper()
        if sexo in 'MF':
            break
        print('ERRO! Responda apenas M ou F.')
    Dados['sexo'] = sexo
    Dados['idade'] = int(input('Idade: '))
    soma += Dados['idade']
    Lista.append(Dados.copy())
    Dados.clear()
    while True:
        cont = str(input('Quer continuar? [S/N] ')).lower()
        if cont in c:
            break
        print('ERRO! Responda apenas S ou N.')
    if cont in r:
        break
print('-='*30)
print(f'A) Ao todo temos {len(Lista)} pessoas cadastradas.')
média = soma / len(Lista)
print(f'B) A média de idade é de {média} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for p in Lista:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print()
print(f'D) Lista de pessoas que estão acima da média :')
for p in Lista:
    if p['idade'] >= média:
        print('     ', end='')
        for k, v in p.items():
            print(f'{k} = {v}   ', end='')
        print()
print('<<ENCERRADO>>')