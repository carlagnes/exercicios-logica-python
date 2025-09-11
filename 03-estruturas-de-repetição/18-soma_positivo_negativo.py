# Utilizando estrutura de repetição, faça um algoritmo que receba 20 valores inteiros e imprima a soma dos 
# valores positivos e a quantidade de valores negativos lidos.

qtd_negativo = 0
sum_positivo = 0


print("Digite 20 valores inteiros (positivos ou negativos).")


for i in range(4):
    while True:
            # Pede o valor dentro do laço
            valor = int(input(f"Digite o {i + 1}º valor inteiro: "))
            break # Sai do laço de validação se o valor for válido




    if valor < 0:
        qtd_negativo += 1 # Incrementa a contagem de negativos
    else: # Se não for negativo, é zero ou positivo
        sum_positivo += valor # Adiciona à soma dos positivos (inclui zero aqui)


# Os prints finais devem estar fora do laço 'for'
# para exibir os resultados depois que todos os 20 valores forem processados
print("\n--- Resultados Finais ---")
print("A soma dos números positivos é:", sum_positivo)
print("A quantidade de números negativos é:", qtd_negativo)
