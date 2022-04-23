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
        'CPF': cpf,
        'Nome': nome,
        'Data de nascimento': data_nascimento
    }
    
    lista_inquilinos.append(registro_inquilino)
    id_inquilino.append(id_inicial)
    print('\nCadastro realizado com Sucesso!!!')
    sleep(3)
    system('cls')
    
def listar_inquilino():
    for inquilino in lista_inquilinos:
        print(f"| ID: {inquilino['ID']}", f"| Nome: {inquilino['Nome']}", f"| CPF: {inquilino['CPF']}", f"| Data nascimento: {inquilino['Data de nascimento']} |\n")   

def alterar_inquilino():
    print('Qual inquilino deseja alterar? Digite o Id')
    id_inquilino = input('Id: ')

    if id_inquilino == 0:
        print('Não consta inquilino cadastrado com o Id informado')
    else:
        listar_inquilino()

        nome_1 = input('Digite nome: ')   
        cpf_1 = input('Digite cpf: ')
        data_nascimento_1 = input('Digite da nascimento: ')

        pass