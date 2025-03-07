import os

restaurantes = ['Pizza', 'Sushi', 'Lasanha', 'Churrasco']

def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def exibir_opcoes():
    print('1 - Cadastrar Restaurante')
    print('2 - Listar Restaurantes')
    print('3 - Ativar Restaurante')
    print('4 - Sair\n')

def finalizar_app():
    os.system('cls')
    print('Finalizando o app')

def opcao_invalida():
    print('Opção Inválida!')
    input('Digite uma tecla para voltar ')
    main()

def cadastrar_novo_restaurante():
    os.system('cls')
    print('Novo cadastro de Restaurantes\n')
    nome_do_restaurante = input('Digite o nome do Restaurante que deseja cadastrar: ')
    restaurantes.append(nome_do_restaurante) 
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    input('\nDigite uma tecla para voltar para o menu principal')
    main() 

def listar_restaurantes():
    os.system('cls')
    print('Listando todos os restaurantes:')
    for restaurante in restaurantes:
        print(f'- {restaurante}')
    input('\nDigite uma tecla para voltar para o menu principal')
    main() 

def escolher_opcoes():
    try:
        opcao_escolhida = int(input('Escolha uma opção: ')) 
        print(f'Você escolheu a opção: {opcao_escolhida}.')

        if opcao_escolhida == 1: 
           cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print('Ativar Restaurante')
        elif opcao_escolhida == 4:
            finalizar_app()
        else: 
            opcao_invalida()
    except ValueError:  # Captura erros de entrada inválida
        opcao_invalida() 

def main(): 
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()
