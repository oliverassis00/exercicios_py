# Receber um número float e mostrar somente o inteiro

from math import trunc

numero = float(input('Digite um numero: '))

print(trunc(numero))

# Receber comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo. Calcular e mostrar o comprimento da hipotenusa

from math import pow, sqrt

cateto_A = float(input('Qual o tamanho do cateto A: '))
cateto_B = float(input('Qual o tamanho do cateto B: '))

hipotenusa = sqrt(pow(cateto_A, 2) + pow(cateto_B, 2))


print(f'A Hipotenusa desse triangulo é {hipotenusa:.2f}')

# Sortear um aluno para apagar o quadro

import random

sorteio = random.randint(1, 4)

aluno_1 = input('Digite o nome do aluno 1: ')
aluno_2 = input('Digite o nome do aluno 2: ')
aluno_3 = input('Digite o nome do aluno 3: ')
aluno_4 = input('Digite o nome do aluno 4: ')

if sorteio == 1:
    print(f'Numero sorteado foi {sorteio}, sendo assim, o aluno sorteado foi {aluno_1}')
elif sorteio == 2:
    print(f'Numero sorteado foi {sorteio}, sendo assim, o aluno sorteado foi {aluno_2}')
elif sorteio == 3:
    print(f'Numero sorteado foi {sorteio}, sendo assim, o aluno sorteado foi {aluno_3}')
else:
    print(f'Numero sorteado foi {sorteio}, sendo assim, o aluno sorteado foi {aluno_4}')
