lista = []

class Inquilino(object):   

    def __init__(self,codigo, nome, data_nascimento):
        self.codigo = codigo
        self.nome = nome
        self.data_nascimento = data_nascimento
        
    
          
    def cadastro(self, codigo, nome, data_nascimento):   

        while nome == "":
            nome = input('Digite o nome: ')
        
        while data_nascimento == "":
            data_nascimento = input('Digite a data nascimento: ')

        inquilino = {"ID":codigo, "Nome": nome, "Data nascimento": data_nascimento}

        codigo = 0
        for codigo in lista:
            codigo += 1
       
        lista.append(inquilino)
        print('Cadastro realizado')
    
    def listar():
        for item in lista:
            print(item)
       
            
    
    