from datetime import datetime
Cadastro = {}
Cadastro['nome'] = str(input('Nome: '))
nasc = int(input('Data de nascimento: '))
Cadastro['gênero'] = str(input('Gênero [M/F]: ')).upper()
Cadastro['idade'] = datetime.now().year - nasc
Cadastro['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if Cadastro['ctps'] != 0:
    Cadastro['contratação'] = int(input('Ano de contratação: '))
    Cadastro['salário'] = float(input('Salário: '))
    Cadastro['aposentadoria'] = Cadastro['idade'] + Cadastro['contratação'] + 35 -datetime.now().year

print('=-='*30)
for k, v in Cadastro.items():
    print(f'  - {k} tem valor {v}')



