from os import system
from imovel.cadastro_imovel import *
from inquilino.cadastro_inquilino import *
from proprietario.cadastro_proprietario import *
from aluguel.cadastro_aluguel import *
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
                print('OPÇÃO INVALIDA, TENTA NOVAMENTE')
                sleep(3)
                system('cls')

        elif opcao == '2':
            system('cls')
            menu.cabecalho()                       
            print('[1] - Listar Inquilinos')
            print('[2] - Listar Imoveis')
            print('[3] - Listar Proprietários')
            print('[4] - Listar Aluguéis')
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
            
            elif opcao =='4':
                system('cls')
                print('BASE DE ALUGUÉIS CADASTRADOS')
                print('-' * 33)  
                listar_aluguel()
            
            else:
                system('cls')
                print('OPÇÃO INVALIDA, TENTA NOVAMENTE')
                sleep(3)
                system('cls')
                  
        elif opcao == '3':
            system('cls')
            alterar_inquilino()
            
        elif opcao == '4':
            system('cls')
            menu.cabecalho()
            excluir_proprietario()

        elif opcao == '5':
            print('Fim do Sistema')
            break

        else:
            system('cls')
            print('OPÇÃO INVALIDA, TENTA NOVAMENTE')
            sleep(3)
            system('cls')  
        
if __name__ == '__main__':
    main()