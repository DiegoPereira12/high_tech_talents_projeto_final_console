lista = []

class Inquilino(object):

    ID = 0

    def __init__(self, nome, data_nascimento):
        self.codigo = Inquilino.ID
        self.nome = nome
        self.data_nascimento = data_nascimento
        Inquilino.id += 1

    def retorna_codigo(self: object):
        return self.codigo

    def cadastro(self, ID, nome, data_nascimento):
        while nome == "":
            nome = input('Digite o nome: ')
        
        while data_nascimento == "":
            data_nascimento = input('Digite a data nascimento: ')

        inquilino = {"ID": ID,"Nome": nome, "Data nascimento": data_nascimento}
        lista.append(inquilino)
        print('Cadastro realizado')
    
    def listar():
        for item in lista:
            print(item)
    
    