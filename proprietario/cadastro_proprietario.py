from os import system
from time import sleep

lista_proprietarios = []
id_proprietario = []

def cadastro_properietario():

    id_inicial = ""

    if len(id_proprietario) == 0:
        id_inicial = 1
    else:
        id_inicial = len(id_proprietario) + 1
    
    nome = input('Digite nome: ')
    cpf = input('Digite CPF: ')
    data_nascimento = input('Digite data nascimento: ')

    registro_proprietario = {
        'ID': id_inicial,
        'Nome': nome,
        'CPF': cpf,    
        'Data de nascimento': data_nascimento
    }
    
    lista_proprietarios.append(registro_proprietario)
    id_proprietario.append(id_inicial)
    print('\nCadastro realizado com Sucesso!!!')
    sleep(2)
    system('cls')
    
def listar_proprietario():

    for prop in lista_proprietarios:
        print(f"| ID: {prop['ID']}", f"| Nome: {prop['Nome']}", f"| CPF: {prop['CPF']}", f"| Data nascimento: {prop['Data de nascimento']} |\n")

def excluir_proprietario():
  
    listar_proprietario()

    print('Digite o ID que deseja excluir')
    opcao = input('=> ')
    
    for prop in lista_proprietarios:
        
        if prop['ID'] == int(opcao):
            lista_proprietarios.remove(prop)
            print('Cadastro excluido com sucesso!!!')
            sleep(2)
            system('cls')
            break
    else:
        system('cls')
        print('OPÇÃO INVALIDA, TENTA NOVAMENTE')
        sleep(3)
        system('cls')  
    
    
    
        
        



