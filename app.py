import os

#VAI UTILIZAR SNAKE CASE exemplo_snake_case PARA NOME DE VARIAVEIS EM PYTHON

#ASPAS SIMPLES OU DUPLAS SIMPLES OU DUPLAS TRIPLICADA (PARA DEIXAR A FORMTAÇÃO DO JEITO QUE FOI ESCRITO)

restaurantes = [{'nome': 'Pizzaiollo', 'categoria': 'Pizza', 'status':True},
                {'nome': 'Tapiocca', 'categoria': 'Tapioca', 'status':False},
                {'nome': 'BurguerBrasa', 'categoria': 'Hamburguer', 'status':True}]
#vai ser utilizado o métododo DICIONÁRIO para manejar os restaurantes e seus atributos, como exemplo: nome e status

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
    print('3. Alterar status do restaurantes')
    print('4. Sair\n')
#====================================================================


def voltar_ao_menu_principal():
    input('Digite uma tecla para voltar ao meno principal.\n')
    main()
#====================================================================


def exibir_subtitulo(texto):
    #VAI USAR A BIBLIOTECA OS PARA LIMPAR A TELA E VAI
    os.system('cls')
    print(texto)
#====================================================================


def finalizar_app() : 
    # DAR PRINT NA TELA
    exibir_subtitulo('Encerrando o app.\n')
#====================================================================


def opcao_invalida():
    print('Opção inválida.\n')
    voltar_ao_menu_principal()
#====================================================================


def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes.\n')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar:  ') #PEDE AO USUARIO O NOME DO RESTAURANTE PARA SER CADASTRADO

    categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ') #PEDE A CATEGORIA DO RESTAURANTE
    dado_do_restaurante = {'nome':nome_do_restaurante, 'categoria': categoria, 'status': False } #DICIONÁRIO PARA NOME E CATERIA DO RESTAURANTE CADATSRADO
    restaurantes.append(dado_do_restaurante) #ADICIONA O NOVO RESTAURANTE NA LISTA DE RESTAURANTES
    
    print(f'O Restaurante {nome_do_restaurante} foi cadastrado com sucessso!\n')
   
    voltar_ao_menu_principal()
#====================================================================


def listar_restaurantes():
    exibir_subtitulo('Listar Restaurantes\n')

    print(f'{'Nome do restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'Status do restaurante'.ljust(20)}')


    #FAZER UM LOOP PARA MOSTRAR OS RESTAURANTES DA LISTA
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_do_restaurante = restaurante['categoria']
        status_do_restaurante = 'Ativado' if restaurante['status'] else 'Desativado'
        print(f'-{nome_restaurante.ljust(20)}| {categoria_do_restaurante.ljust(20)} | {status_do_restaurante.ljust(20)} \n')

    voltar_ao_menu_principal()
#====================================================================


def alternar_status_restaurante():
    exibir_subtitulo('Alternar o status do restaurante')

    #VAMOS PROCURAR O RESTAURANTE POR NOME
    nome_restaurante = input('Informe o nome do restaurante que deseja alterar o status: ')
    #VERIFICANDO SE O RESTAURANTE FOI ENCONTRADO 
    restaurante_encontrado = False #está falso pois ainda não foi enconmtrado

    #LOOP PARA PROCURAR O RESTAURANTE NA LISTA
    for restaurante in restaurantes:
        #SE O NOME DIGITADO AGORA FOI IGUAL AO NOME INSERIDO NA LISTA PELA CHAVE 'NOME'
        if nome_restaurante == restaurante['nome']: 
            restaurante_encontrado = True 
                #significa que ele foi encontrado
            restaurante['status'] = not restaurante['status']
                #o status do restaurante vai ficar o inverso do que ele é
            #ADICIONANDO UMA MENSAGEM
            mensagem = f'O restaurante {nome_restaurante} foi atividado com sucesso!\n' if restaurante['status'] else f'O restaurante {nome_restaurante} foi desativado com sucesso!\n'

            print(mensagem)

    if not restaurante_encontrado:
         print('O restaurante não foi encontrado')
    
    voltar_ao_menu_principal()
#====================================================================


def escolher_opcao():
    try: #USADDO PARA QUAMNDO O USUARIO UTILIZA UMA TECLA SEM SER NUMERO INTEIRO OU OUTROS VALORES INVÁLIDOS
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1 :
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
             alternar_status_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else: 
            opcao_invalida()
    except:
        opcao_invalida()
#====================================================================


def main():
    os.system('cls') #LIMPA A TELA
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()
#====================================================================


if __name__ == '__main__' :
    main()
    #SE O NOME DO PROGRAMA FOR MAIN ENTAO VAI CHAMAR A FUNÇÃO MAIN