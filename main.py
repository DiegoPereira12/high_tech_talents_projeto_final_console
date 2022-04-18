from os import system


def main():

    while True:

        print('-' * 30)
        print('Bem vindo Imobiliária SanDiego')
        print('-' * 30)
        print('Escolha uma opção:')
        print('1 - Cadastrar')
        print('2 - Listar')
        print('3 - Alterar')
        print('4 - Excluir')
        print('5 - Sair')
        opcao = input('=> ')
        
        if opcao == '1':
            system('cls')
            print('Escolha uma opção:')
            print('1 - Cadastro Inquilino')
            print('2 - Cadastro Proprietário')
            print('3 - Cadastro Imóvel')
            print('4 = Cadastro Aluguel')
            opcao = input('=> ')
            
            if opcao == '1':
                print('Inquilino')
            
            elif opcao == '2':     
                print('Propriétário')
            
            elif opcao == '3':
                print('Imóvel')

            elif opcao == '4':
                print('Aluguel')
            
            else:
                print('Opção inválida! Tente novamente')

        elif opcao == '2':
            pass

        elif opcao == '3':
            pass

        elif opcao == '4':
            pass

        elif opcao == '5':
            print('Fim do Sistema')

        else:
            print('Opção inválida! Tente novamente')
        

if __name__ == '__main__':
    main()