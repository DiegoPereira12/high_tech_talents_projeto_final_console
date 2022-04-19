from os import system
from unicodedata import name
from xml.dom.minidom import Element


lista_inquilinos = []

class Inquilino(object):

    def __init__(self, codigo, nome, data_nascimento):
        self.codigo = codigo
        self.nome = nome
        self.data_nascimento = data_nascimento

    def cadastro(self, codigo, nome, data_nascimento):
        codigo = input('Id: ')
        nome = input('Digite nome: ')
        data_nascimento = input('Digite data nascimento: ')
        lista_inquilinos.append((codigo, nome, data_nascimento))
        system('cls')

    def listar(self, codigo, nome, data_nascimento):
        for inquilino in lista_inquilinos:
            codigo, nome, data_nascimento = inquilino
            print(f'| ID: {codigo} | Nome: {nome} | Data nascimento: {data_nascimento} |')
            

    def alterar(self, codigo, nome, data_nascimento):
        print('Qual inquilino deseja alterar? Digite o Id')
        id_inquilino = input('Id: ')
        for inquilino in lista_inquilinos:
            codigo, nome, data_nascimento = inquilino

            if codigo == id_inquilino:
                print(f'| ID: {codigo} | Nome: {nome} | Data nascimento: {data_nascimento} |')
                # remove
                
                nome = input('Digite nome: ')
                data_nascimento = input('Digite data nascimento: ')
                lista_inquilinos.append((codigo, nome, data_nascimento))
                break
                
        else:
            print(f'Inquilino com Id {id_inquilino} não foi encontrado')        