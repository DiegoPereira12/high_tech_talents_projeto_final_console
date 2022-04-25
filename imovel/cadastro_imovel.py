from os import system
from time import sleep

lista_imovel = []
id_imovel = []

def cadastro_imovel():

    id_inicial = ""

    if len(id_imovel) == 0:
        id_inicial = 1
    else:
        id_inicial = len(id_imovel) + 1
    
    logradouro = input('Digite logradouro: ')
    cep = input('Digite CEP: ')
    bairro = input('Digite bairro: ')
    cidade = input('Digite cidade: ')
    proprietario = input('Digite proprietario: ')

    registro_imovel = {
        'ID': id_inicial,
        'Logradouro': logradouro,
        'Cep': cep,
        'Bairro': bairro,
        'Cidade': cidade,
        'Proprietário': proprietario
    }
    
    lista_imovel.append(registro_imovel)
    id_imovel.append(id_inicial)
    print('\nCadastro realizado com Sucesso!!!')
    sleep(2)
    system('cls')

def listar_imovel():
    for imovel in lista_imovel:
        print(f"| ID: {imovel['ID']}", f"| Logradouro: {imovel['Logradouro']}", f"| CEP: {imovel['Cep']}", f"| Bairro: {imovel['Bairro']}", f"| Cidade: {imovel['Cidade']}", f"| Proprietário: {imovel['Proprietário']} |\n")
