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
    
    idImovel = input('Digite ID do Imovel: ')
    for idImovel in listar_imovel():
        print(idImovel)
        lista_aluguel.append      
    else:
        print('Não consta Imóvel cadastrado com este ID')

    idInquilino = input('Digite ID do Inquilino: ')
    for idInquilino in listar_inquilino():
        lista_aluguel.append
        print(idInquilino)
        lista_aluguel.append
    else:
        print('Não consta Inquilino cadastrado com este ID')

    registro_aluguel = {
        'ID': id_inicial,
        'ID Imóvel': id_aluguel,
        'ID Inquilino': id_aluguel
    }

    lista_aluguel.append(registro_aluguel)
    id_aluguel.append(id_inicial)
    system('cls')