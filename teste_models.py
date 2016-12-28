# -*- coding: UTF-8 -*-

from models import Perfil
from models import Data
from models import Pessoa

perfil1_nome = 'Flavio Almeida'
perfil1_telefone = 'nao informado'
perfil1_empresa = 'Caelum'

perfil2_nome = 'Nico Steppat'
perfil2_telefone = 'segredo'
perfil2_empresa = 'Caelum'

print perfil1_empresa
print  perfil2_empresa

print 'Nome %s, telefone %s, empresa %s' % (perfil1_nome, perfil1_telefone, perfil1_empresa)
print 'Nome %s, telefone %s, empresa %s' % (perfil2_nome, perfil2_telefone, perfil2_empresa)


perfil = {'nome' : 'Flavio Almeida', 'telefone' : 'nao informado', 'empresa' : 'Caelum'}

print perfil
print perfil.keys()
print perfil.values()
print perfil['nome']
print perfil['empresa']
print perfil.has_key('telefone')

perfil = Perfil('Vania', 'segredo', 'Alura')

print perfil.empresa
print perfil.nome

perfil.nome = 'Vânia Almeida'

print perfil.nome

perfil.imprimir()


perfil2 = Perfil(empresa='Caelum', nome='Flavio', telefone='nao informado')

perfil2.imprimir()

print type(perfil) # no oldstyle sai <type 'instance'>, no novo sai diferente. Usar o novo

print perfil.__class__ # no oldstyle sai models.Perfil

perfil2 = Perfil('Steve', '2121-2121', 'Minecraft')

perfil3 = Perfil('Peter', '3333-4444', 'Minecraft')

outro = perfil2

print outro.nome

outro.nome = 'Steven'

print perfil2.nome

d = Data(21,11,2016)

d.imprime()

pessoa = Pessoa('Ronaldo', 105, 1.78)
pessoa.imprime_imc()