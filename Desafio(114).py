import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.request.URLError:
    print('O site pudim não está acessivel no momento.')
else:
    print('Consegui acessar o site Pudim com sucesso!')
    print('Dados do site: ')
    print(site.read())





