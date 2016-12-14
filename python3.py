# -*- coding: utf-8 -*
print ('Bem-vindo ao Python')
minha_idade = 25
print (minha_idade)
a, b = 10,20
print (a, b)
nome, idade = 'Vânia', 26
print (nome, idade)
oi,ola = 'Fábio',123456789
print (oi, ola)
nome,cpf,email = 'Fábio',123456789,'f@mail.com'
print ('%s %d %s' %(nome, idade, email))
nome, idade = 'Vânia Almeida', 26
print ('%s tem %d anos' % (nome, idade))
primeiro_nome = nome[0:5]
print (primeiro_nome)
parentes = []
nomes = ['Vânia Almeida', 'Erica Rodrigues', 'Doce']
print (nomes[0])
print (nomes[1])
print (nomes[2])
nomes.append('Flávio Almeida') #//acrescenta uma variavel
print (nomes)
nomes.append(10)
print (nomes)
nomes.remove(10)
print (nomes)
convites = ['Romulo', 'Almeida', 'Bronson', 'Nicodemos', 'Rubi']
print (convites[2:4])
variados = ['A', 'B', 12, 'F', 14]
variados.remove('B')
variados.append(15)
print (variados)
cortesias_com_valor = ('prima', 'seg', 'terc', 'quarta')  #nao aceita add outra coisa
print (cortesias_com_valor)
print (cortesias_com_valor[0])
cortesias_com_valor = {'prima' : 10, 'seg' : 20, 'terc' : 30, 'quarta' : 40}
print (cortesias_com_valor)
print (cortesias_com_valor.keys())
print (cortesias_com_valor.values())
print (cortesias_com_valor['prima'])

status_civil = ('casado', 'solteiro') + ('divorciado',)
print (status_civil)

print (type(status_civil))

nomes = ['Ana', 'Bruna', 'Carol'] + ['Dani', 'Ema']
print (nomes)

print (type(nomes))

print (('oi', 'como', 'vai', 'voce') + tuple(['e', 'aí', 'galera']))
print (list(('oi', 'como', 'vai', 'voce')) + ['e', 'aí', 'galera'])

print (max([10, 12, 50]))
print (min([10, 12, 50]))

nomes = ('rafa', 'ze', 'caio')
print (sorted(nomes))

materias_com_peso = {'Equações Diofantinas' : 3, 'Álgebra Relacional' : 2, 'Português instrumental' : 4}
pesos = tuple(materias_com_peso.values())
#pesos.append(1)
