def notas(*nota, situação=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param nota: Uma ou mais notas dos alunos (aceita várias).
    :param situação: Valor opcional, indicando se deve ou não adicionar a situação.
    :return: Dicionário com várias informações sobre a situação da turma.
    """
    dic = {}
    t = soma = maior = menor = 0
    for n in nota:
        t += 1
        soma += n
        if t == 1:
            maior = menor = n
        else:
            if n > maior:
                maior = n
            if n < menor:
                menor = n
    média = soma / t
    dic['total'] = t
    dic['maior'] = maior
    dic['menor'] = menor
    dic['média'] = média
    if situação:
        if média < 6:
            dic['situação'] = 'RUIM'
        if média <= média <7:
            dic['situação'] = 'RAZOÁVEL'
        if média >= 7:
            dic['situação'] = 'BOA'
    return dic


resp = notas(10, 5, 7, 2, 3.7, situação=True)
print(resp)
