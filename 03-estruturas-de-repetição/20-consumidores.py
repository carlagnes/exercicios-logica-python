# Deseja-se calcular os valores a serem pagos pelos n consumidores de energia elétrica em um prédio. 
# Faça um algoritmo que receba o custo do kWh, a quantidade de consumidores, 
# e o consumo em kWh de cada um dos consumidores.
# Apresente o valor a ser pago por cada um dos consumidores. 
# Apresente o total a ser pago por todos os consumidores do prédio

# Inicializa o total a ser pago por todos os consumidores
total_a_pagar_predio = 0.0


# Solicita o custo do kWh ao usuário
custo_kwh = float(input("Digite o custo do kWh (Ex: 0.85): "))


# Solicita a quantidade de consumidores no prédio
quantidade_consumidores = int(input("Digite a quantidade de consumidores no prédio: "))


print("\n--- Calculando o valor para cada consumidor ---")


# Loop para iterar sobre cada consumidor
for i in range(quantidade_consumidores):
    # Solicita o consumo em kWh para o consumidor atual
    consumo_kwh_consumidor = float(input(f"Digite o consumo em kWh do consumidor {i + 1}: "))


    # Calcula o valor a ser pago pelo consumidor
    valor_pagar_consumidor = custo_kwh * consumo_kwh_consumidor


    # Apresenta o valor a ser pago pelo consumidor
    print(f"O consumidor {i + 1} deve pagar: R$ {valor_pagar_consumidor:.2f}")


    # Adiciona o valor do consumidor ao total a ser pago pelo prédio
    total_a_pagar_predio += valor_pagar_consumidor


# Apresenta o total a ser pago por todos os consumidores do prédio
print(f"\n--- Resumo do Prédio ---")
print(f"O total a ser pago por todos os consumidores do prédio é: R$ {total_a_pagar_predio:.2f}")

