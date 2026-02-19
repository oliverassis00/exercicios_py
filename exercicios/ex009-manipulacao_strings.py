# # Manipulação de Strings

# Serapar um nome e contar letras

nome = input('Digite seu nome: ')
separar = nome.split()
juntar = "".join(separar)
primeiro_nome = separar[0]

print(f"""
O seu nome em maiusculo é {nome.upper()}!
O seu nome em minusculo é {nome.lower()}!
A contagem de letras do Primeiro Nome {len(primeiro_nome)}
A contagem letras {len(juntar)}!    
""")

# # Ler numero de 0 a 9999 e mostrar digitos separados

import sys

numero = int(input('Digite de 0 a 9999: '))

if numero < 0 or numero > 9999:
    print('Valor inválido')
    sys.exit()

numero = str(numero)
tamanho = len(numero)


if tamanho > 3:
    print(f"""
A unidade: {numero[3:]}
A dezena: {numero[2:3]}
A centena: {numero[1:2]}
Milhar: {numero[0]}
""")
elif tamanho > 2:
    print(f"""
A unidade: {numero[2:]}
A dezena: {numero[1:2]}
A centena: {numero[0]}
Milhar: {0}
""")  
elif tamanho > 1:
    print(f"""
A unidade: {numero[1:]}
A dezena: {numero[0:1]}
A centena: {0}
Milhar: {0}
""")  
else:
    print(f"""
A unidade: {numero[0]}
A dezena: {0}
A centena: {0}
Milhar: {0}
""")  


# Verificando primeiras letras de um texto


cidade_Alvo = "Santa Barbara D' Oeste".lower()

cidade_Nascimento = input("Em que cidade você nasceu?: ").lower().strip()

primeira_Letra = 'santa' in cidade_Nascimento

print(primeira_Letra)



# Verificar uma string dentro da outra

nome_Completo = str(input('Qual o seu nome completo?: ')).strip()

verifica_Sobrenome = 'silva' in nome_Completo.lower()

print(verifica_Sobrenome)



# Primeira e ultima ocorrencia de uma string

frase = str(input('Digite uma frase: ')).strip().lower()

contagem_A = frase.count('a')
primeiro_A = frase.find('a')
ultimo_A = frase.rfind('a')

print(f"""

A letra A aparece {contagem_A} vezes na frase.
A primeira letra A apareceu na posição {primeiro_A + 1}
A última letra A apareceu na posição {ultimo_A + 1}

""")