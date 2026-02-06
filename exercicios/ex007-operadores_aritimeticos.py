# Pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias que foi alugado. São R$60,00 o dia e R$0,15 o KM rodado

qnt_dias = int(input('Quantos dias você alugou o veículo? : '))
km_rodado = float(input('Quantos km você rodou no veiculo? : '))
pagamento = (qnt_dias * 60) + (km_rodado * 0.15) 

print(f"Você alugou o veículo por {qnt_dias} dias e rodou {km_rodado:.0f} km, sendo assim, o valor total de pagamento ficou R$ {pagamento:.2f}")