# Ler um número e mostrar o antecessor e o sucessor

digite_numero = int(input('Digite um número: '))

print(f'O seu antecessor é o número {digite_numero - 1} e o sucessor é o número {digite_numero + 1}!')


# Leia um número e mostre o dobro, triplo e a raiz quadrada

digite_algum_numero = int(input('Digite um número: '))

print(f'O dobro desse número é {digite_algum_numero * 2} o triplo dele é {digite_algum_numero * 3} e a raiz quadrada dele é {digite_algum_numero ** (1/2)}')


# Um programa que leia duas notas de um aluno e calcule a média

nota_1 = float(input('Digite sua primeira nota: '))
nota_2 = float(input('Digite sua segunda nota: '))
media_notas = (nota_1 + nota_2) / 2

print(f'O aluno mencionado tirou as notas respectivamente {nota_1} e {nota_2}, sendo assim, teve a média de {media_notas}!')


# Ler valores em metros e exibir convertendo para centímetros e milímetros

nota_1 = float(input('Digite o valor em metros: '))
conversao_cm = nota_1 * 100
conversao_mm = nota_1 * 1000

print(f'O valor digitado foi {nota_1} m e convertido em centímetros fica {conversao_cm} cm e em milímetros {conversao_mm} mm!')


# Pedir um número e mostrar a tabuada

digite_tabuada = int(input('Digite um número: '))

print(f"""A Tabuada do {digite_tabuada} é:
    {digite_tabuada} x 0 = {digite_tabuada * 0} 
    {digite_tabuada} x 1 = {digite_tabuada * 1} 
    {digite_tabuada} x 2 = {digite_tabuada * 2} 
    {digite_tabuada} x 3 = {digite_tabuada * 3} 
    {digite_tabuada} x 4 = {digite_tabuada * 4} 
    {digite_tabuada} x 5 = {digite_tabuada * 5} 
    {digite_tabuada} x 6 = {digite_tabuada * 6} 
    {digite_tabuada} x 7 = {digite_tabuada * 7} 
    {digite_tabuada} x 8 = {digite_tabuada * 8} 
    {digite_tabuada} x 9 = {digite_tabuada * 9} 
    {digite_tabuada} x 10 = {digite_tabuada * 10}""")


# Mostrar quantos dólares uma pessoa tem na carteira

digite_dinheiro = float(input('Digite quanto de dinheiro você tem: '))
conversao_dolar = digite_dinheiro / 5.19

print(f'Você tem R${digite_dinheiro} que em dólares americanos seriam ${conversao_dolar:.2f}')


# Calcule a área de uma parede e a quantidade de tinta necessária para pintar,
# considerando que cada litro de tinta pinta uma área de 2 m²

lateral_parede = float(input('Digite a lateral da parede: '))
altura_parede = float(input('Digite a altura da parede: '))
area_parede = lateral_parede * altura_parede
litros_tinta = area_parede / 2

print(f'A área da parede é {area_parede} e para poder pintar ela inteira, considerar {litros_tinta} litros de tinta!')


# Colocar desconto em um produto e mostrar o novo preço

preco_produto = float(input('Qual o preço do produto?: '))
desconto_produto = (preco_produto * 5) / 100
valor_final = preco_produto - desconto_produto

print(f'O preço do produto é R${preco_produto} e o valor final com desconto de 5% ficou em R${valor_final}')


# Mostrar um novo salário de funcionário com 15% de aumento

valor_salario = float(input('Qual o salário do funcionário?: '))
aumento_salario = valor_salario * 15 / 100
salario_liquido = valor_salario + aumento_salario

print(f'O salário antigo era R${valor_salario} e o valor atualizado com aumento de 15% ficou em R${salario_liquido}')

