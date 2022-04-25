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
    for imov in lista_imovel:
        print(f"| ID: {imov['ID']}", f"| Logradouro: {imov['Logradouro']}", f"| CEP: {imov['Cep']}", f"| Bairro: {imov['Bairro']}", f"| Cidade: {imov['Cidade']}", f"| Proprietário: {imov['Proprietário']} |\n")

def excluir_imovel():
  
    listar_imovel()

    print('Digite o ID que deseja excluir')
    opcao = input('=> ')
    
    for imov in lista_imovel:
        
        if imov['ID'] == int(opcao):
            lista_imovel.remove(imov)
            print('Cadastro excluido com sucesso!!!')
            sleep(2)
            system('cls')
            break
    else:
        system('cls')
        print('OPÇÃO INVALIDA, TENTA NOVAMENTE')
        sleep(3)
        system('cls') 

# Falta desenvolver essa função
def alterar_imovel():
    pass
    