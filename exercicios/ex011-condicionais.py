# Empréstimo Bancário

casa = float(input('Qual o valor da Casa?: '))
salario = float(input('Qual o valor do salário?: '))
prestacoes = int(input('Quantos anos você vai pagar?: '))

if (casa / prestacoes ) <= salario * 0.30:
    print(f"Emprestimo aprovado, valor da mensalidade R${casa / prestacoes:.2f} e  náximo de valor que voce poderia pagar {salario * 0.30}")
else:
    print(f"Emprestimo negado, valor da mensalidade R${casa / prestacoes:.2f} e valor máximo que voce pode pagar é R$ {salario * 0.30:.2f}")