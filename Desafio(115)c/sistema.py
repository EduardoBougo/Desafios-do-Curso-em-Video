from lib.interface import *
from lib.arquivo import *

arq = "cursoemvideo.txt"
if not arquivoExiste(arq):
    criarArquivo(arq)


while True:
    resp = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resp == 1:
        cabeçalho('PESSOAS CADASTRADAS')
        lerarquivo(arq)
    elif resp == 2:
        cabeçalho('CADASTRO')
        nome = str(input('Nome:')).strip()
        idade = leiaint('Idade: ')
        genero = str(input('Gênero [M/F]')).upper().strip()
        cadastrar(arq=arq, nome=nome, idade=idade, genero=genero)
        cabeçalho('CADASTRADO COM SUCESSO')

    elif resp == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print(f'\033[31mERRO! Digite uma opção válida\033[0m')



