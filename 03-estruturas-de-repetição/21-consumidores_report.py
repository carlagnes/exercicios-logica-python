# Deseja-se estudar o perfil dos consumidores de energia elétrica de uma cidade,
# para um dado mês do ano. Para tanto, deverão ser lidos os seguintes dados para cada 
# um dos n consumidores de uma amostragem (n deve ser solicitado ao usuário no início do programa):
# consumo do mês, em kWh;
# tipo de consumidor: (1: residencial, 2: comercial e 3: industrial);
# Antes de ler os dados dos consumidores, o preço do kWh deve ser fornecido ao programa. 
# Escrever um programa em Python que leia os dados indicados acima e calcule e imprima:
# - Para cada consumidor, o total a pagar;
# - O maior consumo verificado na amostra de consumidores;
# - O menor consumo verificado na amostra de consumidores;
# - O total do consumo para cada um dos três tipos de consumidores.


# Inicializa variáveis para os resultados
maior_consumo = 0.0
menor_consumo = float('inf') # Inicializa com um valor "infinito" para garantir que qualquer consumo será menor


total_consumo_residencial = 0.0
total_consumo_comercial = 0.0
total_consumo_industrial = 0.0


# Solicita o preço do kWh no início do programa
preco_kwh = float(input("Digite o preço do kWh: "))


# Solicita o número total de consumidores na amostra
num_consumidores = int(input("Digite o número de consumidores na amostra: "))


print("\n--- Coleta de Dados dos Consumidores ---")


# Loop para ler os dados de cada consumidor
for i in range(num_consumidores):
    print(f"\n--- Dados do Consumidor {i + 1} ---")


    # Loop para garantir uma entrada de consumo válida
    while True:
        try:
            consumo_mes = float(input("Digite o consumo do mês em kWh: "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número para o consumo.")


    # Loop para garantir uma entrada de tipo de consumidor válida
    while True:
        try:
            tipo_consumidor = int(input("Digite o tipo de consumidor (1: residencial, 2: comercial, 3: industrial): "))
            if tipo_consumidor in [1, 2, 3]:
                break
            else:
                print("Tipo de consumidor inválido. Digite 1, 2 ou 3.")
        except ValueError:
            print("Entrada inválida. Por favor, digite 1, 2 ou 3.")


    # Calcula o total a pagar para o consumidor atual
    total_pagar_consumidor = consumo_mes * preco_kwh
    print(f"Total a pagar para este consumidor: R$ {total_pagar_consumidor:.2f}")


    # Atualiza o maior e o menor consumo verificados
    if consumo_mes > maior_consumo:
        maior_consumo = consumo_mes
    if consumo_mes < menor_consumo:
        menor_consumo = consumo_mes


    # Acumula o consumo de acordo com o tipo de consumidor
    if tipo_consumidor == 1:
        total_consumo_residencial += consumo_mes
    elif tipo_consumidor == 2:
        total_consumo_comercial += consumo_mes
    elif tipo_consumidor == 3:
        total_consumo_industrial += consumo_mes


# Apresenta os resultados finais após processar todos os consumidores
print("\n--- Resumo do Estudo ---")
print(f"O maior consumo verificado na amostra foi: {maior_consumo:.2f} kWh")
print(f"O menor consumo verificado na amostra foi: {menor_consumo:.2f} kWh")
print(f"Total de consumo para consumidores Residenciais: {total_consumo_residencial:.2f} kWh")
print(f"Total de consumo para consumidores Comerciais: {total_consumo_comercial:.2f} kWh")
print(f"Total de consumo para consumidores Industriais: {total_consumo_industrial:.2f} kWh")
