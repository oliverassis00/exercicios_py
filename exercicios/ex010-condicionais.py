# Condicionais

# Jogo Advinhação

from random import randint

user_numero = int(input("Digite um número entre 0 e 5: "))
computer_numero = randint(0,5)



print(f"Você ganhou, numero digitado {user_numero} e o numero escolhido pelo computador {computer_numero}") if user_numero == computer_numero else print("Você perdeu!")


# Limite de Velocidade

velocidade = float(input("Digite a velocidade do veículo em KM/H: "))
multa = velocidade - 80

if velocidade > 80:
    print(f"Você passou do limite de 80 km/h da via e foi multado sobre os kms excedentes, valor da multa será de R$7,00 o km acima do limite totalizando R${multa * 7:.2f}!")
else:
    print("Parabéns, você é um ótimo motorista!")    



# Par ou Impar

numero = int(input("Digite um número: "))

print("Par") if numero % 2 == 0 else print("Impar")


# Agencia de Viagens

viagem = float(input("Qual a distancia da viagem em Km: "))
passagem_200kms = None
passagem_m200kms = None

if viagem <= 200:
   passagem_200kms = viagem * 0.50
   print(f"O valor da passagem será R${passagem_200kms:.2f}")
else:
    passagem_m200kms = viagem * 0.45
    print(f"O valor da passagem será R${passagem_m200kms:.2f}")


 
# Ano Bissexto

ano = int(input("Digite o ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print("O ano é bissexto")
else:
    print("O ano NÃO é bissexto")
     

# Maior e Menor número


n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

print(f"O Maior é {max(n1, n2, n3)} e o Menor é {min(n1, n2, n3)}")


# Aumento Salário

salario = float(input("Qual o seu salário: "))

print(f"Seu salário com o aumento de 10% será R${(salario * 0.10) + salario:.2f}") if salario <= 1250 else print(f"Seu salário com o aumento de 15% será R${(salario * 0.15) + salario:.2f}")


# Formação de um Triangulo

lado_a = float(input("Digite o lado A da reta: "))
lado_b = float(input("Digite o lado B da reta: "))
lado_c = float(input("Di8gite o lado C da reta: "))


print("Esses 3 Lados podem formar um triangulo") if (lado_a + lado_b) > lado_c and (lado_a + lado_c) > lado_b and (lado_b + lado_c) > lado_a else print("Esses lados não podem formar um triangulo")

