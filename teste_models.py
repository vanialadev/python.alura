# -*- coding: UTF-8 -*-

from models import Perfil
from models import Data
from models import Pessoa
from models import Retangulo
from models import Perfil_Vip
from models import Conta
from models import Conta_Corrente

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

perfil.curtir()
perfil.curtir()

print perfil.obter_curtidas()


ret = Retangulo(2,3)
print ret.obter_area()
ret._Retangulo__area = 10
print ret._Retangulo__area

perfil._Perfil__curtidas = 9999999
print perfil._Perfil__curtidas

print perfil.obter_curtidas()

perfil.imprimir()

perfil_vip = Perfil_Vip('Vania Almeida', 'nao informado', 'Alura', 'vaniala')

print perfil_vip.apelido

perfil_vip.curtir()
perfil_vip.curtir()
print perfil_vip.obter_curtidas()
print perfil_vip.obter_creditos()

conta_corrente  = Conta_Corrente('Leonardo', 2000, 50)

print conta_corrente.calcular_imposto()

arquivo = open('perfis.csv', 'r')

linha = arquivo.readline()
print linha

for linha in arquivo:
    print linha

arquivo.close()

# arquivo = open('novos_perfis.csv', 'w')
#
# arquivo.write('Pedro Gomes, 85-55555555, Gomes e Amigos \n')
#
# arquivo.close()

#arquivo = open('novos_perfis', 'r')

#print arquivo.readline()
#arquivo.close()

arquivo = open('teste.txt', 'a')
arquivo.write('Python rocks \n')

print arquivo.mode
arquivo.close()

"""
logo = open('python-logo.png', 'rb')
data = logo.read()
logo.close()

logo2= open('python-logo2.png', 'wb')
logo2.write(data)
logo2.close()
"""

perfis = Perfil_Vip.gerar_perfis('perfis.csv')
print type(perfis[0])

for perfil in perfis:
    perfil.imprimir()
perfil = Perfil_Vip('Joao','2222222','Caelum')
print 'teste %s' % perfil.apelido

try:
    arquivo = open('arquivo_nao_existe.txt', 'r')
    valores = arquivo.readline(',')
    Perfil(*valores)
    print 'arquivo foi aberto'
    arquivo.close()
except IOError as erro:
    print 'Erro de IO %s' % erro
except TypeError as erro:
    print 'TypeErro %s' % erro

try:
    arquivo = open('novos_perfis.csv', 'r')
    valores = arquivo.readline(';')
    Perfil(*valores)
    print 'arquivo foi aberto'
    arquivo.close()
except IOError as erro:
    print 'Erro de IO %s' % erro
except TypeError as erro:
    print 'TypeErro %s' % erro
except Exception as erro:
    print 'Exception %s' % erro

arquivo = None
try:
    arquivo = open('perfis.csv', 'r')
    valores = arquivo.readline().split(':')
    Perfil(*valores)
    print 'arquivo foi aberto'
  #  arquivo.close()
except (IOError, TypeError, StandardError) as erro:
    print 'DEu erro %s' % erro
finally:
    if arquivo is not None:
        print 'fechando arquivo'
        arquivo.close()

try:
    with open('perfis.csv', 'r') as arquivo:
        for linha in arquivo:
            print linha
except Exception as erro:
    print 'Exception %s' % erro


perfis = Perfil.gerar_perfis('novos_perfis.csv')