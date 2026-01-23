input_recebido = input('Digite algo: ')

print(f"""
O tipo primitivo desse valor é {type(input_recebido)}!
Só tem espaços? {input_recebido.isspace()}
É um número? {input_recebido.isnumeric()}
É alfabético? {input_recebido.isalpha()}
É alfanumérico? {input_recebido.isalnum()}
Está em maiúscula? {input_recebido.isupper()} 
Está em Minúscula? {input_recebido.islower()}
Está Capitalizada? {input_recebido.istitle()}
""")