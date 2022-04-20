from os import system
from time import sleep


lista_inquilinos = []

class Inquilino(object):

    def __init__(self, codigo, nome, cpf, data_nascimento):
        self.codigo = codigo
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento

    def cadastro(self, codigo, nome, cpf, data_nascimento):
        codigo = input('Id: ')
        nome = input('Digite nome: ')
        cpf = input('Digite CPF: ')
        data_nascimento = input('Digite data nascimento: ')
        lista_inquilinos.append((codigo, nome, cpf, data_nascimento))
        system('cls')

    def listar(self, codigo, nome, cpf, data_nascimento):
        for inquilino in lista_inquilinos:
            codigo, nome, cpf, data_nascimento = inquilino
            print(f'| ID: {codigo} | Nome: {nome} | CPF: {cpf} | Data nascimento: {data_nascimento} |')
            
    def alterar(self, codigo, nome, cpf, data_nascimento):
        print('Qual inquilino deseja alterar? Digite o Id')
        id_inquilino = input('Id: ')
        for inquilino in lista_inquilinos:
            codigo, nome, cpf, data_nascimento = inquilino
            

            if codigo == id_inquilino:
                print(f'| ID: {codigo} | Nome: {nome} | CPF: {cpf} | Data nascimento: {data_nascimento} |')
                #remove_item(lista_inquilinos, nome, cpf, data_nascimento)
                del lista_inquilinos[0:4]
                nome = input('Digite nome: ')
                cpf = input('Digite cpf: ')
                data_nascimento = input('Digite data nascimento: ')
                lista_inquilinos.append((codigo, nome, cpf, data_nascimento))
                break                
        else:
            print(f'Inquilino com Id {id_inquilino} não foi encontrado')        