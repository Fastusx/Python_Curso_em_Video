from urllib import request, error

try:
    site = request.urlopen(str(input('Digite uma URL: ')))
except error.URLError:
    print('O site não está acessível!')
else:
    print('O site está acessível!')
