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
    sleep(2)
    system('cls')

def listar_aluguel():
    for alug in lista_aluguel:
        print(f"| ID: {alug['ID']}", f"| Imóvel: {alug['Imóvel']}", f"| Inquilino: {alug['Inquilino']} |\n")

def excluir_aluguel():
  
    listar_aluguel()

    print('Digite o ID que deseja excluir')
    opcao = input('=> ')
    
    for alug in lista_imovel:
        
        if alug['ID'] == int(opcao):
            lista_aluguel.remove(alug)
            print('Cadastro excluído com sucesso!!!')
            sleep(2)
            system('cls')
            break
    else:
        system('cls')
        print('OPÇÃO INVÁLIDA, TENTA NOVAMENTE')
        sleep(3)
        system('cls')

def alterar_aluguel():
    
    listar_aluguel()

    print('Digite o ID que deseja atualizar.')
    opcao = input('=> ')
    
    for alug in lista_inquilinos:

        if alug['ID'] == int(opcao):
            print('\nListando imóveis cadastrados')
            listar_imovel()
            novo_idImovel = input('Digite ID do imóvel a ser alugado: ')
            alug['Imóvel'] = novo_idImovel

            print('\nListando inquilinos cadastrados')
            listar_inquilino()
            novo_idInquilino = input('Digite ID do Inquilino: ')
            alug['Inquilino'] = novo_idInquilino
                  
            print('\nCadastro atualizado com sucesso!!!')
            sleep(2)
            system('cls')
            break

    else:
        system('cls')
        print('\nOPCÃO INVÁLIDA, TENTA NOVAMENTE.')
        sleep(3)
        system('cls')