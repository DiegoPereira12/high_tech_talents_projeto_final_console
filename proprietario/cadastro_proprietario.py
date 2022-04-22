from os import system

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
        'CPF': cpf,
        'Nome': nome,
        'Data de nascimento': data_nascimento
    }
    
    lista_proprietarios.append(registro_proprietario)
    id_proprietario.append(id_inicial)
    system('cls')
    
def listar_proprietario():
    for proprieario in lista_proprietarios:
        print(f"| ID: {proprieario['ID']}", f"| Nome: {proprieario['Nome']}", f"| CPF: {proprieario['CPF']}", f"| Data nascimento: {proprieario['Data de nascimento']} |\n")