# -*- coding: utf-8 -*

convites = 12
convites_ano_passado = 20

print convites
print convites_ano_passado

convites, convites_ano_passado = 11, 21

print convites
print convites_ano_passado
print convites, convites_ano_passado

convites = 50
salario = 7500.50
convites = 10L #long, tipo innteger
salario = 7500.50j #complex, tipo float

print type(convites_ano_passado)
print type(convites)
print type(salario)

perfil_aspas_duplas = "Vânia Almeida"

print perfil_aspas_duplas

perfil_aspas_simples = 'Flávio Almeida'

print perfil_aspas_simples

convite = 'Flavio Henrique de Souza Almeida'
primeiro_segundo_nome = convite[0:15]

print primeiro_segundo_nome

convite = 'Rayson Shall'
idade = 20

print type(idade)
print 'Convite do ' + convite
#print 'Convite do ' + convite + ' ' + idade + ' anos' nao converte int em str

print 'Convite do %s idade %s' % (convite, idade)

convite1 = 'Flavio Almeida'
convite2 = 'Nico Steappat'
convite3 = 'Rômulo Henrique'

convites = ['Flavio Almeida', 'Nico Steappat', 'Rômulo Henrique']

print convites
print convites[0]
print convites[2]
print convites[0:2]

convites.append('Vitor Marcos')

print convites

convites.append(10)

print convites

convites.remove(10) #remove pelo o conteudo e nao pelo o index

print convites

convites.remove('Rômulo Henrique')

print convites

tipos_convites = ['vip', 'normal', 'meia', 'cortesia']
tipos_convites.append('penetra')

print type(tipos_convites)
print tipos_convites

tipos_convites = ('vip', 'normal', 'meia', 'cortesia')

print type(tipos_convites)
print tipos_convites[0:2]

convites_com_valor = {'vip' : 60, 'normal' : 40, 'meia' : 30, 'cortesia' : 0}

print convites_com_valor

print convites_com_valor.keys()
print convites_com_valor.values()

status_civil = ('casado', 'solteiro') + ('divorciado',) ##cuidado, precisa ter a virgula após 'divorciado'

print status_civil
print type(status_civil)

print max([10, 5, 7])
print min((10, 5, 7))

nomes_tupla = ('Leonardo', 'Flávio', 'Rômulo')
nomes_lista = nomes = ['Leonardo', 'Flávio', 'Rômulo']

print sorted(nomes_tupla)
print sorted(nomes_lista)

print nomes_tupla

nomes_tupla = sorted(nomes_tupla)

print nomes_tupla

materias_com_peso = {'Equacoes Diofantinas' : 3, 'Algebra Relacional' : 2, 'Portugues instrumental' : 4}
pesos = list(materias_com_peso) #por padrao pega as keys

print type(materias_com_peso)
print pesos
print type(pesos)

pesos = tuple(materias_com_peso.values())

print pesos
print type(pesos)

convite = 'Romulo Henrique'

parte1 = convite[0:4]
parte2 = convite[11:15]

print '%s %s' % (parte1, parte2)

convite = 'Vania Almeida'

tamanho = len(convite)
parte1 = convite[0:4]
parte2 = convite[tamanho-4:tamanho]

print '%s %s' % (parte1, parte2)

def gera_nome_convite_1():
    convite = 'Flavio Henrique'
    posicao_final = len(convite)
    posicao_inicial = posicao_final - 4
    parte1 = convite[0:4]
    parte2 = convite[posicao_inicial:posicao_final]
    print '%s %s' % (parte1, parte2)

gera_nome_convite_1()

def gera_nome_convite(convite):
    posicao_final = len(convite)
    posicao_inicial = posicao_final - 4
    parte1 = convite[0:4]
    parte2 = convite[posicao_inicial:posicao_final]
    return parte1 + ' ' + parte2

codigo = gera_nome_convite('Erica Rodrigues')

print codigo

print 'O código gerado foi %s' % (codigo)


def gera_nome_convite3(nome):
	posicao_final = len(nome)
	posicao_inicial = posicao_final - 4
	parte1 = nome[0:4]
	parte2 = nome[posicao_inicial:posicao_final]
	return parte1 + ' ' + parte2

def envia_convite3(nome):
	print 'Enviando convite para %s'  % (nome)

nome = gera_nome_convite3('Doce gata')

envia_convite3(nome)

def processa_convite(nome):
    codigo = gera_nome_convite3(nome)
    envia_convite3(codigo)

processa_convite('Nao sei mais nomes')

nome = raw_input()

print nome

ano = raw_input()

print ano

# data = 2015 - ano aquianoé string nao vai dar certo tem que pasear

ano_como_inteiro = int (ano)

data = 2015 - ano_como_inteiro

print data

def cadastrar(nomes):
    print 'Digite um nome'
    nome = raw_input()
    nomes.append(nome)
    print nomes

nomes = []
cadastrar(nomes)

ano_como_str = raw_input()
ano = int (ano_como_str)
idade = 2016 - ano
print idade

from datetime import date

ano_como_string = raw_input()
ano = int(ano_como_string)
ano_atual = date.today().year
print ano_atual - ano

hoje  = date.today()

print hoje.year
print hoje.month
print hoje.day
print hoje.ctime()

numeros = [1, 2, 3]
numeros.remove(1) #remove o valor e nao o indice
print numeros

def remover(nomes):
    print 'Qual nome voce gostaria de remover?'
    nome = raw_input()
    nomes.remove(nome)
    print nomes

nomes = ['vania', 'erica', 'daniel', 'larissa', 'mac']
remover(nomes)


letra = raw_input('Digite uma letra: ')
if letra == 'a':
    print 'Ok, essa era a letra esperada'
else:
    print 'Hum, essa nao era a letra esperada'


frase = 'Eu amo Python'
print frase
if len(frase) > 10:
    if frase == 'Eu amo Python':
        print 'Eu também'
    else:
        print 'Ham?'
else:
    print 'Tamanho insuficiente'

frase = 'Python'
contador = 0
while contador < len(frase):
    print frase[contador]
    contador += 1
print 'Fim'