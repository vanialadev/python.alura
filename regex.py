# -*- coding: UTF-8 -*-
import re

resultado = re.match('Py', 'Python')

print resultado

print resultado.group()

#resultado = re.match('py', 'Python') nao serve

resultado = re.match('[Pp]y', 'Python')

print resultado.group()

resultado = re.match('[A-Za-z]y', 'Python ou jython')

print resultado.group()

resultados = re.findall('[A-Za-z]y', 'Python ou jython')

print resultados

resultados = re.findall('[A-Za-z]y[A-Za-z]+', 'Python ou jython ou Pypy')

print resultados

resultados = re.findall('wy\w+', 'Python ou jython')

print resultados

resultados = re.findall('\wy\w+', 'Python ou jython ou Pypy')

print resultados

resultados = re.findall('\wy\w+\d', 'Python3 ou jython2 ou Pypy') #d é numero

print resultados

resultados = re.findall('[A-Za-z]+\d', 'Python3 ou jython2 ou Pypy') #termina com numero

print resultados

resultados = re.findall('[A-Za-z]+\d?', 'Python3 ou jython2 ou Pypy44') #tcomeca com letra e possui um numero ou nao

print resultados

#r'[A-Z]+' #raw string pra declarar expressoes regulares

resultados = re.findall('[fF]\w+', 'Joao Flavio Nico Fabiana')

print resultados

resultados = re.findall(r'[fF]\w{6}', 'Joao Flavio Nico Fabiana')

print resultados

resultados = re.findall(r'[fF]\w{6,20}', 'Joao Flavio Nico Fabiana')

print resultados

resultados = re.findall(r'[fF]\w{5,20}', 'Joao Flavio Nico Fabiana')

print resultados

resultado = re.match(r'^#', '#comentarios comecam com tralha') #procuramos pelo início através do caracter ^

print resultado.group()

resultado = re.match(r'.*br$', 'http://alura.com.br') #$ para buscar pelo final da string

print resultado.group()

resultados = re.findall(r'(\w+\d$)', 'rota66 88centavos Peer2Peer Python2')

print resultados

resultados = re.findall(r'(\w+\d\b)', 'rota66 88centavos Peer2Peer Python2')

print resultados

resultados = re.findall(r'(^\d\w+)', '88centavos Peer2Peer Python2 99taxi')

print resultados

resultados = re.findall(r'(\b\d\w+)', '88centavos Peer2Peer Python2 99taxi')

print resultados

regex_url = r'(.*/perfis/\d+/convidar$)'
existe = re.match(regex_url, 'http://django.com/perfis/123/convidar')
print existe is None

letras = ['B','R','A','S','I','L']
pais = '-'.join(letras) #join une todos os elementos da lista adicionando o caracter definido como junção
print pais

nomes = ['Fabio', 'Flavio','Nico']
nomes_concatenados = ''.join(nomes)
print  nomes_concatenados
