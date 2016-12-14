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


