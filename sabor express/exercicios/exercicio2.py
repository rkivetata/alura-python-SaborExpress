#2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:

#Criança: 0 a 12 anos;
#Adolescente: 13 a 18 anos;
#Adulto: acima de 18 anos.

idade = int(input('Qual é a sua idade\n'))

if idade >= 0 and idade <=12:
    print('Criança\n')
elif idade >=13 and  idade <=18:
    print('Adolescente\n')
elif idade > 18:
    print('Adulto\n')
else:
    print('Fim')