# -*- coding: UTF-8 -*-

class Perfil(object):
    'Classe padrão para perfis de usuários'

    def __init__(self, nome, telefone, empresa):
        if len(nome) < 3:
            raise ArgumentoInvalidoError('Nome deve ter pelo menos 3 caracteres')
        self.nome = nome
        self.telefone = telefone
        self.empresa = empresa
        self.__curtidas = 0

    def imprimir(self):
        print 'Nome: %s, Telefone: %s, Empresa: %s, Curtidas %d' % (self.nome, self.telefone, self.empresa, self.__curtidas)

    def curtir(self):
        self.__curtidas += 1

    def obter_curtidas(self):
        return self.__curtidas

    @classmethod
    def gerar_perfis(cls, nome_arquivo):
        arquivo = open(nome_arquivo, 'r')
        perfis = []
        for linha in arquivo:
            valores = linha.split(',')
            if len(valores) is not 3:
                # raise ValueError('Uma linha no arquivo %s deve ter 3 valores' % nome_arquivo)
                raise ArgumentoInvalidoError('Uma linha no arquivo %s deve ter 3 valores' % nome_arquivo)
            perfis.append(cls(*valores))
        arquivo.close
        return perfis

class Perfil_Vip(Perfil):
    'Classe padrão para perfis de usuários vips'

    def __init__(self, nome, telefone, empresa, apelido=''):
        super(Perfil_Vip, self).__init__(nome, telefone, empresa)
        self.apelido = apelido

    def obter_creditos(self):
        return super(Perfil_Vip, self).obter_curtidas() * 10.0

class ArgumentoInvalidoError(Exception):

    def __init__(self, mensagem):
        self.mensagem = mensagem

    def __str__(self):
        return repr(self.mensagem)

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


class Retangulo(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.__area = x * y

    def obter_area(self):
        return self.__area


class Conta(object):

    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def calcular_imposto(self):
        self.saldo *= 0.1
        return self.saldo


class Conta_Corrente(Conta):

    def __init__(self, titular, saldo, bonus): # se a construtor for igual ao pai nao declara na filha
        super(Conta_Corrente, self).__init__(titular, saldo)
        self.bonus = bonus

    def calcular_imposto(self):
        return super(Conta_Corrente, self).calcular_imposto() + self.bonus


