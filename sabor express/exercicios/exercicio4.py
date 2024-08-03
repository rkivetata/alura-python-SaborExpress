#4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:

x = float(input('Digite o valor de x\n'))

y = float(input('Digite o valor de y\n'))

if (x > 0 and y > 0 ):
    print('Primeiro Quadrante')
elif (x < 0 and y > 0):
    print('Segundo Quadrante')
elif (x < 0 and y < 0):
    print('Terceiro Quadrante')
elif (x > 0 and y < 0):
    print('Quarto Quadrante')
else: 
    print('O ponto está localizado no eixo ou origem')
