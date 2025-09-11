# Utilizando estrutura de repetição, faça um algoritmo que leia valores inteiros
# até que a soma dos valores lidos atinja o valor 100.

soma = 0

print("Por favor, digite um número até atingirmos 100:")

while soma < 100:    
  valor = float(input("Digite o valor: "))
  soma += valor # Adiciona o valor lido à variável 'soma'
  print("A soma de todos os valores é", soma)