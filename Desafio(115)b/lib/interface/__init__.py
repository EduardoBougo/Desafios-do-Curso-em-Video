def linha(tam=42):
    return '-'*tam

def leiaint(msg):
    while True:
        try:
            n=int(input(msg))
        except(ValueError, TypeError):
            print('\033[31mERRO: porfavor, insira um número inteiro valido.\033[0m')
            continue
        except(KeyboardInterrupt):
            print('\033[31mUsuário preferiu não informar esse valor.\033[0m')
            return 0
        else:
            return n

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabeçalho('MENU PRINCIPAL'.center(42))
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[0m - \033[34m{item}\033[0m')
        c += 1
    print(linha())
    opc = leiaint(f'\033[32mSua Opção:\033[0m')
    return opc


