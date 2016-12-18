# -*- coding: UTF-8 -*-

def cadastrar(nomes):
    print 'Digite um nome'
    nome = raw_input()
    nomes.append(nome)

def listar(nomes):
    print 'Listando nomes:'
    for nome in nomes:
        print nome


def remover(nomes):
    print 'Qual nome você gostaria de remover?'
    nome = raw_input()
    nomes.remove(nome)


def alterar(nomes):
    print 'Qual nome você gostaria de alterar?'
    nome = raw_input()
    if nome in nomes:
        print 'Digite novo nome'
        novo_nome = raw_input()
        index = nomes.index(nome)
        nomes[index] = novo_nome


def procurar(nomes):
    print 'Digite um nome a procurar'
    nome = raw_input()
    if nome in nomes:
        print 'Nome %s está cadastrado' % (nome)
    else:
        print 'Nome %s não está cadastrado' % (nome)


def menu():
    nomes = []
    escolha = ''
    while(escolha != '0'):
        print 'Digite 1 para cadastrar, 0 para terminar'
        escolha = raw_input()

        if(escolha == '1'):
            cadastrar(nomes)

        elif(escolha == '2'):
            listar(nomes)

        elif escolha == '3':
            remover(nomes)

        elif escolha == '4':
            alterar(nomes)

        elif escolha == '5':
            procurar(nomes)
menu()