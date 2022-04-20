def cabecalho():

    formartCabecalho('IMOBILIÁRIA SANDIEGO')
    
def menu_opcoes():
    print('Escolha uma opção:')
    print('[1] - Cadastrar')
    print('[2] - Listar')
    print('[3] - Alterar')
    print('[4] - Excluir')
    print('[5] - Sair')
    

def formartCabecalho(msg):
    print('=' * 40)
    print(msg.center(35))
    print('=' * 40)

