# Utilizando estrutura de repetição, faça um algoritmo que leia 10 valores reais, e apresente a sua soma.

soma = 0

print("\nDigite 10 valores reais para somarmos:")
for i in range(10):
  while True:
    numero = float(input("Digite um número: "))
    soma += numero

    break

print(f"A soma dos 10 número é: {numero}")