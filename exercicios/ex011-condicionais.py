# Empréstimo Bancário

casa = float(input('Qual o valor da Casa?: '))
salario = float(input('Qual o valor do salário?: '))
prestacoes = int(input('Quantos anos você vai pagar?: '))

mensalidade = casa / (prestacoes * 12)

if mensalidade <= salario * 0.30:
    print(f"Emprestimo aprovado, valor da mensalidade R${mensalidade:.2f} e máximo de valor que voce poderia pagar R${salario * 0.30:.2f}")
else:
    print(f"Emprestimo negado, valor da mensalidade R${mensalidade:.2f} e valor máximo que voce pode pagar é R${salario * 0.30:.2f}")

# Comparação

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

if n1 > n2:
    print(f"O número {n1} é maior que o número {n2}")
elif n2 > n1:
    print(f"O número {n2} é maior que o número {n1}")
else:
    print(f"Você digitou números iguais, sendo o primeiro número {n1} e o segundo {n2}")


# Alistamento

from datetime import date

nascimento = int(input("Digite o ano de seu nascimento, por favor: "))
ano_atual = date.today().year

idade = ano_atual - nascimento
idade_dif = idade - 18

if idade < 18:
    print("Você ainda deverá se alistar quando fizer 18 anos!")
    print(f"Faltam {abs(idade_dif * 365)} dias para você se alistar")
elif idade == 18:
    print("Você deve se alistar no Exército!")
    print(f"Faltam {abs(idade_dif * 365)} dias para você se alistar")
else:
    print("Você já passou do tempo de alistamento!")
    print(f"Passou {abs(idade_dif * 365)} dias para você se alistar")


# Média alunos

nota1 = float(input("Digite a sua primeira nota: "))
nota2 = float(input("Digite a sua segunda nota: "))

media = (nota1 + nota2) / 2

if media < 5:
    print("Aluno reprovado")
elif media <= 6.9:
    print("Recuperação")
else:
    print("Aluno Aprovado!")