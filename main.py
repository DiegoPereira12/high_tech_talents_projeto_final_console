from os import system
from aluguel.cadastro_aluguel import cadastro_aluguel
from imovel.cadastro_imovel import *
from inquilino.cadastro_inquilino import *
from proprietario.cadastro_proprietario import *
import menu


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
            print('[2] - Cadastro Imóvel')
            print('[3] - Cadastro Proprietário')
            print('[4] - Cadastro Aluguel')
            opcao = input('=> ')
            
            if opcao == '1':
                system('cls')
                menu.cabecalho()
                print('Cadastrando Inquilino...')
                cadastro_inquilino()
                
            elif opcao == '2':     
                system('cls')
                menu.cabecalho()
                print('Cadastrando Imóvel...')
                cadastro_imovel()
            
            elif opcao == '3':
                system('cls')
                menu.cabecalho()
                print('Cadastrando Proprietário...')
                cadastro_properietario()

            elif opcao == '4':
                system('cls')
                menu.cabecalho()
                print('Cadastrando Aluguel...')
                cadastro_aluguel()
            
            else:
                system('cls')
                print('Opção inválida! Tente novamente')

        elif opcao == '2':
            system('cls')
            menu.cabecalho()                       
            print('[1] - Listar Inquilinos')
            print('[2] - Listar Imoveis')
            print('[3] - Listar Proprietários')
            opcao = input('=> ')

            if opcao == '1':
                system('cls')
                print('BASE DE INQUILINOS CADASTRADOS')
                print('-' * 32)  
                listar_inquilino()
            
            elif opcao =='2':
                system('cls')
                print('BASE DE IMÓVEIS CADASTRADOS')
                print('-' * 25)  
                listar_imovel()

            elif opcao =='3':
                system('cls')
                print('BASE DE PROPRIETÁRIOS CADASTRADOS')
                print('-' * 33)  
                listar_proprietario()
            
            else:
                system('cls')
                print('Opção inválida! Tente novamente')

                  
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