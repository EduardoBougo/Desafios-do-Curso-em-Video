def leiaDinheiro(txt):
    while True:
        valor_str = input(txt).strip()
        valor_str = valor_str.replace(',', '.')
        try:
            valor_float = float(valor_str)
            return valor_float
            break
        except:
            print(f'\033[0;31mERRO: "{valor_str}" é um preço invalido!\033[m')



