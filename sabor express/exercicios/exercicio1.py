#Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.

valor = int(input('Insira um valor\n'))

if valor % 2 == 0 :
    print('Esse valor é par')
else :
    print('Esse valor é impar')