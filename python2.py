# -*- coding: utf-8 -*
print ('Bem-vindo ao Python')
print 'Bem-vindo ao Python!'
minha_idade = 25
print minha_idade
a, b = 10,20
print a, b
nome, idade = 'Vania Almeida', 26
print nome, idade
print '%s tem %s anos' % (nome, idade)
primeiro_nome = nome[0:5]
print primeiro_nome
nome, idade = 'Vânia Almeida', 26
print nome, idade
primeiro_nome = nome[0:5]#acho que por causa do acento pega uma letra a mais
print primeiro_nome
primeiro_nome = nome[0:6]
print primeiro_nome
oi,ola = 'Fábio',123456789
print oi, ola
nome,cpf,email = 'Fábio',123456789,'f@mail.com'
print nome, idade, email
parentes = []
nomes = ['Vânia Almeida', 'Erica Rodrigues', 'Doce']
print nomes[0]
print nomes[1]
print nomes[2]
nomes.append('Flávio Almeida')
print nomes
nomes.append(10)
print nomes
nomes.remove(10)
print nomes

name = raw_input("Qual e o seu nome?")
quest = raw_input("Qual e sua missao?")
color = raw_input("Qual e sua cor favorita?")

print "Ah, entao seu nome e %s, sua missao e %s, " \
"e sua cor favorita e %s." % (name, quest, color)
