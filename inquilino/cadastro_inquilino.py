from os import system
from time import sleep

lista_inquilinos = []
id_inquilino = []

def cadastro_inquilino():

    id_inicial = ""

    if len(id_inquilino) == 0:
        id_inicial = 1
    else:
        id_inicial = len(id_inquilino) + 1
    
    nome = input('Digite nome: ')
    cpf = input('Digite CPF: ')
    data_nascimento = input('Digite data nascimento: ')

    registro_inquilino = {
        'ID': id_inicial,
        'Nome': nome,
        'CPF': cpf,
        'Data de nascimento': data_nascimento
    }
    
    lista_inquilinos.append(registro_inquilino)
    id_inquilino.append(id_inicial)
    print('\nCadastro realizado com Sucesso!!!')
    sleep(2)
    system('cls')
    
def listar_inquilino():
    for inq in lista_inquilinos:
        print(f"| ID: {inq['ID']}", f"| Nome: {inq['Nome']}", f"| CPF: {inq['CPF']}", f"| Data nascimento: {inq['Data de nascimento']} |\n")   

def excluir_inquilino():
  
    listar_inquilino()

    print('Digite o ID que deseja excluir.')
    opcao = input('=> ')
    
    for inq in lista_inquilinos:
        
        if inq['ID'] == int(opcao):
            lista_inquilinos.remove(inq)
            print('Cadastro excluido com sucesso!!!')
            sleep(2)
            system('cls')
            break
    else:
        system('cls')
        print('OPÇÃO INVALIDA, TENTA NOVAMENTE.')
        sleep(3)
        system('cls')        

def alterar_inquilino():

    listar_inquilino()

    print('Digite o ID que deseja atualizar')
    opcao = input('=> ')
    
    for inq in lista_inquilinos:

        if inq['ID'] == int(opcao):
            novo_nome = input('Digite nome: ')
            inq['Nome'] = novo_nome
            novo_cpf = input('Digite CPF: ')
            inq['CpF'] = novo_cpf
            novo_data_nascimento = input('Digite data nascimento: ')
            inq['Data de nascimento'] = novo_data_nascimento

        print('\nCadastro atualizado com sucesso!!!')
        sleep(2)
        system('cls')
        break

    else:
        system('cls')
        print('\nOPCÃO INVALIDA, TENTA NOVAMENTE.')
        sleep(3)
        system('cls')