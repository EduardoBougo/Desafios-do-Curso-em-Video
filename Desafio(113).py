def vermelho(txt):
    print("\033[0;31m"+txt+"\033[0;0m")
def leiaint():
    while True:
        try:
            num = int(input('Digite um número inteiro: '))
        except:
            vermelho('ERRO: Porfavor, digite um número inteiro válido.')
        else:
            return num
            break
def leiafloat():
    while True:
        valor_str = input('Digite um número real: ').strip().replace(',', '.')
        try:
            valor_float = float(valor_str)
        except:
            vermelho('ERRO: Porfavor, digite um número inteiro válido.')
        else:
            return valor_float
            break


print(f'O valor inteiro digitado foi {leiaint()} e o real foi {leiafloat()} ')