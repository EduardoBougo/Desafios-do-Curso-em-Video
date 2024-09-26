c = [
    '\033[0;0m',#0 - reset
    '\033[42m',#1 - verde
    '\033[44m',#2 - azul
    '\033[7m',#3 - branco
    '\033[41m'#4 - vermelho
    ]
def título (txt, cor=0):
    tam = len(txt) + 4
    print(c[cor], end='')
    print('~'*tam)
    print(f'  {txt}')
    print('~' * tam)
    print(c[0], end='')
def HELP(txt, cor=0):
    título(f'Acessando o manual do comando \'{comando}\'', 2)
    print(c[cor], end='')
    print(help(txt))
    print(c[0], end='')


#programa príncipal
while True:
    título('SISTEMA DE AJUDA PyHELP', 1)
    comando = str(input('Função ou Biblioteca (Digite FIM para parar)> '))
    if comando.upper() == 'FIM':
        break
    else:
        HELP(comando, 3)
título('ATÉ LOGO!', 4)



