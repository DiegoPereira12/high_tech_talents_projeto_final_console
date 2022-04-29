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
            print('Cadastro excluído com sucesso!!!')
            sleep(2)
            system('cls')
            break
    else:
        system('cls')
        print('OPÇÃO INVÁLIDA, TENTA NOVAMENTE')
        sleep(3)
        system('cls')  
    
def alterar_proprietario():
    
    listar_proprietario()
    
    print('Digite o ID que deseja atualizar.')
    opcao = input('=> ')

    for prop in lista_proprietarios:

        if prop['ID'] == int(opcao):
            novo_nome = input('Digite nome: ')
            prop['Nome'] = novo_nome
            novo_cpf = input('Digite CPF: ')
            prop['CPF'] = novo_cpf
            novo_data_nascimento = input('Digite data nascimento: ')
            prop['Data de nascimento'] = novo_data_nascimento

            print('\nCadastro atualizado com sucesso!!!')
            sleep(2)
            system('cls')
            break

    else:
        system('cls')
        print('\nOPCÃO INVÁLIDA, TENTA NOVAMENTE.')
        sleep(3)
        system('cls')        
    
        
        



