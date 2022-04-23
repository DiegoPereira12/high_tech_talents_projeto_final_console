from time import sleep
from inquilino.cadastro_inquilino import *
from imovel.cadastro_imovel import *

lista_aluguel = []
id_aluguel = []

def cadastro_aluguel():
    
    id_inicial = ""

    if len(id_aluguel) == 0:
        id_inicial = 1
    else:
        id_inicial = len(id_aluguel) + 1
    
    print('\nListando imóveis cadastrados')
    listar_imovel()
    idImovel = input('Digite ID do imóvel a ser alugado: ')
    lista_aluguel.append    
     
    print('\nListando inquilinos cadastrados')
    listar_inquilino()
    idInquilino = input('Digite ID do Inquilino: ')
    lista_aluguel.append
    
    registro_aluguel = {
        'ID': id_inicial,
        'Imóvel': idImovel,
        'Inquilino': idInquilino
    }

    lista_aluguel.append(registro_aluguel)
    id_aluguel.append(id_inicial)
    print('\nCadastro realizado com Sucesso!!!')
    sleep(3)
    system('cls')

def listar_aluguel():
    for aluguel in lista_aluguel:
        print(f"| ID: {aluguel['ID']}", f"| Imóvel: {aluguel['Imóvel']}", f"| Inquilino: {aluguel['Inquilino']} |\n")