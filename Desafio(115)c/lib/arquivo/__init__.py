def cadastrar(arq, nome='<desconhecido>',idade='<desconhecida>', genero='<desconhecido>'):
    with open(arq, "a") as arquivo:
        arquivo.write(f"\n{nome:<25} - {idade:>3} anos - {genero:>3}")
    print(f'Novo registro de {nome} adicionado.')

def lerarquivo(txt):
    with open(f"{txt}", "rt") as arquivo:
        conteudo = arquivo.read()
    print(conteudo)

def arquivoExiste(arq):
    try:
        a = open(arq, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(arq):
    try:
        a = open(arq, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {arq} criado com sucesso!')



