#3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você. 

usuario = input('Insira seu nome de usuário\n')

meu_usuario = "tatatoquinho "

minha_senha = "0711"

senha = int(input('Digite sua senha\n'))

if (usuario == meu_usuario and senha == minha_senha):
    print(f'Bem vindo {usuario}')
else:
    print('Usuário ou senha incorretos')