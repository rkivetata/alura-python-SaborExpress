import os

#VAI UTILIZAR SNAKE CASE exemplo_snake_case PARA NOME DE VARIAVEIS EM PYTHON

#ASPAS SIMPLES OU DUPLAS SIMPLES TRIPLICADA PARA DEIXAR A FORMTAÇÃO DO JEITO QUE FOI ESCRITO

restaurantes = ['Pizza' , 'Hamburguer']


def exibir_nome_do_programa():
    print("""

    ██████████████████████████████████████████████████████████████████████████
    █─▄▄▄▄██▀▄─██▄─▄─▀█─▄▄─█▄─▄▄▀███▄─▄▄─█▄─▀─▄█▄─▄▄─█▄─▄▄▀█▄─▄▄─█─▄▄▄▄█─▄▄▄▄█
    █▄▄▄▄─██─▀─███─▄─▀█─██─██─▄─▄████─▄█▀██▀─▀███─▄▄▄██─▄─▄██─▄█▀█▄▄▄▄─█▄▄▄▄─█
    ▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▀▀▄▄▄▄▀▄▄▀▄▄▀▀▀▄▄▄▄▄▀▄▄█▄▄▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀
        
    """)


def exibir_opcoes():
    print('1. Cadastrar restaurantes')
    print('2. Listar restaurantes')
    print('3. Ativar restaurantes')
    print('4. Sair\n')

def voltar_ao_menu_principal():
    input('Digite uma tecla pára voltar ao meno principal.\n')
    main()

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)

def finalizar_app() : 
    #VAI USAR A BIBLIOTECA OS PARA LIMPAR A TELA E VAI DAR PRINT NA TELA
    exibir_subtitulo('Encerrando o app.\n')

def opcao_invalida():
    print('Opção inválida.\n')
    voltar_ao_menu_principal()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes.\n')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar:  ') #PEDE AO USUARIO O NOME DO RESTAURANTE PARA SER CADASTRADO

    restaurantes.append(nome_do_restaurante) #ADICIONA O NOVO RESTAURANTE NA LISTA DE RESTAURANTES
    print(f'O Restaurante {nome_do_restaurante} foi cadastrado com sucessso!\n')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listar Restaurantes\n')

    #FAZER UM LOOP PARA MOSTRAR OS RESTAURANTES DA LISTA
    for restaurante in restaurantes:
        print(f'.{restaurante}\n')

    voltar_ao_menu_principal()

def escolher_opcao():
    try: #USADDO PARA QUAMNDO O USUARIO UTILIZA UMA TECLA SEM SER NUMERO INTEIRO OU OUTROS VALORES INVÁLIDOS
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1 :
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print('Ativar restaurante')
        elif opcao_escolhida == 4:
            finalizar_app()
        else: 
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls') #LIMPA A TELA
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__' :
    main()
    #SE O NOME DO PROGRAMA FOR MAIN ENTAO VAI CHAMAR A FUNÇÃO MAIN