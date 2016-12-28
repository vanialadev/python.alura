# -*- coding: UTF-8 -*-

class Perfil(object):
    'Classe padrão para perfis de usuários'

    def __init__(self, nome, telefone, empresa):
        self.nome = nome
        self.telefone = telefone
        self.empresa = empresa

    def imprimir(self):
        print 'Nome: %s, Telefone: %s, Empresa: %s' % (self.nome, self.telefone, self.empresa)


class Data(object):
    'Classe padrao para data'

    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def imprime(self):
        print '%d/%d/%d' % (self.dia, self.mes, self.ano)


class Pessoa(object):
    'Classe padrão para pessoa'

    def __init__(self, nome, peso, altura):
        self.nome = nome
        self.peso = peso
        self.altura = altura

    def imprime(self):
        imc =self.peso / (self.altura ** 2)
        print 'O IMC de %s é: %s ' % (self.nome, imc)

    def calcula_imc(self):
        imc = self.peso / (self.altura ** 2)
        return imc

    def imprime_imc(self):
        print 'Imc de %s é: %.2f' % (self.nome, self.calcula_imc())
