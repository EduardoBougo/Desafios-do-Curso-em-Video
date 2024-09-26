# ERRO [se digitar ')' antes de abrir '(', está errada]
#v = input('Digite a expressão: ')
#expre = []
#for a in range(0, (len(v))):
#    if v[a] != ' ':
#        expre.append(v[a])
#if (v.count('(')) == (v.count(')')):
#    print('Sua expressão é valida.')
#else:
#    print('Sua expressão não é valida')

expressão = str(input('Digite a expressão: '))  # str / inserir numeros como se fossem letras não valores
pilha = []
for simbolo in expressão:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão é valida.')
else:
    print('Sua expressão está errada')



