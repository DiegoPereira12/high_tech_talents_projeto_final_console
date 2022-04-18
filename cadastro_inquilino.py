lista = []

class Inquilino(object):

    

    def __init__(self,nome, data_nascimento):
        
        self.nome = nome
        self.data_nascimento = data_nascimento
        
        
    def cadastro(self, nome, data_nascimento):

      

        while nome == "":
            nome = input('Digite o nome: ')
        
        while data_nascimento == "":
            data_nascimento = input('Digite a data nascimento: ')

        inquilino = {"Nome": nome, "Data nascimento": data_nascimento}
       
        lista.append(inquilino)
        print('Cadastro realizado')
    
    def listar():
        for item in lista: 
            print(item)
    
    