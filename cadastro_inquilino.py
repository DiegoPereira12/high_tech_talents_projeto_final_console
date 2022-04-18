lista = []

class Inquilino(object):

    def __init__(self, codigo, nome, data_nascimento):
        self.codigo = codigo
        self.nome = nome
        self.data_nascimento = data_nascimento
        

    def retorna_codigo(self: object):
        return self.codigo

    def cadastro(self, codigo, nome, data_nascimento):

        while codigo == contador:
            
            contador = contador + 1
            
        while nome == "":
            nome = input('Digite o nome: ')
        
        while data_nascimento == "":
            data_nascimento = input('Digite a data nascimento: ')

        inquilino = {"codigo": codigo, "Nome": nome, "Data nascimento": data_nascimento}
       
        lista.append(inquilino)
        print('Cadastro realizado')
    
    def listar():
        for item in lista:
            print(item)
    
    