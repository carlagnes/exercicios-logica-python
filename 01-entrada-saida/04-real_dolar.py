# Faça um algoritmo que calcule a conversão de dólares para reais. O usuário deverá informar a cotação e o valor em dólares, e deverá apresentar o valor convertido em reais.

cotacao_dolar = float(input("\nInforme a cotação atual do dólar: "))
valor_dolar = float(input("Digite o valor que deseja converter para real: "))

valor_real = cotacao_dolar * valor_dolar

print("\n===== RESULTADO =====")
print(f"O valor de US$ {valor_dolar} equivale a R$ {valor_real}.")