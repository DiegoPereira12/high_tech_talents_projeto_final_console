from os import system
import menu
from inquilino.cadastro_inquilino import *

def main():
    
    while True:

        menu.cabecalho()
        menu.menu_opcoes()
        
        opcao = input('=> ')
        
        if opcao == '1':
            system('cls')
            menu.cabecalho()
            print('Selecione uma opção:')
            print('[1] - Cadastro Inquilino')
            print('[2] - Cadastro Proprietário')
            print('[3] - Cadastro Imóvel')
            print('[4] = Cadastro Aluguel')
            opcao = input('=> ')
            
            if opcao == '1':
                system('cls')
                menu.cabecalho()
                print('Cadastrando Inquilino...')
                cadastro_inquilino()
                
            elif opcao == '2':     
                print('Propriétário')
            
            elif opcao == '3':
                print('Imóvel')

            elif opcao == '4':
                print('Aluguel')
            
            else:
                system('cls')
                print('Opção inválida! Tente novamente')

        elif opcao == '2':
            system('cls')                       
            print('[1] - Listar Inquilinos')
            print('[2] - Listar Imoveis')
            print('[3] - Listar Inquilinos')
            opcao = input('=> ')

            if opcao == '1':
                system('cls')
                print('BASE DE INQUILINOS CADASTRADOS')
                print('-' * 31)  
                listar_inquilino()
                  
        elif opcao == '3':
            system('cls')
            alterar_inquilino()
            

        elif opcao == '4':
            pass

        elif opcao == '5':
            print('Fim do Sistema')
            break

        else:
            system('cls')
            print('Opção inválida! Tente novamente')
        

if __name__ == '__main__':
    main()