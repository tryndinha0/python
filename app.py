# import os

# def exibir_nome_do_programa():

#     print("""
#     ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
#     ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
#     ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
#     ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
#     ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
#     ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
#     """)

# def finalizar_app():
#     os.system('cls')
#     print('Finalizando o app')



# def exibir_opcoes():
#     print('1. Cadastrar restaurante')
#     print('2. Listar restaurante')
#     print('3. Ativar restaurante')
#     print('4. Sair\n')

    







# def escolher_opcao():
#     opcao_escolhida = int(input('Escolha uma opção: '))
#     match opcao_escolhida:
#         case 1:
#             print('Cadastrar restaurante')
#         case 2:
#             print('Listar restaurante')
#         case 3:
#             print('Ativar restaurante')
#         case 4:
#             finalizar_app()
#         case _: 
#             print('opção invalida')
#     print(f'Você escolheu a opção {opcao_escolhida}')
    
        

# def main():
#     exibir_nome_do_programa()
#     exibir_opcoes()
#     escolher_opcao()

# if __name__ == '__main__':
#     main()


numero = int(input('Insira uma idade e classificaremos sua categoria: '))
if numero >= 0 and numero <= 12:
    print('É criança')
elif numero <= 18 :
    print('É adolescente!')
else:
    print('É adulto')