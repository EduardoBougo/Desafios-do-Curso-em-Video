def vermelho(txt):
    print("\033[0;31m"+txt+"\033[0;0m")
def leiaint(txt):
    while True:
        n = str(input(f'{txt}'))
        n.strip()
        if n.isnumeric():
            valor = int(n)
            break
        vermelho('ERRO! Digite um número inteiro válido.')
    return valor


n =  leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')