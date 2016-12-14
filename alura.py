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

