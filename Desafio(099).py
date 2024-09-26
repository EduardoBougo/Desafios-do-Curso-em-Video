from time import sleep
Lista = []
def maior(* num):
    cont = maiorv = 0
    print('-='*30)
    print('Analisando os valores passados....')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maiorv = valor
        else:
            if valor > maiorv:
                maiorv = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maiorv}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()



